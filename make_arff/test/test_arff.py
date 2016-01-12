#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from make_arff import Make_arff


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("set up")

    def test_input(self):
        data_path = os.environ["OPENSMILE_PYTHON"]
        make_arff = Make_arff(data_path + "/wav_list")
        make_arff.extract()

if __name__ == '__main__':
    unittest.main()
