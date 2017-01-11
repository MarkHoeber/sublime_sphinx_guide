
Use Snippets as Shortcuts
#################################

Snippets are short fragments of text that you use frequently. Use snippets to
save yourself tedious typing. Snippets are smart templates that will insert
text for you and adapt it to their context.

You can associate snippets with triggers, that is, specific keystrokes.  For
example, if you configured a snippet for an RST ordered list with the trigger
``ol``, when you enter ``ul``, the following snippet is added at the cursor::

  #. Step one.

  #. Step two.

  #. Step three.

After it's added at the cursor, you can edit the snippet as needed. You can
configure the snippet so you can tab through subsequent parts of the text.

The following video demonstrates using some custom snippets for common RST structures.

.. youtube:: 1FBhdtQe1MQ

Snippets are stored on your computer. To share snippets within a team, you
must manually share the snippet files.

For a good overview of snippets, see :xref:`Snippets Doc`.


Add a Snippet 
***********************

You add a snippet in Sublime.

#. From the **Tools** menu, select **Developer** >> **New Snippet**.

   A new file opens with the snippet template:

   .. code-block:: XML
      
      <snippet>
        <content><![CDATA[
      Hello, ${1:name} is a ${2:snippet}.
      ]]></content>
        <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
        <!-- <tabTrigger>keystrokes</tabTrigger> -->
        <!-- Optional: Set a scope to limit where the snippet will trigger -->
        <!-- <scope>source.rst</scope> -->
      </snippet>
    
#. Modify the content within ``[CDATA[``.

   * To be able to tab through text fields in the snippet, use ``${n:text}``, where ``n`` is the number for the tab order, and ``text`` is the default text in the snippet.

   * To add a key shortcut, uncomment the ``<tabTrigger>`` element and enter the keystrokes that will add the snippet:

     .. code-block:: XML
        
        <tabTrigger>code</tabTrigger>

#. Save the file.

You can then add the snippet to RST files by typing the tab trigger text.

Example Snippets 
***********************

You can create snippets to suit your needs. Anything you find yourself
repeating is a good candidate for a snippet. Following are snippets for common RST
uses. You can copy the files for these snippets from the repository for this document into your Sublime user package.

H1 
=========================

.. literalinclude:: snippets/h1.sublime-snippet
   :language: xml

H2 
=========================

.. literalinclude:: snippets/h2.sublime-snippet
   :language: xml

H3
=========================

.. literalinclude:: snippets/h3.sublime-snippet
   :language: xml


Anchor
=========================

.. literalinclude:: snippets/anchor.sublime-snippet
   :language: xml


Code
=========================

.. literalinclude:: snippets/code.sublime-snippet
   :language: xml

File Include
=========================

.. literalinclude:: snippets/include.sublime-snippet
   :language: xml

List
=========================

.. literalinclude:: snippets/list.sublime-snippet
   :language: xml

Internal Reference
=========================

.. literalinclude:: snippets/ref.sublime-snippet
   :language: xml

Steps
=========================

.. literalinclude:: snippets/steps.sublime-snippet
   :language: xml


Substitution
=========================

.. literalinclude:: snippets/sub.sublime-snippet
   :language: xml

Index Page TOC
=========================

.. literalinclude:: snippets/toc.sublime-snippet
   :language: xml

External Link
=========================

.. literalinclude:: snippets/xref.sublime-snippet
   :language: xml

YouTube Video
=========================

.. literalinclude:: snippets/youtube.sublime-snippet
   :language: xml

