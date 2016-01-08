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
from input_anvil import Input_anvil

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("set up")

    def test_input(self):
        data_path = os.environ["OPENSMILE_PYTHON"]
        inputter = Input_anvil(data_path + "/anvil_list")
        data = inputter.input_data()

if __name__ == '__main__':
    unittest.main()
