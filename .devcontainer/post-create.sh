#!/bin/bash

source $1/.devcontainer/configit.sh $1

# Linux utils
sudo apt-get update
sudo apt-get install -y tree

sudo apt-get install tk -y
sudo apt-get install -y python3-pip
pip3 install -U --user --upgrade pip
pip3 install mypy -U --user
pip3 install jupyter -U --user --force-reinstall 
pip3 install ipykernel -U --user --force-reinstall
