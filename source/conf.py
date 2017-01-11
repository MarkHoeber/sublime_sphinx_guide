import sys, os
import sphinx_bootstrap_theme

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')

extensions = ['xref', 
              'youtube', 
              'sphinx.ext.autosectionlabel',
              'sphinxcontrib.osexample']

from links.link import *
from links import *


templates_path = ['_templates']
html_static_path = ["_static"]

source_suffix = '.rst'

master_doc = 'index'

project = u'RST, Sphinx, and Sublime'
copyright = u'2017, Mark Hoeber'
author = u'Mark Hoeber'

googleanalytics_id = 'UA-88078032-1'

pygments_style = 'sphinx'


todo_include_todos = True


html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {

  'navbar_site_name': "Contents",
  #'navbar_pagenav_name': "Lesson",
  'source_link_position': "footer",

  #'bootswatch_theme': "Sandstone"
}

exclude_patterns = ['links.rst', 'substitutions.rst', 'atom.rst', 
  'unused/3.rst', 'unused/4.rst', 'unused/14.rst']

rst_epilog = """
.. include:: substitutions.rst
"""
