

Build the Project 
###################

Make HTML 
***********************

To build the HTML output for your project, open the command prompt in the top-level folder of your project (the location of the ``Makefile``).  Then enter:

.. code-block:: BASH
  
  make html

The HTML files are created in the build folder. Typically this is called ``build`` and at the same level as the ``source`` folder, although you can change this in the ``Makefile``.

Automatically Generate HTML Updates 
************************************

You can set up your project so that the HTML is automatically regenerated every time you save a change. This allows you to keep a the project open in your browser and view changes immediately.

You must install :xref:`Sphinx Autobuild`.

#. From a command prompt, enter ``pip install sphinx-autobuild``. 

#. In the ``Makefile``, add the lines:

   .. code-block:: BASH
   
     SPHINXAUTOBUILD = sphinx-autobuild

     ALLSPHINXLIVEOPTS   = $(ALLSPHINXOPTS) -q \
        -p 0 \
        -H 0.0.0.0 \
        -B \
        --delay 1 \
        --ignore "*.swp" \
        --ignore "*.pdf" \
        --ignore "*.log" \
        --ignore "*.out" \
        --ignore "*.toc" \
        --ignore "*.aux" \
        --ignore "*.idx" \
        --ignore "*.ind" \
        --ignore "*.ilg" \
        --ignore "*.tex" \
        --watch source 

     .PHONY: livehtml
     livehtml:
        $(SPHINXAUTOBUILD) -b html $(ALLSPHINXLIVEOPTS) $(BUILDDIR)
        @echo
        @echo "Build finished. The HTML pages are in $(BUILDDIR)."

#. From the command prompt, enter:

   .. code-block:: BASH
     
     make livehtml


The project is built and opens automatically in your browser.

Each time you save a file in the project, it is automatically rebuilt. Just refresh your browser.
   
.. note:: If there are errors in the project, the automatic build will not complete and the HTML will not be updated.  Check the command window for error details.


