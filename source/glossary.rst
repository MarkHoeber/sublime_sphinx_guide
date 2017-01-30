Add a Glossary 
###################

Sphinx has a built-in Glossary structure that you can use to:

* Produce a consolidated glossary of terms.

* Link terms in other content to their glossary definitions.

Create a Glossary
******************

To add glossary terms, you use the directive ``.. glossary::``. Write each
glossary entry as a definition list, with a term, followed by a single-line
indented definition.

Each glossary entry is nested below the ``.. Glossary::`` directive.  For
example:

.. code-block:: RST
  
  .. glossary::
           
      Sphinx 
        Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages. 

      RST
        |RST| is an easy-to-read, what-you-see-is-what-you-get plain text markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents. |RST| is designed for extensibility for specific application domains. The |RST| parser is a component of Docutils.

      Sublime Text
        Sublime Text is a sophisticated text editor for code, markup and prose. You'll love the slick user interface, extraordinary features and amazing performance.

You can list all glossary terms under a single Glossary directive, or use
multiple Glossary directives.

For more information, see the :xref:`Sphinx Glossary`.


Link a Term to its a Glossary Entry
*************************************

When a glossary term is used in text, you can link it to its definition with the
``:term:`` role. For example, to link the term :term:`Sphinx` to its definition,
use the following syntax:

.. code-block:: RST

  :term:`Sphinx`

The term specified must exactly match a term in Glossary directive.

You can link to a term in the glossary while showing different text in the topic
by including the term in angle brackets. For example:

.. code-block:: RST

  :term:`reStructuredText<RST>`

The term in angle brackets must exactly match a term in the glossary. The text
before the angle brackets is what users see on the page.
