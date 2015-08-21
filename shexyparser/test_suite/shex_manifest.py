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
from rdflib import Graph, RDF, RDFS, BNode, URIRef, Namespace
from urllib.request import urlopen

shext = Namespace("http://www.w3.org/ns/shextest#")
mf = Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#")


class ShExManifestEntry:
    def __init__(self, entryuri: URIRef, g: Graph):
        self.g = g
        self.entryuri = entryuri

    def _objs(self, p):
        return self.g.objects(self.entryuri, p)

    def _single_obj(self, p):
        rval = list(self._objs(p))
        return rval[0] if rval else None

    @property
    def name(self):
        return self._single_obj(mf.name)

    @property
    def comments(self):
        return '\n'.join([str(e) for e in self._objs(RDFS.comment)])

    @property
    def status(self):
        return self._single_obj(shext.status)

    @property
    def should_parse(self):
        return self._single_obj(RDF.type) != shext.NegativeSyntax

    @property
    def should_pass(self):
        return self._single_obj(RDF.type) == shext.Valid

    @property
    def schema(self):
        schema_uri = str(self._single_obj(shext.schema))
        return urlopen(schema_uri).read().decode() if schema_uri else None

    @property
    def instances(self, fmt='n3'):
        return [self._instance(e, fmt) for e in self._objs(shext.instance)]

    @staticmethod
    def _instance(uri, fmt):
        rval = Graph()
        rval.parse(uri, format=fmt)
        return rval

    @property
    def subject_iri(self):
        return self._single_obj(shext.iri)

    @property
    def start_shape(self):
        return self._single_obj(shext.shape)

    def __str__(self):
        return str(self.name)



class ShExManifest:
    def __init__(self, file_loc, fmt='n3'):
        self.g = Graph()
        self.g.parse(file_loc, format=fmt)
        entries = []
        for s in self.g.subjects(RDF.type, mf.Manifest):
            entries += [ShExManifestEntry(e, self.g) for e in self.listify(self.g.objects(s, mf.entries))]
            self.entries = {str(e): e for e in entries}

    def listify(self, nodes: list) -> list:
        """ Flatten an RDF List structure
        :param nodes: a list of nodes
        :return: Flattened list
        """
        for n in nodes:
            if isinstance(n, BNode):
                return [o for p, o in self.g.predicate_objects(n) if p == RDF.first] + \
                    self.listify([o for p, o in self.g.predicate_objects(n) if p == RDF.rest])
            else:
                return [] if n == RDF.nil else []
