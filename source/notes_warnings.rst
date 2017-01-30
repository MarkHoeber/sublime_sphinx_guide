Use Notes and Warnings
######################

Use notes and warnings to make a sentence stand out visually.

In |RST|, you specify notes are warnings through directives (the ``..`` syntax).

Notes
*******

.. note::
  This is note text. Use a note for information you want the user to pay
  particular attention to.
  
  If note text runs over a line, make sure the lines wrap and are indented to
  the same level as the note tag. If formatting is incorrect, part of the note
  might not render in the HTML output.

  Notes can have more than one paragraph. Successive paragraphs must indent to
  the same level as the rest of the note.

This is how the note appears in RST:

.. code-block:: RST
  
 .. note::
    This is note text. Use a note for information you want the user to 
    pay particular attention to. 
    
    If note text runs over a line, make sure the lines wrap and are indented to 
    the same level as the note tag. If formatting is incorrect, part of the note 
    might not render in the HTML output.

    Notes can have more than one paragraph. Successive paragraphs must 
    indent to the same level as the rest of the note.


Warnings
***********

.. warning::
    This is warning text. Use a warning for information the user must
    understand to avoid negative consequences.
    
    Warnings are formatted in the same way as notes. In the same way, lines
    must be broken and indented under the warning tag.

This is how the warning appears in RST:

.. code-block:: RST

  .. warning::
      This is warning text. Use a warning for information the user must 
      understand to avoid negative consequences.
      
      Warnings are formatted in the same way as notes. In the same way, 
      lines must be broken and indented under the warning tag.
  