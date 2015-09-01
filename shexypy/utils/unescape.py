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

# Regular expression and replacement strings to escape strings
from pip.backwardcompat import u

stringEscapeSequence = r'\\u([a-fA-F0-9]{4})|\\U([a-fA-F0-9]{8})|\\(.)/g,'
irirefEscapeSequence = r'\\u([a-fA-F0-9]{4})|\\re.U([a-fA-F0-9]{8})/g,'
stringEscapeReplacements = {'\\': '\\', "'": "'", '"': '"',
                             't': '\t', 'b': '\b', 'n': '\n', 'r': '\r', 'f': '\f' }
semactEscapeReplacements = {'\\': '\\', '%': '%' }


def sub_unicode4(unicode4):
    return chr(int(unicode4, 16))

def sub_unicode8(unicode8):
    char_code = int(unicode8, 16)
    if char_code < 0xFFFF:
        return int(char_code)
    else:
        char_code -= 0x10000
        return chr(0xD800 + (char_code >> 10)) + chr(0xDC00 + (char_code & 0x3FF))


def f(sequence, unicode4, unicode8, escaped_char):
    if unicode4:
        return chr(int(unicode4, 16))
    elif unicode8:
        char_code = int(unicode8, 16)
        if char_code < 0xFFFF:
            return int(char_code)
        else:
            char_code -= 0x10000
            return chr(0xD800 + (char_code >> 10)) + chr(0xDC00 + (char_code & 0x3FF))
    else:
        replacement = replacements[escaped_char]
        if not replacement:
            raise Exception()
        return replacement


def unescape(string, regex, replacements):
    def f(sequence, unicode4, unicode8, escaped_char):
        if unicode4:
            return chr(int(unicode4, 16))
        elif unicode8:
            char_code = int(unicode8, 16)
            if char_code < 0xFFFF:
                return int(char_code)
            else:
                char_code -= 0x10000
                return chr(0xD800 + (char_code >> 10)) + chr(0xDC00 + (char_code & 0x3FF))
        else:
            return replacements.get(escaped_char, None)

    return re.sub(regex, f, string)


def unescape_string(string: str, trim_length: int=0) -> str:
    if trim_length:
        string = string[trim_length:-trim_length]
    return '"' + unescape(string, stringEscapeSequence, stringEscapeReplacements) + '"'