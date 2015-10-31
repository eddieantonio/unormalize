% UNORMALIZE(1) Unicode Normalization
% Eddie Antonio Santos
% October 30, 2015

# NAME

unormalize - convert between Unicode normalization forms

# SYNOPSIS

unormalize [--form={nfc,nfd,nfkc,nfkd}] [--in-place=EXTENSION] [*files*...]

nfc [--in-place=*EXTENSION*] [*files*...]

nfd [--in-place=*EXTENSION*] [*files*...]

nfkc [--in-place=*EXTENSION*] [*files*...]

nfkd [--in-place=*EXTENSION*] [*files*...]

# DESCRIPTION

`unormalize` (and its siblings) converts its standard input or any files
given to it to the desired Unicode normalization form. Either use the
filter with the corresponding name, or use the general `unormalize` tool
with the `--form` argument.

## Options

-h, --help
 ~ shows help message and exits

-f FORM, --form FORM
 ~ one of nfc, nfd, nfkc, or nfkd (default is NFC)

-i [EXTENSION], --in-place [EXTENSION]
 ~ Edits files in place, appending EXTENSION to the filename of the
  back-up files.

# LICENSE

MIT licensed.
