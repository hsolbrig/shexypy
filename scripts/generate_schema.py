#!/usr/local/bin/python

#  -*- coding: utf-8 -*-
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

# Copied from pyxbgen 1.2.3

# This module generates the shexyParser/schema/ShEx.py module from the XML Schema in the static directory

import pyxb.xmlschema
import pyxb.binding.generate
import pyxb.utils.utility
import pyxb.utils.domutils

schemaroot = "../static/xsd/"


cmdline = '--schema-root %s -u ShEx.xsd -m ShEx --binding-root=../shexyparser/schema' % schemaroot

import logging
logging.basicConfig()
log_ = logging.getLogger(__name__)


generator = pyxb.binding.generate.Generator()
parser = generator.optionParser()

(options, args) = parser.parse_args(cmdline.split())

generator.applyOptionValues(options, args)

generator.resolveExternalSchema()

if 0 == len(generator.namespaces()):
    parser.print_help()
    sys.exit(1)

import sys
import traceback

# Save binding source first, so name-in-binding is stored in the
# parsed schema file
try:
    tns = generator.namespaces().pop()
    modules = generator.bindingModules()
    print('Python for %s requires %d modules' % (tns, len(modules)))

    top_module = None
    path_dirs = set()
    for m in modules:
        m.writeToModuleFile()

    generator.writeNamespaceArchive()
except Exception as e:
    print('Exception generating bindings: %s' % (e,))
    traceback.print_exception(*sys.exc_info())
    sys.exit(3)

# LocalVariables:
# mode:python
# End:
