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
from rdflib import BNode, Literal, URIRef


class Triple:
    def __init__(self, s, p, o):
        self.s = RDFTerm(s)
        self._p = RDFTerm(p)
        self.o = RDFTerm(o)

    @property
    def p(self):
        return self._p.iri


class RDFTerm:
    def __init__(self, o):
        self.o = o

    @property
    def val(self):
        return self.is_bnode if self.is_bnode else self.literal if self.is_literal else self.iri

    @property
    def is_bnode(self) -> bool:
        return isinstance(self.o, BNode)

    @property
    def bnode(self) -> BNode:
        return self.o if self.is_bnode else None

    @property
    def is_literal(self) -> bool:
        return isinstance(self.o, Literal)

    @property
    def literal(self) -> Literal:
        return self.o if self.is_literal else None

    @property
    def is_iri(self) -> bool:
        return isinstance(self.o, URIRef)

    @property
    def iri(self) -> URIRef:
        return self.o if self.is_iri else None