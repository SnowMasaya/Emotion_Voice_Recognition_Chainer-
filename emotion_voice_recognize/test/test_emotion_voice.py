#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from convert_arff_emo import Convert_arff_emo
from emotion_voice import Emotion_voice

"""
   Emotion Recognition by Voice.
   "Speech Emotion Recognition Using Deep Neural Network and Extreme
   Learning Machine"
   http://research.microsoft.com/pubs/230136/IS140441.PDF
   .. note::
   Args:
       arff_label_list: you set the arff_label file list
       feature: IS2009 orIS2010
       For example: arff_emo_list_change_label_sort
                    arff_emo_list_IS2010
   Output:
       accuracy, recall, precision, f_score
"""

def parse_args():
    p = ArgumentParser(description='Emotion recognition')

    p.add_argument('-r', '--arff_label', type=str, help='you set the arff label')
    p.add_argument('--gpu', '-g', default=-1, type=int,
                        help='GPU ID (negative value indicates CPU)')
    p.add_argument('-f', '--feature', type=str, help='\'IS2009\' or \'IS2010\'')
    args = p.parse_args()

    # check args
    try:
        if args.feature not in ['IS2009', 'IS2010']: raise ValueError('you must set mode = \'IS2009\' or \'IS2010\'')
    except Exception as ex:
        p.print_usage(file=sys.stderr)
        print(ex)
        print(sys.stderr)
        sys.exit()

    return args

def test_emotion():
    args = parse_args()
    data_path = os.environ["OPENSMILE_ARFF"]
    emolist = args.arff_label
    inputter = Convert_arff_emo(data_path + emolist)
    inputter.input_emo_list()
    first_flag = 1
    for k, v in inputter.arff_emo_list.items():
        inputter.input_data(k, v, first_flag)
        first_flag = 0
    for i in range(1, 20):
        print("iteration number,", i)
        emotion_voice = Emotion_voice(inputter.x_data, inputter.y_data, i, args.feature, args.gpu)
        emotion_voice.method()

if __name__ == '__main__':
    test_emotion()
