# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys

SETUP_README = u"""\
# Project Name

TODO: Write a project description

## Requirement

| name             | version  |
|:----------------:|:--------:|
| docker           | 1.9.1    |
| docker-machine   | 0.5.1    |
| docker-compose   | 1.5.2    |

TODO: Write requirement tools

## Installation

```
% INSTALL COMMAND
```

TODO: Describe the installation process

## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits
"""

SETUP_LICENSE = u"""\
The MIT License (MIT)

Copyright (c) 2015 USER_NAME

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

SETUP_GITIGNORE = u"""\
# Ignore bundler config
/.bundle

# Ignore the build directory
/build

# Ignore cache
.sass-cache
node_modules
.tmp

# Numerous always-ignore extensions
*.diff
*.err
*.orig
*.log
*.rej
*.swo
*.swp
*.vi
*~

# OS or Editor folders
.DS_Store
Thumbs.db
.cache
.project
.settings
.tmproj
.esproj
nbproject/private

# Dreamweaver added files
_notes
dwsync.xml

# Komodo
*.komodoproject
.komodotools

# Folders to ignore
.hg
.svn
.CVS
intermediate
publish
.idea

build/buildinfo.properties
build/config/buildinfo.properties

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Local setup
.python-version
"""

SETUP_GITATTRIBUTES = u"""\
* text=auto
"""

SETUP_EDITORCONFIG = u"""\
root = true

[*]

indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.css]
indent_size = 2

[*.scss]
indent_size = 2

[*.sass]
indent_size = 2

[*.html]
indent_size = 2

[*.js]
indent_size = 2

[*.php]
indent_size = 2

[*.yml]
indent_size = 2

[*.py]
indent_size = 4

[*.md]
indent_size = 4
trim_trailing_whitespace = false
"""

file_list = [
    {
        'file': 'README.md',
        'body': SETUP_README,
    },
    {
        'file': 'LICENSE',
        'body': SETUP_LICENSE,
    },
    {
        'file': '.gitignore',
        'body': SETUP_GITIGNORE,
    },
    {
        'file': '.gitattributes',
        'body': SETUP_GITATTRIBUTES,
    },
    {
        'file': '.editorconfig',
        'body': SETUP_EDITORCONFIG,
    },
]

def output(dict):
    file = dict.get('file', False)
    body = dict.get('body', False)
    with open(file, 'w') as fh:
        fh.write(body)
    print("output: {}".format(file))

def setup(argv=sys.argv[1:]):
    current_dir = os.getcwd()
    os.chdir(current_dir)
    print("[current_dir] {}".format(current_dir))
    for list in file_list:
        output(list)

if __name__ == '__main__':
    setup()
