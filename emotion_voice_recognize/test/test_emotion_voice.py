#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from convert_arff_emo import Convert_arff_emo
from emotion_voice import Emotion_voice


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("set up")

    def test_input(self):
        data_path = os.environ["OPENSMILE_ARFF"]
        emolist = "/arff_emo_list_change_label_sort"
        inputter = Convert_arff_emo(data_path + emolist)
        inputter.input_emo_list()
        first_flag = 1
        for k, v in inputter.arff_emo_list.items():
            inputter.input_data(k, v, first_flag)
            first_flag = 0
        for i in range(1, 20):
            print("iteration number,", i)
            emotion_voice = Emotion_voice(inputter.x_data, inputter.y_data, i)
            emotion_voice.method()

if __name__ == '__main__':
    unittest.main()
