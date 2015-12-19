% UNORMALIZE(1) | Unicode Normalization
% Eddie Antonio Santos

# NAME

unormalize — convert between Unicode normalization forms

# SYNOPSIS

| unormalize \[--form={nfc,nfd,nfkc,nfkd}] \[--in-place=*EXTENSION*]
|            \[*files*...]
| nfc  \[--in-place=*EXTENSION*] \[*files*...]
| nfd  \[--in-place=*EXTENSION*] \[*files*...]
| nfkc \[--in-place=*EXTENSION*] \[*files*...]
| nfkd \[--in-place=*EXTENSION*] \[*files*...]

# DESCRIPTION

`unormalize` (and friends) converts its standard input or any files
given to it to the desired Unicode normalization form. To chose
a normalization form, either use the filter with the corresponding name,
or use the general `unormalize` tool with the `--form` argument.

By default, all output is printed to standard output; however,
`unormalize` can edit files in-place by using the `--in-place` argument.

## Options

-h, --help

: shows help message and exits.

-f *FORM*, --form *FORM*

:  One of nfc, nfd, nfkc, or nfkd (default is nfc).

   For more information,
   see [Unicode Standard Annex #15](http://unicode.org/reports/tr15/).

-i *EXTENSION*, --in-place=*EXTENSION*

:  Edits files in-place, appending *EXTENSION* to the filename of the
   back-up files.

# LICENSE

Copyright 2015 (C) Eddie Antonio Santos. MIT licensed.
