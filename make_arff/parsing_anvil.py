#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os


class Parsing_anvil():

    def __init__(self, anvil_list):
        self.anvil_list = anvil_list
        self.track = re.compile(".*<track name.*")
        self.re_xml_index = re.compile(".*<el index=\"\d*\" start=\"\d*\.\d*\".*")
        self.re_xml_index2 = re.compile(".*<el index=\"\d*\" start=\"\d*\" end=\"\d*\.\d*\".*")
        self.re_xml_attribute = re.compile(".*<attribute\ name=.*true.*")
        self.female = re.compile(".*track name=\"Female.*\".*")
        self.male = re.compile(".*track name=\"Male.*\".*")
        self.index = re.compile("index=\"\d*\"")
        self.emotion_dect = re.compile("name=\".*\"")
        self.emotion = {"Anger": 0, "Happiness": 1, "Excited": 2, "Sadness": 3, "Frustration": 4, "Fear": 5, "Surprise": 6, "Other": 7, "Neutral state": 8, "Disgust": 9}
        self.past_anvil = ""
        self.arff_path = os.environ["OPENSMILE_DATA"]
        self.arff_fname = ""
        self.string = ""
        self.ano_flag = ""

    def read_anvil_list(self):
        for anvil in self.anvil_list:
            f = open(anvil, 'r')
            self.__parsing(anvil)
        f.close()

    def __parsing(self, anvil):
        f = open(anvil, 'r')
        tmp_anvil = anvil
        tmp_anvil = re.sub(r'_e\d\.anvil', "_e.anvil", tmp_anvil)
        if tmp_anvil == self.past_anvil:
            return
        self.re_anvil_fname = re.compile(".*_e\d.anvil.*")
        ano_flag = 0
        anvil_last = (anvil.split("/")).pop()
        self.arff_fname = self.arff_path + anvil_last
        self.__read_parsing(f, ano_flag)
        self.past_anvil = tmp_anvil

    def __read_parsing(self, f, ano_flag):
        self.string = self.arff_fname
        past_string = self.arff_fname
        for line in f:
            self.__detect_female_mael(line, past_string)
            self.__detect_index(line)
            self.__detect_emotion(line)

    def __detect_female_mael(self, line, past_string):
        if self.track.match(line):
            if self.male.match(line):
                self.arff_fname = re.sub(r'_e\d*\.anvil', "_M0", past_string)
            if self.female.match(line):
                self.arff_fname = re.sub(r'_e\d*\.anvil', "_F0", past_string)
            self.string = self.arff_fname
        return self

    def __detect_index(self, line):
        if self.re_xml_index.match(line) or self.re_xml_index2.match(line):
            m = self.index.search(line)
            index_number = (m.group(0).replace("index=\"", "")).replace("\"", "")
            self.arff_fname = self.arff_fname + "%02d" % (int(index_number)) + ".arff"
            self.ano_flag = 0
        return self

    def __detect_emotion(self, line):
        if self.re_xml_attribute.match(line) and self.ano_flag == 0:
            m = self.emotion_dect.search(line)
            emotion = m.group(0).replace("name=\"", "").replace("\"", "")
            self.arff_fname = self.arff_fname + "," + emotion + "," + str(self.emotion[emotion])
            print(self.arff_fname)
            self.arff_fname = self.string
            self.ano_flag = 1
