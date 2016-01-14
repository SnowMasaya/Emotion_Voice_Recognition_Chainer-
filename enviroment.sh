#!/bin/bash
# hoge.sh
#
# -----------------------------------------------------------------------------
# Purpose : foobarbaz
# -----------------------------------------------------------------------------
# yyyy.MM.dd created  {account}@{mail.address}
#
# Description :
#   1. hoge
#   2. fuga
#   3. piyo
#
# Usage :
#   $ hoge.sh param1 param2
#       param1 - foo
#       param2 - bar
#   Example) $ hoge.sh baz
#
#
# -----------------------------------------------------------------------------
#virtualenv -p python3.4
echo numpy > requeriment.txt
pip install -r requeriment.txt
echo export OPENSMILE_PYTHON=`pwd` > .envrc
#You set the openSMILE-x.x.x/bin/linux_x64_standalone_static/SMILExtract PATH 
echo export OPENSMILE_PATH=OPENSMILE_PATH >>.envrc
#You set the openSMILE-x.x.x/config/IS09_emotion.conf PATH 
#or
#You set the openSMILE-x.x.x/config/IS10_paraling.conf PATH 
echo export OPENSMILE_CONFIG=OPENSMILE_CONFIG_PATH >> .envrc
#You set the Data Path
echo export OPENSMILE_DATA=OPENSMILE_DATA >> .envrc
#You set the arff output Path
echo export OPENSMILE_OUTPUT=OPENSMILE_OUTPUT >> .envrc
#You set the ARFF Path
echo export OPENSMILE_ARFF=OPENSMILE_ARFF >> .envrc
direnv allow
source $OPENSMILE_PYTHON/my_env/bin/activate
