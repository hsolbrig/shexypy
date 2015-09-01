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
import sys


def compare_dicts(d1: dict, d2: dict, d1name: str="dict1", d2name: str="dict2", file=sys.stdout, filtr=None) -> bool:
    """ Recursively compare the two dictionaries.
    :param d1: First dictionary
    :param d2: Second dictionary
    :param d1name: Name of the first dictionary
    :param d2name: Name of the second dictionary
    :param file: Output file (default: sys.stdout)
    :param filtr: comparison filter. Signature: filtr( i1: (k,v), i2: (k, v)) -> bool:
    :return: Whether the dictionaries match
    """

    def n1(k):
        return d1name + '.' + k

    def n2(k):
        return d2name + '.' + k

    def f(t1, t2):
        return False if filtr is None else filtr(t1, t2)

    if d1 == d2:
        return True

    n_errors = 0
    for e in sorted(list(set(d1.keys()) - set(d2.keys()))):
        if not f((e, d1[e]), None):
            n_errors += 1
            print("+  %s: %s" % (n1(e), d1[e]), file=file)
    for e in sorted(list(set(d2.keys()) - set(d1.keys()))):
        if not f(None, (e, d2[e])):
            n_errors += 1
            print("-  %s: %s" % (n2(e), d2[e]), file=file)
    for k, v in sorted(d1.items()):
        if k in d2 and d2[k] != d1[k] and not f((k, d1[k]), (k, d2[k])):
            if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                if not compare_dicts(d1[k], d2[k], n1(k), n2(k), file, filtr):
                    n_errors += 1
            else:
                n_errors += 1
                print("< %s: %s" % (d1name + '.' + k, d1[k]), file=file)
                print("> %s: %s" % (d2name + '.' + k, d2[k]), file=file)
    return n_errors == 0


def dict_compare(d1: dict, d2: dict, d1name: str="dict1", d2name: str="dict2", filtr=None) -> (bool, str):
    class MemFile:
        def __init__(self):
            self.text = ""

        def write(self, txt):
            self.text += txt

    of = MemFile()
    print("--- %s" % d1name, file=of)
    print("+++ %s" % d2name, file=of)
    print(file=of)
    return compare_dicts(d1, d2, d1name, d2name, file=of, filtr=filtr), of.text
