Add Images 
###################


You add images to |RST| with the ``.. image::`` directive:

.. code-block:: RST
  
  .. image:: path/filename.png
    :width: 400
    :alt: Alternative text

For example this image:

.. image:: images/get_started_sphinx.png
 :width: 600

Is added to the |RST| file in by the following lines:

.. code-block:: RST
  
  .. image:: images/get_started_sphinx.png
     :width: 600


Use Image Substitutions 
***********************

You can also define a :ref:`substitutions<Use a Substitution>` to reference an
image:

.. code-block:: RST
  
  .. |Substitution Name| image:: path/filename.png
    :width: 400
    :alt: Alternative text

Then add the image in content by adding the substitution name:

.. code-block:: RST
  
  The screen opens:

  |Substitution Name|

This is useful if you are using the image multiple times in a project and want
to manage it in one location.

Width
*******

You set the image width in pixels using the ``:width:`` parameter.  

Typically you want to use a width between 400 - 800 pixels.

Alt text
************

You should add alternative text for screen readers for each image using the
``:alt:`` parameter. Provide text that is useful to someone who might not be
able to see the image.
