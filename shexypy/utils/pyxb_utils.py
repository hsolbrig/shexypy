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
from pyxb import binding, SimpleFacetValueError
import pyxb.binding.facets as facets
import pyxb.binding.datatypes as datatypes


def test_numeric_facet(v, total_digits=None, fraction_digits=None):
    class Decimal (datatypes.decimal):
        pass
    init_list = []
    rval = None
    if total_digits is not None:
        Decimal._CF_totalDigits = facets.CF_totalDigits(super_facet=datatypes.decimal._CF_totalDigits, value=facets.CF_totalDigits._ValueDatatype(total_digits))
        init_list.append(Decimal._CF_totalDigits)
    if fraction_digits is not None:
        Decimal._CF_fractionDigits = facets.CF_fractionDigits(super_facet=datatypes.decimal._CF_maxExclusive, value=facets.CF_fractionDigits._ValueDatatype(fraction_digits))
        init_list.append(Decimal._CF_fractionDigits)
    if init_list:
        Decimal._InitializeFacetMap(*init_list)
    try:
        rval = Decimal(v)
    except SimpleFacetValueError:
        pass
    return float(rval) if rval else None


class PyxbWrapper:

    unicode_re = re.compile(r'\\u([a-fA-F0-9]{4})|\\U([a-fA-F0-9]{8})')

    def __init__(self, node):
        self._node = node

    @property
    def node(self):
        return self._node

    @property
    def elements(self):
        return [PyxbWrapper.PyxbElement(n) for n in self._node._validatedChildren()
                if isinstance(n, binding.basis.ElementContent)]

    class PyxbElement:
        def __init__(self, el):
            self._el = el

        @property
        def type(self):
            return self._el.elementDeclaration._ElementDeclaration__id

        @property
        def value(self):
            return PyxbWrapper(self._el.value)

    @staticmethod
    def mixed_content(item):
        return ''.join([PyxbWrapper.proc_unicode(e.value) if isinstance(e, binding.basis.NonElementContent)
                        else "toDOM(e)" for e in item.orderedContent()])

    @staticmethod
    def proc_unicode(txt):
        def map_unicode(hex_str) -> str:
            char_code = int(hex_str, 16)
            if char_code < 0xFFFF:
                return chr(char_code)
            else:
                char_code -= 0x10000
                return chr(0xD800 + (char_code >> 10)) + chr(0xDC00 + (char_code & 0x3FF))

        def unescape(t):
            """ Unescape the CODE escape characters in txt
            :param t: string to be unescaped
            :return: unescaped equivalent
            """
            return re.sub(r'\\\\', r'\\', re.sub(r'\\%', '%', t)) if t else ""

        rval = ''
        pos = 0
        utxt = unescape(txt)
        for e in PyxbWrapper.unicode_re.finditer(utxt):
            rval += utxt[pos:e.start()] + map_unicode(e.group(1))
            pos = e.end()
        return rval + utxt[pos:]


class PyxbChoice:

    def __init__(self, node):
        self._node = node

    def __getattr__(self, item):
        if item.startswith('_'):
            return self.__dict__[item]
        elif item == 'elements':
            return [PyxbChoice(n) for n in self._node._validatedChildren()]
        elif item == 'type':
            return self._node.elementDeclaration._ElementDeclaration__id
        else:
            return self._node.value if self._node.elementDeclaration._ElementDeclaration__id == item else None
