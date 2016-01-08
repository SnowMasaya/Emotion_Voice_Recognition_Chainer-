#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
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
