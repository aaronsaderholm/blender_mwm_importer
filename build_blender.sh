#!/usr/bin/env bash
# https://wiki.blender.org/index.php/Dev:Doc/Building_Blender/Mac#Building_Blender_for_macOS
# https://gist.github.com/alexlee-gk/3790bf5916649082d9d6
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e
set -x
cd $DIR
#rm -rf blender-git
#mkdir blender-git
cd blender-git
#git clone https://git.blender.org/blender.git
cd blender
git submodule update --init --recursive
git submodule foreach git checkout master
git submodule foreach git pull --rebase origin master

make