#!/usr/bin/env python3

from os.path import join, dirname
import sys
if sys.version_info < (3, 5):
    print("Python 3.5 or newer is required", file=sys.stderr)
    sys.exit(1)

execfile(join(dirname(__file__), 'src', 'PdfLibrary', 'version.py'))

from distutils.core import setup

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

long_description=open(join(dirname(__file__), 'README.md',)).read()

setup(
  name             = 'robotframework-pdflibrary',
  version          = VERSION,
  description      = 'Robot Framework PDF Inspect Library',
  long_description = long_description,
  author           = 'bloopark systems GmbH & Co. KG',
  author_email     = 'info@bloopark.com',
  url              = 'https://github.com/blooparksystems/robotframework-pdflibrary',
  license          = 'Apache License 2.0',
  keywords         = 'robotframework checking testautomation pdf reports',
  platforms        = 'any',
  zip_safe         = False,
  classifiers      = CLASSIFIERS.splitlines(),
  package_dir      = {'' : 'src'},
  python_requires  = ' >= 3.5',
  install_requires = ['robotframework',
                      'chardet >= 3.0.4, < 4',
                      'pdfminer.six == 20181108 ; sys_platform != "darwin"',
                      'pylibdmtx',
                      'wand'],
  extras_require   = {'pdfminer': ['pdfminer.six == 20181108'],},
  packages         = ['PdfLibrary'],
)

