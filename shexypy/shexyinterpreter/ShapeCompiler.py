# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import re

from shexypy.utils.pyxb_utils import PyxbWrapper
from shexypy.schema.ShEx import *
from shexypy.utils.PrefixMap import PrefixMap


class CompiledShape:
    # The type of shape_interpreter is ShapeInterpreter
    def __init__(self, nsmap: PrefixMap, shape: Shape, shape_interpreter):
        self._shape = shape
        self.containing_schema = shape_interpreter
        w_shape = PyxbWrapper(shape)
        self.tripleconstraints = self.depth_first_triples(w_shape)
        self.predmap = {}
        mp_num = 0
        while mp_num < len(self.tripleconstraints):
            k = nsmap.uri_for(self.tripleconstraints[mp_num].predicate)
            self.predmap.setdefault(k, [])
            self.predmap[k].append(str(mp_num) + ' ')
            mp_num += 1
        self._triple_number = 0
        self._pattern = r''.join(self.depth_first_pattern(w_shape))

        # Generate an additional match for every extra predicate
        #  Extra patterns are recognized by the leading '0
        for e in self._shape.extra:
            mp_num += 1
            ptn = '0' + str(mp_num) + ' '
            k = nsmap.uri_for(e.ref)
            self.predmap.setdefault(k, [])
            self.predmap[k].append(ptn)
            self._pattern += "(" + ptn + ")*"

        self.matchpattern = re.compile(self._pattern)

    @property
    def name(self):
        return self._shape.label

    @property
    def closed(self):
        return self._shape.closed

    @staticmethod
    def cardinality(n) -> str:
        minv, maxv = n.value.node.min, n.value.node.max
        if minv == 0 and maxv == 1:
            return '?'
        elif minv == 0 and maxv == 'unbounded':
            return '*'
        elif minv == 1 and maxv == 1:
            return ''
        elif minv == 1 and maxv == 'unbounded':
            return '+'
        else:
            return '{%s,%s}' % (minv, maxv if maxv != "unbounded" else "")

    def depth_first_pattern(self, node):
        rval = []
        for n in node.elements:
            if n.type == 'tripleConstraint':
                rval += ["(" + str(self._triple_number) + " )" + self.cardinality(n)]
                self._triple_number += 1
            elif n.type == 'someOf' or n.type == 'group':
                jchar = '|' if n.type == 'someOf' else ''
                rval += ['(' + jchar.join(self.depth_first_pattern(n.value)) + ')' + self.cardinality(n)]
        return rval

    @staticmethod
    def depth_first_triples(node):
        rval = []
        for n in node.elements:
            if n.type == 'tripleConstraint':
                rval.append(n.value.node)
            else:
                rval += CompiledShape.depth_first_triples(n.value)
        return rval
