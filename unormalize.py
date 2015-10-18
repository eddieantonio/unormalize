#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import unicodedata
import fileinput

def process(line):
    r"""
    >>> from unicodedata import lookup as u
    >>> line = 'e' + u('COMBINING ACUTE ACCENT') + 'tude\n'
    >>> process(line.encode('UTF-8'))
    '\xc3\xa9tude\n'
    """
    line = line.decode('UTF-8')
    norm = unicodedata.normalize('NFC', line)
    return norm.encode('UTF-8')

if __name__ == '__main__':
    for line in fileinput.input():
        sys.stdout.write(process(line))
