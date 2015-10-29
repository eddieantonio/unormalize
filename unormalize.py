#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
unormalize [args] [FILES]

nfc [args] [files]
nfd [args] [files]

Converts files or standard input to the given format.

Options

    -i EXTENSION -- Modify files inplace, saving back-ups with EXTENSION
    -f FORMAT -- normalization form; default is NFC.

"""

import os
import sys
import unicodedata
import fileinput

def process(line, form='NFC'):
    r"""
    >>> from unicodedata import lookup as u
    >>> line = 'e' + u('COMBINING ACUTE ACCENT') + 'tude\n'
    >>> process(line.encode('UTF-8'))
    '\xc3\xa9tude\n'
    """
    line = line.decode('UTF-8')
    norm = unicodedata.normalize(form, line)
    return norm.encode('UTF-8')

def get_form(program_name):
    name = os.path.basename(program_name)
    if name in ['nfc', 'nfd', 'nfkc', 'nfkd']:
        return name.upper()
    return None

def main(program_name, *arguments):
    form = get_form(program_name) or 'NFC'
    for line in fileinput.input():
        sys.stdout.write(process(line, form))

if __name__ == '__main__':
    main(*sys.argv)
