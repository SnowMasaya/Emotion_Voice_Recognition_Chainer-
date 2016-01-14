#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import os
import sys
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from make_arff import Make_arff

"""
   Making the arff file for weka format by using the voice.
   You can choose Make the 2 type of the arff file
   Emotion feature 2009 http://emotion-research.net/sigs/speech-sig/emotion-challenge/INTERSPEECH-Emotion-Challenge-2009_draft.pdf
   Emotion feature 2010 http://emotion-research.net/sigs/speech-sig/The%20INTERSPEECH%202010%20Paralinguistic%20Challenge.pdf
   .. note::
   Args:
       config: you can choose the how to extract the Emotion feature
       output dir: you can modified the output directory. initial directory is the output
       wav_list: you have to set the wav file list
       * If you would like to try the japanese voice you have to cut the voice. However I alreay set the japanese split voice.
       split japanese voise: OGVC_wav_split_list(wav list) and set the directory \"os.environ[\"DATA_SPLIT_PATH\"]\" 
   Output:
       arff file(Voice)
"""

def parse_args():
    p = ArgumentParser(description='Choose Make arff output config')

    p.add_argument('-c', '--config', type=str, help='\'OPENSMILE_CONFIG\' or \'OPENSMILE_CONFIG_2010\'')
    p.add_argument('-o', '--output_dir', default='output/',type=str, help='[output dir]  you set output dir')
    p.add_argument('-w', '--wav_list', default='wav_list',type=str, help='wav_list  you set wav file list')
    args = p.parse_args()

    # check args
    try:
        if args.config not in ['OPENSMILE_CONFIG', 'OPENSMILE_CONFIG_2010']: raise ValueError('you must set mode = \'OPENSMILE_CONFIG\' or \'OPENSMILE_CONFIG_2010\'')
    except Exception as ex:
        p.print_usage(file=sys.stderr)
        print(ex)
        print(sys.stderr)
        sys.exit()

    return args

def test_input():
    args = parse_args()
    data_path = os.environ["OPENSMILE_PYTHON"]
    config_file = os.environ[args.config]
    output_dir = args.output_dir
    make_arff = Make_arff(data_path + args.wav_list, config_file, output_dir)
    make_arff.extract()

if __name__ == '__main__':
    test_input()
