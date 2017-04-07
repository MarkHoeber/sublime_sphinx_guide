Use Conditional Text 
#####################

Sphinx supports conditional text. That is, you can specify that some content is visible only to the intended audience. You can then build different versions of the project for different audiences

To limit visibility of certain content, indent that content under an ``.. only::`` directive. For example, to specify that some content is available only to internal audiences, use:

.. code-block:: RST
  
  .. only:: Internal
    
    Content to be included only in the internal version of the document.

Build Projects with Conditions 
********************************

When you use conditions, you must use the ``-t audience`` flag in the build command to specify which version of the project to build.

For example, the default command to build HTML in a project Makefile is:

.. code-block:: bash
   
   .PHONY: html
   html:
    $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)
    @echo
    @echo "Build finished. The HTML pages are in $(BUILDDIR)."
 

If you use this command (``make html``) to build the project, the resulting HTML will **not** include content indented under the ``.. only:: Internal`` directive.

To build a project that does include this conditional content, add a command to your Makefile with the parameter ``-t Internal``:

.. code-block:: bash
  :emphasize-lines: 3

  .PHONY: internalhtml
   internalhtml:
    $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) -t Internal $(INTERNALBUILDDIR)
    @echo
    @echo "Build finished. The HTML pages are in $(INTERNALBUILDDIR)."

Then build the project with ``make internalhtml``. The resulting HTML will
include the internal-only content.

.. note:: This example assumes you have defined **INTERNALBUILDDIR** as a separate location for the built files.  You do not want to place them in the same directory as those files built without the conditional text, and have them overwrite the other project.


