#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from argparse import ArgumentParser
import os
import sys
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from make_arff import Make_arff


def parse_args():
    p = ArgumentParser(description='Choose Make arff output config')

    p.add_argument('-c', '--config', type=str, help='\'OPENSMILE_CONFIG\' or \'OPENSMILE_CONFIG_2010\'')
    p.add_argument('-o', '--output_dir', type=str, help='[output dir]  you set output dir')
    args = p.parse_args()

    # check args
    try:
        if args.config not in ['OPENSMILE_CONFIG', 'OPENSMILE_CONFIG_2010']: raise ValueError('you must set mode = \'OPENSMILE_CONFIG\' or \'OPENSMILE_CONFIG_2010\'')
        #if not args.output_dir: raise ValueError('you must set --output_dir')
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
    make_arff = Make_arff(data_path + "/wav_list")
    #make_arff.extract()

if __name__ == '__main__':
    test_input()
