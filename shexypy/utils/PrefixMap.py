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
import pyxb.namespace
from rdflib import URIRef
from shexypy.schema.ShEx import Schema


class PrefixMap:

    """ Prefix to URI mapping.  This performs both PNAME_NS / PNAME_LN and ATPNAME_NS / ATPNAME_LN mapping.
    """
    def __init__(self, schema: Schema, dom_schema):
        """ Create a prefix to URI mapping.  We take advantage of the rdflib tools to manage this
        :param schema: ShEx Schema instance to derive mapping from
        :param dom_schema: DOM representation of the Schema document
        """
        self._nsc = pyxb.namespace.NamespaceContext.GetNodeContext(dom_schema.documentElement)
        self._map = {prefix: str(url) for prefix, url in self._nsc.inScopeNamespaces().items()}
        if schema.default_namespace:
            self._map[''] = schema.default_namespace

    def uri_for(self, iri: str) -> str:
        """ Return the URI form of the supplied IRI.  We use the presence of "://" in the incoming string to deterime
        whether it is in QName or IRI format
        :param iri: IRI to be mapped
        :return: mapped IRI
        """
        if iri and ':' in iri and '://' not in iri:
            ns, local = iri.split(':', 1)
            if ':' not in local and ns in self._map:
                return self._map[ns] + local
        elif ':' not in iri and iri in self._map:
            return self._map[iri]
        return str(URIRef(iri)) if iri is not None else ""

    def namespaces(self):
        return self._map