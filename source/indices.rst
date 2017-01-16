Create Tables of Contents
###########################

When you create new topics, you must add them to a TOC in the project.

You can add topics to the main TOC in the main index file. Or you can add them
to TOCs in other files to create a second level in your document.

You add files in the ``.. toctree::`` directive, using the file name (RST
extension is not necessary.) See :xref:`Sphinx TOC Tree Documentation` for
more information.

For example, the main index file for this project contains 5 separate TOCs.
They are broken up in order to use headings for each part.

.. literalinclude:: index.RST
  :language: RST

If you add a file to the project and do not include it in a TOC, it will not
be built, and you will get a warning when building the project, unless you add
it to the excluded files in the ``conf.py`` file.

Depth 
***********************

In this project, only the top-level headings are listed in to TOC. You can
include other levels in an indented list by setting the ``:maxdepth:``
parameter to ``2`` or higher:

.. code-block:: RST

  .. toctree::
   :maxdepth: 2

In this example, second-level headings will be indented under the topic title
in the TOC.

Numbered Sections 
***********************

You can automatically generate numbered topics and sections by adding the
``:numbered:`` parameter to the ``.. toctree`` directive:

.. code-block:: RST

  .. toctree::
   :numbered:

Each topic and section is then numbered consecutively in the output.
