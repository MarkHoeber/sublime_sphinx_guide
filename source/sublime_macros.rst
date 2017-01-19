Customize Sublime
#####################

You can customize Sublime in many ways, as described below.

Set Preferences
***********************

You can set a wide variety of editor preferences.

From the **Sublime Text** menu, select **Preferences** >> **Settings**.

A new window opens with two files displayed:  the default sublime settings, and the user settings.

Do not edit the default settings. Instead, you specify custom preferences in the user settings file. User settings override default settings.

For example, the default editor font size is 10pt.  If you want 14pt text, copy the ``font-size`` attribute into the user prefernces file and change ``10`` to ``14``.

The changes are visible when you save the user preferences file.

Explore the default preferences list for settings you want to override, and add those to the user preferences list and change the values.

For example, here is my user preferences file:

.. code-block:: JSON

	{
		"color_scheme": "Packages/Color Scheme - Default/Solarized (Dark).tmTheme",
		"tab_size": 2,
		"font_size": 14,
		"font_face": "arial",
		"line_padding_top": 2,
	}


Set Shortcut Keys
**************************

You can set a shortcut keys as needed..

From the **Sublime Text** menu, select **Preferences** >> **Key Bindings**.

A new window opens with two files displayed:  the default sublime key bindings, and the user key bindings.

The key binding format is:

.. code-block:: JSON

	{ "keys": ["key+key+key"],  "command": "command_name" }

For example:

.. code-block:: JSON

	{ "keys": ["super+shift+["], "command": "prev_view" }

Do not edit the default key bindings. Instead, you specify custom key bindings in the user settings file. User settings override default settings.

The changes are active when you save the user preferences file.

Explore the default key bindings list for settings you want to override, and add those to the user preferences list and change the values.

Set Colors
****************

You can set the color scheme in the editor.  

#. From the **Sublime Text** menu, select **Preferences** >> **Color Scheme**.
#. Select from the color schemes listed.

