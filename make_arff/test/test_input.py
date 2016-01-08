#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from input_arff import Input_arff


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass 

    def test_input(self):
        data_path = os.environ["OPENSMILE_PYTHON"]
        inputter = Input_arff(data_path + "/wav_list")
        inputter.input_data()

if __name__ == '__main__':
    unittest.main()
