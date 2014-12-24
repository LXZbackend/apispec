# -*- coding: utf-8 -*-

import sys
import os

from marshmallow.compat import OrderedDict
sys.path.insert(0, os.path.abspath('..'))
import smore

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

primary_domain = 'py'
default_role = 'py:obj'

intersphinx_mapping = {
    'python': ('http://python.readthedocs.org/en/latest/', None),
    'webargs': ('http://webargs.readthedocs.org/en/latest/', None),
    'marshmallow': ('http://marshmallow.readthedocs.org/en/latest/', None),
}

source_suffix = '.rst'
master_doc = 'index'
project = u'smore'
copyright = u'Steven Loria 2014'

version = release = smore.__version__

exclude_patterns = ['_build']

# THEME

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]