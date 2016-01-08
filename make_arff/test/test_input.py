#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from input_arff import Input_arff
import os
import sys
import commands 
wd = commands.getoutput("echo $CHAINER_PYTHON")
sys.path.append(wd)


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("set up")

    def test_input(self):
        data_path = os.environ["OPENSMILE_PYTHON"]
        inputter = Input_arff(data_path + "/data/data2.txt")
        inputter.input_data()

if __name__ == '__main__':
    unittest.main()
