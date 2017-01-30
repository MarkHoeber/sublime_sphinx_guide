
Write Topics
#############

A topic, or page, explains to users "what, why, and how".  Typically a topic
should be short and focused on a single subject.

A |RST| file in a project becomes one HTML page in the document.

Typically a topic starts by explaining abstract ideas and introducing
terminology. Then the topic covers how users accomplish specific tasks.

Topic Outline
**************

You can use the outline below to start a new topic:

.. code-block:: RST
  
  Topic Title
  ###########

  High-level overview of topic.

  What is ?
  **********

  High level conceptual information (Heading 2).

  At a minimum, a concept includes the following components.

  * A title, phrased as a gerund or question.
  * One or more body paragraphs.

  Complex concepts may contain 2 or more subsections.

  What is <part of subject> ?
  ============================

  When you need to break down a subject, you can break it down into subsections (H3s). Typically you would have 0 H3s, or 2+ H3s.


  What is <part of subject> ?
  ============================

  When you need to break down a subject, you can break it down into subsections (H3s)

  Do this
  **********

  A task typically follows conceptual information. Task titles should be imperative. Tasks should have a short introduction sentence that captures the user's goal and introduces the steps, for example, "Verify your products are in the catalog:"

  A task should have 3 - 7 steps.  Tasks with more should be broken down into digestible chunks.

  Intro sentence.

  #. Step 1.

  #. Step 2.

  #. Step 3.

  Following the steps, you should add the result and any follow-up tasks needed.

Use Headings
*************

In |RST|, the level of a heading is indicated by a series of symbols below the
heading text. You can use any symbols, as long as you use them
consistently for each level.

This document uses the following symbols:

* H1: pound symbols (#)
* H2: asterisk (*)
* H3: equals symbol (=)


For example: 

.. code-block:: RST
  
  Heading 1
  ###########

  The top level heading on any file, underscored by #. use for the topic title.

  Heading 2
  **********

  The second level heading in a topic. Use for high-level concepts, tasks, or
  reference information.

  Heading 3
  ===========

  The 3rd level heading in a topic. Use for breaking down conceptual
  information into understandable chunks.

.. note:: Heading text cannot extend beyond the markers. If translated heading
  text is longer than the original English text, make sure to extend the markers
  so that they are at least the same length as translated text.
