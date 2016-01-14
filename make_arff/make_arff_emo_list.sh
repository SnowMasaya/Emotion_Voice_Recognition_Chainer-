#!/bin/bash
# hoge.sh
#
# -----------------------------------------------------------------------------
# Purpose : foobarbaz
# -----------------------------------------------------------------------------
# yyyy.MM.dd created  {account}@{mail.address}
#
# Description :
#   1. hoge
#   2. fuga
#   3. piyo
#
# Usage :
#   $ hoge.sh param1 param2
#       param1 - foo
#       param2 - bar
#   Example) $ hoge.sh baz
#
#
# -----------------------------------------------------------------------------
#Make arff file
python test_arff.py -c OPENSMILE_CONFIG
#arff add the label
python test_anvil_parsing.py > arff_emo_list_change_label
sort -u  arff_emo_list_change_label > arff_emo_list_change_label_sort
