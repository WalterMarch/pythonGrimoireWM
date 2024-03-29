# Python Grimoire

## a book of Python (programming) magic

The repository is based on the [devcontainerPythonGUIWM](https://github.com/WalterMarch/devcontainerPythonGUIWM) template repo and is a part of the larger [Grimoire Programmatica](https://github.com/WalterMarch/grimoireprogrammatica) project.

I'm currently a Software Engineer specializing in Python. These scripts and concepts will likely still be simple and may not always follow best practices because these are meant to be notes.

### Repository Structure

To enhance the magic theme, I'm going to use the following structure:

* [essentials](essentials/) - learning the basics of Python
* [cantrips](cantrips/) - code snippets
* [spells](spells/) - more complete programs or functions
* [marginalia](marginalia) - miscellany jotted down for future reference and/or development.

## miscellany

`configit.sh` looks like this:

```bash
#!/bin/bash

git config --global user.email "yourEmail@mail.com"
git config --global user.name "yourGitUserName"
git config --global push.autoSetupRemote true

git config --global --add safe.directory $1
```
