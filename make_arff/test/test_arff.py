#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import os
import sys
#you set the script path for input_anvil parsing_anvil
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from make_arff import Make_arff


"""Applies forward propagation with chaining backward references.
   Basic behavior is expressed in documentation of :class:`Function`
   class.
   .. note::
   If the :data:`~Variable.data` attribute of input variables exist on
   GPU device, then, before it calls :meth:`forward` method, the
   appropriate device is selected, so in most cases implementers do
   not need to take care of device selection.
   Args:
       inputs: Tuple of input :class:`Variable` objects. The volatile
           flags of all input variables must agree.
   Returns:
       One :class:`Variable` object or a tuple of multiple
       :class:`Variable` objects.
"""

def parse_args():
    p = ArgumentParser(description='Choose Make arff output config')

    p.add_argument('-c', '--config', type=str, help='\'OPENSMILE_CONFIG\' or \'OPENSMILE_CONFIG_2010\'')
    p.add_argument('-o', '--output_dir', default='output',type=str, help='[output dir]  you set output dir')
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
    make_arff = Make_arff(data_path + "/wav_list", config_file, output_dir)
    make_arff.extract()

if __name__ == '__main__':
    test_input()
