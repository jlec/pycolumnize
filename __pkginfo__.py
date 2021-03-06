"""packaging information"""
# Things that change more often go here.
copyright   = '''
Copyright (C) 2008-2010, 2013, 2015 Rocky Bernstein <rocky@gnu.org>.
'''
classifiers =  ['Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: Python Software Foundation License',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules',
                ]

# The rest in alphabetic order
author       = "Rocky Bernstein"
author_email = "rocky@gnu.org"
ftp_url      = None
license      = 'PSF2'
mailing_list = None
modname      = 'columnize'

short_desc = 'Format a simple (i.e. not nested) list into aligned columns.'
py_modules = [modname]

# VERSION.py sets variable VERSION.
import os.path
exec(compile(open(os.path.join(os.path.dirname(__file__), 'VERSION.py')).read(), os.path.join(os.path.dirname(__file__), 'VERSION.py'), 'exec'))

web = 'https://github.com/rocky/pycolumnize'
# tracebacks in zip files are funky and not debuggable
zip_safe = False

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

readme = 'README.txt'
if os.path.exists('README.rst'): readme = 'README.rst'
long_description   = ( read(readme) + '\n' )
