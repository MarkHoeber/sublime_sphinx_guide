

Show Example Code 
###################

To show example code, use the |RST| ``codeblock`` directive:

.. code-block:: RST

 .. codeblock:: language

    code

By specifying the language, you enable *pygments*, which show syntax color
coding for that code sample. (Ensure that your project ``conf.py`` file
contains ``pygments_style = 'sphinx')``.

If you might use the same example code in multiple parts of the document or
multiple documents, you can save it as a separate file and include it
directly:

.. code-block:: RST

  .. include:: my_code_example.txt

The included file must start with the codeblock directive.

Alternatively, you can use the ``literalinclude`` directive to include an
actual code file:

.. code-block:: RST

  .. literalinclude:: configuration.json
    :language: JSON

You could add code-block directives for different languages as :ref:`snippets<Use Snippets as Shortcuts>`.

Show Line Numbers 
***********************

You can add line numbers to code examples with the ``:linenos:`` parameter.

.. code-block:: RST
  :linenos:

  .. code-block:: javascript
    :linenos:

    code . . .

Highlight Lines 
***********************

You can have certain lines in an example highlighted line numbers to code examples with the ``:emphasize-lines:`` parameter. In the following example, line 2 (with the ``:emphasize-lines:`` directive) is highlighted.

.. code-block:: RST
 :emphasize-lines: 2

  .. code-block:: javascript
    :emphasize-lines: 8,10,16

    code . . .

Code Examples in Multiple Languages
*************************************

You might want to show code examples in multiple languages. You can use the
``sphinxcontrib-osexample`` extension to create code examples to be displayed
in a tabbed list.  For example:

.. example-code::

  .. code-block:: JSON

    {
      "key": "value"
    }

  .. code-block:: python

    pygments_style = 'sphinx'

  
  .. code-block:: ruby

    print "Hello, World!\n"


To enable tabs for multiple code examples, add ``sphinxcontrib.osexample`` to
the list of extensions in the ``conf.py`` file:

.. code-block:: python

  extensions = ['sphinx.ext.autosectionlabel',
                'sphinxcontrib.osexample']

Then, to show multiple code examples with tabs, embed the code blocks under the ``.. example-code::`` directive.  The RST text for the code block example above is:

.. code-block:: RST

  .. example-code::

    .. code-block:: JSON

      {
        "key": "value"
      }

    .. code-block:: python

      pygments_style = 'sphinx'

    
    .. code-block:: ruby

      print "Hello, World!\n"


Examples 
***********************

The following examples show code blocks in different languages, with automatic
syntax color coding.

JSON
=========

.. code-block:: JSON

  {
    "key": "value"
  }

Source:

.. code-block:: RST

  .. code-block:: JSON

    {
      "key": "value"
    }


RST
=========

.. code-block:: RST

  .. code-block:: RST

Source:

.. code-block:: RST

  .. code-block:: RST

    .. code-block:: RST

Python 
=========

.. code-block:: python

  pygments_style = 'sphinx'

Source:

.. code-block:: RST

  .. code-block:: python

      pygments_style = 'sphinx'

Ruby
=========

.. code-block:: ruby

  print "Hello, World!\n"

Source:

.. code-block:: RST

  .. code-block:: ruby

    print "Hello, World!\n"
    

Javascript
============

.. code-block:: javascript

  alert('Hello, World!')

Source:

.. code-block:: RST

  .. code-block:: javascript

    alert('Hello, World!')

HTML
=========

.. code-block:: HTML

  <h1 class="title">Title</h1>

Source:

.. code-block:: RST

  .. code-block:: HTML

    <h1 class="title">Title</h1>

XML
=========

.. code-block:: XML

    <name>Mark</name>

Source:

.. code-block:: RST

  .. code-block:: XML

      <name>Mark</name>
