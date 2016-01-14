#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Make_arff():

    def __init__(self, wav_list, config_file, output_dir):
        self.wav_list = wav_list
        self.smile_extract = os.environ["OPENSMILE_PATH"]
        self.config_file = config_file
        self.output_dir = output_dir

    def extract(self):
        print(self.config_file)
        print(self.output_dir)
        f = open(self.wav_list, 'r')
        for line in f:
            wav_list = line.replace("\n", "")
            wav_list_split = line.replace("\n", "").split("/")
            output_files = self.output_dir + wav_list_split[len(wav_list_split) - 1].replace("wav", "arff")
            extract_code = "%s -C %s -I %s -O %s" % (self.smile_extract, self.config_file, wav_list, output_files)
            print(extract_code)
            os.system(extract_code)
