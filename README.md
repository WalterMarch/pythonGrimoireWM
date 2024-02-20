# Python Grimoire

## a book of Python (programming) magic

The repository is based on the [devcontainerPythonGUIWM](https://github.com/WalterMarch/devcontainerPythonGUIWM) template repo and is a part of the larger [Grimoire Programmatica](https://github.com/WalterMarch/grimoireprogrammatica) project.

I'm currently a Software Engineer specializing in Python. These scripts and concepts will likely still be simple and may not always follow best practices because these are meant to be notes.

## The code

Files (mostly Jupyter notebooks) in the `concepts` directory illustrate various concepts/ideas/built-ins related to Python.

Files in `scripts_and_functions` are complete Python scripts or functions meant to be used in other code.

`tools.md` briefly touches on the use of the Python-related tools in this devcontainer.

## miscellany

`configit.sh` looks like this:

```bash
#!/bin/bash

git config --global user.email "yourEmail@mail.com"
git config --global user.name "yourGitUserName"
git config --global push.autoSetupRemote true

git config --global --add safe.directory $1
```
