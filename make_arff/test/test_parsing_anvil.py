#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import subprocess 
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from input_anvil import Input_anvil
from parsing_anvil import Parsing_anvil


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_input(self):
        data_path = os.environ["OPENSMILE_PYTHON"]
        inputter = Input_anvil(data_path + "/anvil_list")
        data = inputter.input_data()
        parsing = Parsing_anvil(data)
        parsing.read_anvil_list()

if __name__ == '__main__':
    unittest.main()
