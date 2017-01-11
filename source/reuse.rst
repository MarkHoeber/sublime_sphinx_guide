

Reuse Content
###################

Sphinx supports several ways to reuse content within and across projects.

`Use a Substitution`_ to reuse short, inline content.

`Include a Shared File`_ to reuse longer, more complex content.

Use a Substitution
********************

For common, short content, use RST :term:`substitutions<Substitution>`. 

For example, use a substitution for a product name. To print the product name in a topic, enter ``|Product|``. For example:

.. code-block:: RST
  
  Set |Product| configuration properties by . . .

The value of ``|Product|`` is defined in a substitution definition:

.. code-block:: RST
  
  .. |Product| replace:: SoftTech Analyzer

The generated documentation from this example is:

.. code-block:: RST
  
  Set SoftTech Analyzer configuration properties by . . .

If you then change the replace value of the substitution, the new value is
used in all instances when you rebuild the project.

You can define a substitution in any RST file in the project. To keep the
project organized and have substitutions easily discoverable by other team
members, you can include all substitutions in a file that is included in every
other project file.

For more information, see the :xref:`Sphinx Substitutions`.

Include a Shared File
***********************

You can store complex content, such as tasks, or code samples, in a file that
is then included in multiple.

If you are working on multiple projects, you can save entire topics in shared
files, and include those files in multiple projects.

You add a shared file to content in your project with the ``.. include::`` directive. For example:

.. code-block:: RST
  
  .. include:: ../shared/folder/filename.rst

The contents of the shared file will then be built in the project.

.. caution:: Include paths are relative to the file in the document project, not the file in shared content.

.. note:: You must reference the shared file from a file within the project. You cannot use a direct TOC reference to files outside of the project directory.
