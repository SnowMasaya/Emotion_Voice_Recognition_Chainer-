Chainer with Speech Emotion Recognition
====

This tool is the Speech Emotion Recognition

<img src="https://qiita-image-store.s3.amazonaws.com/0/10496/1012efb4-b348-e755-12f1-aa970a9b11fa.jpeg" alt="赤ちゃん" width="400" height="300" />

## Japanese Reference Page

http://tech-sketch.jp/2015/10/chainer.html

## Description
This tool is recognition emotion by humam voice

If you see the detail about it, you see the below<br> 
##Requirements

    Python 3.4+
    NumPy
    chainer
    PyYAML
    OpenSMILE http://www.audeering.com/research/opensmile 
#
### Install

You have to install OpenSMILE

http://www.audeering.com/research-and-open-source/files/openSMILE-book-latest.pdf

```
apt-get install direnv
apt-get install virtualenv 
apt-get install libhdf5-dev
```

You edit the enviroment.sh

1: You choose python version<br>
2: You set the "Your Chainer Path"<br> 
3: You set the "Your OpenSMILE Path"<br> 
4: You set the "Your OpenSMILE Config Path"<br> 
5: You set the "Your VirtualEnv Path"<br> 

```
virtualenv -p python3.xx
echo numpy > requeriment.txt
pip install -r requeriment.txt
echo export OPENSMILE_PYTHON=`pwd` > .envrc
#You set the openSMILE-x.x.x/bin/linux_x64_standalone_static/SMILExtract PATH 
echo export OPENSMILE_PATH=OPENSMILE_PATH >>.envrc
#You set the openSMILE-x.x.x/config/IS09_emotion.conf PATH 
#or
#You set the openSMILE-x.x.x/config/IS10_paraling.conf PATH 
echo export OPENSMILE_CONFIG=OPENSMILE_CONFIG_PATH >> .envrc
#You set the Data Path for Parsing Info file
echo export OPENSMILE_DATA=OPENSMILE_DATA >> .envrc
#You set the arff output Path
echo export OPENSMILE_OUTPUT=OPENSMILE_OUTPUT >> .envrc
#You set the ARFF Path
echo export OPENSMILE_ARFF=OPENSMILE_ARFF >> .envrc
direnv allow
source $OPENSMILE_PYTHON/my_env/bin/activate
```

```
sh enviroment.sh
```
#
### Usage 
#
Prepare arff file
If you don't know how to make a arff file please read below repository
https://github.com/tech-sketch/Make-arff-for-Emotion-reconize-by-voice
```
*You execute python example
**prepare arff file
python make_arff/test/test_arff.py --config OPENSMILE_CONFIG
**chainer learn
python emotion_voice_recognize/test/test_emotion_voice.py --arff_label arff_emo_list_change_label_sort --feature IS2009 
```
#
### Licence
#
```
The MIT License (MIT)

Copyright (c) 2015 Masaya Ogushi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
#
### Author
#
[SnowMasaya](https://github.com/SnowMasaya)
### References 
#
>[Chainer]http://chainer.org/<br>
[OpenSMILE]http://www.audeering.com/research/opensmile<br> 
[Baby Picture]https://www.pakutaso.com/ 
