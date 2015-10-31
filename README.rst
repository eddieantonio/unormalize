**************************************************
unormalize - Filters that do Unicode normalization
**************************************************

Converts UTF-8 input to the desired UTF-8 in Unicode normalization form.

Read about the `Unicode Normalization Forms`_!

=====
Usage
=====

There are five executables included, that all have the exact same usage and
arguments:

- unormalize
- nfc
- nfd
- nfkc
- nfkd

You may either redirect or pipe input into `unormalize` (and its buddies), or
provide filenames as arguments.

-------
Options
-------

``-f FORM``/``--form=FORM``
  Selects the normalization form: one of NFC, NFD, NFKC, or NFKD. The
  equivalently named executables imply their respective normalization form;
  ``unormalize`` is equivilent to ``nfk`` without the ``--form`` arugment.

``-i EXTENSION``/``--in-place EXTENSION``
  Filenames **must** be specified as arguments. If so, this opens them, and
  converts them into the desired normalization form, in place. ``EXTENSION`` is
  the extension given to back-ups of the original files.

========
Examples
========

Convert clipboard contents to NFC (OS X)::

    $ pbpaste | nfc | pbcopy

Convert a file, in-place, to NFKD::

    $ nfkd --in-place=.bak file.txt && rm file.txt.bak

Convert circled, variants, and half-widths to their compatible forms::

    $ echo 'ℍ①ｶ' | nfkc 
    H1カ

=======
License
=======

© 2015 Eddie Antonio Santos. MIT Licensed.

.. _`Unicode Normalization Forms`: http://unicode.org/reports/tr15/
