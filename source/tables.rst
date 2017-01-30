Use Tables 
###################

Tables are very useful for presenting complex information.  With |RST| and Sphinx, you can create tables in several ways.

List Table Directive
***********************

You can add |RST| table syntax with ``.. list-table::`` directive.

Each table has the number of columns and their associated relative widths
indicated in a width tag.

For proper formatting, the asterisk indicating each row must align vertically,
and the hyphens indicating each column must also align. Empty cells must be
accounted for, so that each column in a row is always marked, even if there is
no content in the table cell. An example of an empty cell is the second column
in the first row of the following example.

.. code-block:: RST
  :emphasize-lines: 9

  .. list-table:: Title
     :widths: 25 25 50
     :header-rows: 1

     * - Heading row 1, column 1
       - Heading row 1, column 2
       - Heading row 1, column 3
     * - Row 1, column 1
       - 
       - Row 1, column 3
     * - Row 2, column 1
       - Row 2, column 2
       - Row 2, column 3

The table is displayed in HTML as:

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     - 
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3

CSV Files 
***********************

It's often easier to create tables in a program like Excel than with RST
syntax. You can then save the table as a CSV file, and reference the CSV file
in your |RST| file where you want the table to go.

When you have a CSV file, reference it with the ``.. csv-table::`` directive.
For widths, use the percentage width of each column (without the ``%`` sign).
For header rows, typically use 1.

Make sure the parameters match the content of the CSV file.

.. code-block:: RST

  .. csv-table:: Table Title
     :file: CSV file path and name
     :widths: 30, 70
     :header-rows: 1

Within the CSV file, you can use RST markup just as you would if writing in
directly in the RST file.
