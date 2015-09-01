# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
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

import xml.parsers.expat
from xml.sax.saxutils import escape, unescape

import pyxb
from pyxb.utils import domutils

from shexypy.schema import ShEx

defaultNS = ShEx.Namespace


def prettyxml(pyxb_xml, ns=None, xslt=None, toxml=True):
    """ Pretty printer for pyxb object. This differs from the standard minidom's
        toprettyxml because it doesn't touch anything inside a i{value} tag.
        
        @param pyxb_xml: The pyxb node to format
        
        @param ns: base namespace to use for encoding
        @param xslt: name of xslt module to include in header
        @param toxml: if True, convert to XML otherwise already is in XML
    """
    pyxb.defaultNamespace = ns
    domutils.BindingDOMSupport.SetDefaultNamespace(ns if ns else defaultNS)
    pyxb.RequireValidWhenGenerating(True)
    return prettyxml_(pyxb_xml.toxml(encoding='utf-8') if toxml else pyxb_xml, xslt)


def prettyxml_(rawxml, xslt=None):

    def indent(dpth, prv):
        return ('\n' + (' ' * 4 * dpth)) if prv != 'd' else ""

    def args(alist):
        if len(alist):
            return ' ' + ' '.join([k + '="' + v + '"' for (k, v) in alist.items()])
        return ''

    seq = []
    p = xml.parsers.expat.ParserCreate('UTF-8')
    p.StartElementHandler = lambda name, attrs: seq.append(('s', name, attrs))
    p.EndElementHandler = lambda name: seq.append(('e', name))
    p.CharacterDataHandler = lambda data: seq.append(('d', data))
    p.Parse(rawxml, 1)

    depth, prev, rval = (0, 'e', '<?xml version="1.0" encoding="UTF-8"?>' + (xslt if xslt else ""))
    data_text = ''
    while len(seq):
        e = seq.pop(0)
        if e[0] == 's':
            # shortcut the simple start end tag
            if seq[0][0] == 'e':
                assert e[1] == seq[0][1]
                seq.pop(0)
                rval += indent(depth + 1, prev)
                rval += '<' + e[1] + args(e[2]) + '/>'
                prev = 'e'
            else:
                if prev != 'e':
                    depth += 1
                if data_text:
                    rval += data_text
                    data_text = ''
                rval += indent(depth, prev)
                rval += '<' + e[1] + args(e[2]) + '>'
        elif e[0] == 'e':
            if prev not in ['d', 's']:
                depth -= 1
            else:
                rval += escape(unescape(data_text))
                data_text = ''
            rval += indent(depth, prev)
            rval += '</' + e[1] + '>'
        else:
            if prev != 'e' or e[0] != 'd' or e[1].strip():
                data_text += e[1]
        if prev != 'e' or e[0] != 'd' or e[1].strip():
            prev = e[0]
    return rval


def cleanxml(txt):
    if txt:
        return uncleanxml(txt).replace('&', '&amp;').replace('<', '&lt;')
    return None


def uncleanxml(txt):
    if txt:
        return txt.replace('&amp;', '&').replace('&lt;', '<')
