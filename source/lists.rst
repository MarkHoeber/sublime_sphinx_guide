Use Lists
##########

This topic shows how to use ordered and unordered lists in |RST|.

Ordered Lists
***************

Use hash symbols for ordered lists:

.. code-block:: RST
  
    #. Step 1.
    #. Step 2.
    #. Step 3.

.. note::
 Ordered lists usually use numerals. Nested ordered lists (ordered lists inside
 other ordered lists) use letters.

 An ordered lists should have 3-7 items.

Unordered Lists
***************

Use asterisks for unordered (bulleted) lists.

.. code-block:: RST

    * Item 1.
    * Item 2.
    * Item 3.

An unordered lists should have 3-7 items.

Unordered List Inside Ordered List
*********************************************

To include an unordered list inside an ordered list, indent the unordered list
three spaces. The first bullet in the unordered list must be flush with the
text in the ordered list.

.. code-block:: RST

    #. Step 1.

        * Item 1.

        * Item 2.

    #. Step 2.

Ordered List Inside Unordered List
*********************************************

To include an ordered list inside an unordered list, indent the ordered list
two spaces. The first number or letter of the ordered list must be flush with
the text in the unordered list.

.. code-block:: RST

    * Item 1.

      #. Step 1.

      #. Step 2.

    * Item 2.

Unordered List Inside Unordered List
*********************************************

To include an unordered list inside another unordered list, indent the second
unordered list two spaces. The first bullet of the second unordered list must
be flush with the text in the unordered list.

.. code-block:: RST

    * Item 1.

      * Item a.

      * Item b.

    * Item 2.

Ordered List inside Ordered List
*********************************************

To include another ordered list inside an ordered list, indent the second
ordered list three spaces. The second ordered list must be flush with the text
in the numbered list. The first ordered list uses numerals, and the second
uses letters.

.. code-block:: RST

    #. Step 1.

        #. Step a.

        #. Step b.

    #. Step 2.

Code, Images, and Other Content Inside Lists
*********************************************

To include content such as code or an image inside a list, position the code or
image directive flush with the text in the list. That is, indent three spaces
for ordered lists and two spaces for unordered lists.

.. code-block:: RST

    #. Step 1. Example:

        .. code-block:: bash

          Example code

    #. Step 2.
