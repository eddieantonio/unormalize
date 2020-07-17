#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2015, 2017, 2020 Eddie Antonio Santos. MIT Licensed.
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

import argparse
import fileinput
import os
import sys
import unicodedata

__author__ = "Eddie Antonio Santos"
__license__ = "MIT"
__version__ = "2020.7.17"


def process(line, form):
    r"""
    >>> from unicodedata import lookup as u
    >>> line = u'e' + u('COMBINING ACUTE ACCENT') + 'tude\n'
    >>> res = process(line, 'NFC')
    >>> res == (u('LATIN SMALL LETTER E WITH ACUTE') + u'tude\n')
    True
    """
    return unicodedata.normalize(form, line)


def nfc():
    sys.exit(main(form_default="nfc"))


def nfd():
    sys.exit(main(form_default="nfd"))


def nfkc():
    sys.exit(main(form_default="nfkc"))


def nfkd():
    sys.exit(main(form_default="nfkd"))


def parse_args(form_default):
    parser = argparse.ArgumentParser(description="perform Unicode normalization",)

    parser.add_argument(
        "-f",
        "--form",
        metavar="FORM",
        help="one of nfc, nfd, nfkc, or nfkd (default is %s)" % (form_default,),
        default=form_default,
        choices=["nfc", "nfd", "nfkc", "nfkd"],
    )

    parser.add_argument(
        "-i",
        "--in-place",
        metavar="EXTENSION",
        help="Edits files in place",
        nargs="?",
        default=None,
        const=".bak",
    )

    parser.add_argument(
        "files",
        metavar="FILES",
        nargs=argparse.REMAINDER,
        help="Zero or more files; if none given, uses stdin",
    )

    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    args = parser.parse_args()

    # Ensure --in-place is given with arguments.
    if args.in_place and len(args.files) < 1:
        parser.error("must specify at least one file to use -i/--in-place")

    # Uppercase the normalization form name:
    args.form = args.form.upper()
    # Add a dot to the extension.
    if args.in_place and not args.in_place.startswith("."):
        args.in_place = "." + args.in_place

    return args


def ensure_unicode_object(text):
    if sys.version_info >= (3,):
        # Python 3+
        return text
    return text.decode("UTF-8")


def ensure_writable_output(text):
    if sys.version_info >= (3,):
        # Python 3+
        return text
    return text.encode("UTF-8")


def main(form_default="NFC"):
    args = parse_args(form_default)
    files, form, in_place = args.files, args.form, args.in_place

    if files == []:
        # read from stdin by default
        files.append("-")

    options = {}

    if in_place:
        options.update(inplace=True, backup=in_place)

    all_files = fileinput.input(files, **options)

    # fileinput.inplace redirects stdout
    for line in all_files:
        sys.stdout.write(
            ensure_writable_output(process(ensure_unicode_object(line), form))
        )


if __name__ == "__main__":
    sys.exit(main())
