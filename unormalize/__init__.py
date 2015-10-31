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
import argparse
import fileinput
import unicodedata

__author__ = 'Eddie Antonio Santos'
__license__ = 'MIT'
__version__ = '0.1.0'

def process(line, form):
    r"""
    >>> from unicodedata import lookup as u
    >>> line = 'e' + u('COMBINING ACUTE ACCENT') + 'tude\n'
    >>> process(line.encode('UTF-8'))
    '\xc3\xa9tude\n'
    """
    line = line.decode('UTF-8')
    norm = unicodedata.normalize(form, line)
    return norm.encode('UTF-8')

def nfc():
    sys.exit(main(form_default='NFC'))

def nfd():
    sys.exit(main(form_default='NFD'))

def nfkc():
    sys.exit(main(form_default='NFKC'))

def nfkd():
    sys.exit(main(form_default='NFKD'))

def parse_args(form_default):
    parser = argparse.ArgumentParser(
        description='perform Unicode normalization',
    )

    parser.add_argument(
        '-f', '--form', metavar='FORM',
        help='one of nfc, nfd, nfkc, or nfkd (default is %s)' % (form_default,),
        default=form_default,
        choices=['nfc', 'nfd', 'nfkc', 'nfkd'])

    parser.add_argument(
        '-i', '--in-place', metavar='EXTENSION',
        help='Edits files in place',
        nargs='?', default=None, const='.bak')

    parser.add_argument(
        'files', metavar='FILES', nargs=argparse.REMAINDER,
        help='Zero or more files; if none given, uses stdin'
    )

    args = parser.parse_args()

    # Ensure --in-place is given with arguments.
    if args.in_place and len(args.files) < 1:
        parser.error('must specify at least one file to use -i/--in-place')

    # Uppercase the normalization form name:
    args.form = args.form.upper()
    # Add a dot to the extension.
    if args.in_place and not args.in_place.startswith('.'):
        args.in_place = '.' + args.in_place

    return args

def main(form_default='NFC', inplace=None):
    args = parse_args(form_default)
    files, form, in_place = args.files, args.form, args.in_place

    if len(files):
        all_files = fileinput.input(files, inplace=in_place and 1, backup=in_place)
    else:
        all_files = fileinput.input()

    for line in all_files:
        sys.stdout.write(process(line, form))

if __name__ == '__main__':
    sys.exit(main())
