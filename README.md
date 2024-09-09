# Visual novel interpreter and scripting language

### Video Demo: https://youtu.be/9bTLNTji_3M

### Description
This file is the documentation for this scripting language
and its interpreter

This application is designed for creating visual novels
novice authors with no previous experience
using similar applications

### Usage guide
For the correct operation of the program, it must be launched
from the Linux OS through the command line with the command

```
$ python3 start.py
```

Custom modules are also required for the program to work:

 - PyQt5
 - playsound
 - pygame

To install them, you need to execute the following commands (Fedora Linux):

```bash
$ sudo dnf install python3-pip
$ pip install --upgrade wheel
$ pip3 install PyQt5 playsound pygame
```
 

### VN creation guide

Required files, which must be located at the root of the folder:

 - start_background.png - background image of the start menu
 - text_window.png - image of a text window
 - name_window.png - image of the window for the character's name
 - logo.png - logo of the visual novel in the initial menu
 - firstScript.script - the script that starts the game

#### VN scripting language
Guide to script writing

There should be only one command per line

To display a string of text without a name:

```
"<text>"
```

 - text - some text

To display a line of text with a name:

```
"<name>" "<text>"
```

 - name - Name of the character
 - text - some text

To play a sound effect:

```
PLAY SOUND "<path>"
```

 - path - path to the file
 - The next command is read automatically

To change background music:

```
PLAY MUSIC "<path>"
```

 - path - path to the file
 - The next command is read automatically

To change the background image:

```
SCENE "<path>"
```

 - path - path to the file
 - The next command is read automatically

Adding a character image:

```
SHOW "<path>" AT <X> <Y> AS <alias>
```

 - path - path to the file
 - X - X coordinate, an integer
 - Y - Y coordinate, an integer
 - nickname - a nickname by which the character can be removed
 - The next command is read automatically

Hiding the character:

```
HIDE <alias>
```

 - nickname - nickname given when adding a character
 - The next command is read automatically

Adding an action option that will lead to a transition
to another scenario:

```
OPTION "<text>" TO "<script>"
```

 - text - the text displayed on the button
 - script - the path to the script to which the transition takes place
 - The next command is read automatically

After entering each of the options, a selection must be made
so that the next line is STOP

Jump to some line of some script (use is not desirable):

```
GOTO "<script>" SKIP <N>
```

 - script - the path to the script to which the transition takes place
 - N - the number of the line from which script reading begins

End of script:

```
END
```

To stop automatic reading of the next line
or ignoring a single user click:

```
STOP
```

When reading any line that does not match any
from the above templates, the next line is read


