#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from make_arff import Make_arff
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
        make_arff = Make_arff(data_path + "/wav_list")
        make_arff.extract()

if __name__ == '__main__':
    unittest.main()
