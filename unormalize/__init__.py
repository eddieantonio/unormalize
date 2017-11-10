#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2015, 2017 Eddie Antonio Santos. MIT Licensed.
# See LICENSE for details.

"""
Normalizes files or standard input using a Unicode normalization form.

Usage:

    unormalize [-f FORM] [-i EXT] [files...]
    nfc [-i EXTENSION] [files...]
    nfd [-i EXTENSION] [files...]
    nfkc [-i EXTENSION] [files...]
    nfkd [-i EXTENSION] [files...]

Options

    -i EXTENSION -- Modify files inplace, saving back-ups with EXTENSION
    -f FORM-- normalization form
"""

import os
import sys
import argparse
import fileinput
import unicodedata

__author__ = 'Eddie Antonio Santos'
__license__ = 'MIT'
__version__ = '0.2.0'


def process(line, form):
    r"""
    >>> from unicodedata import lookup as u
    >>> line = 'e' + u('COMBINING ACUTE ACCENT') + 'tude\n'
    >>> process(line.encode('UTF-8'), 'NFC')
    '\xc3\xa9tude\n'
    """
    line = line.decode('UTF-8')
    norm = unicodedata.normalize(form, line)
    return norm.encode('UTF-8')


def nfc():
    sys.exit(main(form_default='nfc'))


def nfd():
    sys.exit(main(form_default='nfd'))


def nfkc():
    sys.exit(main(form_default='nfkc'))


def nfkd():
    sys.exit(main(form_default='nfkd'))


def parse_args(form_default):
    parser = argparse.ArgumentParser(
        description='perform Unicode normalization',
    )

    parser.add_argument(
        '-f', '--form', metavar='FORM',
        help='one of nfc, nfd, nfkc, or nfkd (default is %s)' %
             (form_default,),
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

    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s ' + __version__
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


def main(form_default='NFC'):
    args = parse_args(form_default)
    files, form, in_place = args.files, args.form, args.in_place

    if len(files):
        if in_place:
            all_files = fileinput.input(files, inplace=True, backup=in_place)
        else:
            all_files = fileinput.input(files)
    else:
        all_files = fileinput.input()

    # fileinput.inplace redirects stdout
    for line in all_files:
        sys.stdout.write(process(line, form))


if __name__ == '__main__':
    sys.exit(main())
