#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Make_arff():

    def __init__(self, wav_list):
        self.wav_list = wav_list
        self.smile_extract = os.environ["OPENSMILE_PATH"]
        self.conf_file = os.environ["OPENSMILE_CONFIG"]
        self.output_dir = os.environ["OPENSMILE_OUTPUT"]

    def extract(self):
        f = open(self.wav_list, 'r')
        for line in f:
            wav_list = line.replace("\n", "")
            wav_list_split = line.replace("\n", "").split("/")
            output_files = self.output_dir + wav_list_split[len(wav_list_split) - 1].replace("wav", "arff")
            extract_code = "%s -C %s -I %s -O %s" % (self.smile_extract, self.conf_file, wav_list, output_files)
            print(extract_code)
            os.system(extract_code)
