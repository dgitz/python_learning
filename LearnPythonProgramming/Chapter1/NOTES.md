# Virtual Environments
__Install__<br>
`sudo apt install python3-venv`

__Usage-Start__<br>

`cd <project>`<br>
`python3 -m venv lpp3ed`<br>
`source ./lpp3ed/bin/activate`<br>

__Usage-Stop__<br>
`deactivate`

# Pip Requirements
View Requirements:<br>
`cd <project>`<br>
`cat requirements`<br>


# Code Organization

To tell Python that a folder is a "python package", create an empty file in the folder called `__init__.py`

# Scopes

`local`: The innermost scope and contains local names.<br>
`enclosing`:The scope of any enclosing function.  Contains non-local names and non-globalnames.<br>
`global`: Contains global names.<br>
`built-in`: Contains the built-in names.  Includes: `print`, `all`, `abs`, etc.<br>

Scopes are scannedwhen when looking for a name by the order: (L)ocal->(E)nclosing->(G)lobal->(B)uilt-in.

# Objects and Classes

* Objects are instances of classes.

# Guidelines for writing good Code

__PEP8__ informs of guidelines for Python aesthetics.

