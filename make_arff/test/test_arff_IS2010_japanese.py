#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import commands
wd = commands.getoutput("echo $CHAINER_PYTHON")
sys.path.append(wd)
wd = commands.getoutput("echo $OPENSMILE_PYTHON")
sys.path.append(wd)
from make_arff_2010_japanese import Make_arff_2010_Japanese


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("set up")

    def test_input(self):
        data_path = os.environ["DATA_SPLIT_PATH"]
        make_arff = Make_arff_2010_Japanese(data_path + "/OGVC_wav_split_list")
        make_arff.extract()

if __name__ == '__main__':
    unittest.main()
