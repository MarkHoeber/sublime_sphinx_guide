"""
Imports the system and the 
theme the project is using to the project.
"""

import sys, os
import sphinx_bootstrap_theme

"""
Adds path to the folder ext, where extensions are stored.
"""

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')

"""
Tells Sphinx which extensions to use.
"""

extensions = ['xref', 
              'youtube', 
              'sphinx.ext.autosectionlabel',
              'sphinxcontrib.osexample']

"""
Imports all link files into project.
"""

from links.link import *
from links import *

"""
Tells the project where to look for theme templates and css overrides.
"""
templates_path = ['_templates']
html_static_path = ["_static"]

"""
Tells the project the name of the home page.
"""

master_doc = 'index'

"""
The project name, copyright, and author.
"""

project = u'RST | Sphinx | Sublime | GitHub'
copyright = u'2017, Mark Hoeber'
author = u'Mark Hoeber'

"""
The Google Analytics ID.
"""
googleanalytics_id = 'UA-88078032-1'

"""
Tells the project to use sphinx pygments for color coding code examples.
"""

pygments_style = 'sphinx'

"""
Tells the project to include content in todo directives.  Often set through 
parameter to make commands.
"""
todo_include_todos = True

"""
Tells the project which theme to use, and the theme options.
"""
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {

  'navbar_site_name': "Contents",
  'source_link_position': "footer",
}

"""
Tells the project to ignore certain files in the build process.
"""
exclude_patterns = ['substitutions.rst']

"""
Tells the project to append content at the end of every file during the build 
process.
"""
rst_epilog = """
.. include:: substitutions.rst
"""
