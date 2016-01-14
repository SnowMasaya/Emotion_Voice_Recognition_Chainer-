#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
import re


class Convert_arff_emo():

    def __init__(self, file_name):
        self.file_name = file_name
        self.x_data = numpy.array([], dtype=numpy.float32)
        self.y_data = numpy.array([])
        self.y_vector = []
        self.arff_emo_list = {}

    def input_emo_list(self):
        f = open(self.file_name, 'r')
        for line in f:
            r_line = line.replace("\n", "")
            arff_emo_list = r_line.split(",")
            if arff_emo_list[0] in self.arff_emo_list:
                continue
            else:
                self.arff_emo_list.update({arff_emo_list[0]: arff_emo_list[2]})

    def input_data(self, arff_name, label, first_flag):
        f = open(arff_name, 'r')
        data_re = re.compile("^@data")
        reader_flag = 0
        for line in f:
            if data_re.match(line):
                reader_flag = 1
                continue
            if reader_flag == 1:
                reader_flag = 2
                continue
            if reader_flag == 2:
                vec_data = line.split(",")
                first_flag = self.__input_vector(vec_data, first_flag, label)
        f.close()

    def __input_vector(self, vec_data, first_flag, label):
        del vec_data[0]
        y_data = (vec_data.pop()).replace("\n", "")
        y_data = y_data.replace("?", label)
        self.y_vector.append(y_data)
        x_vector = numpy.array(vec_data, dtype=numpy.float32)
        if first_flag == 1:
            self.x_data = numpy.hstack((self.x_data, x_vector))
            self.y_data = numpy.array(self.y_vector)
            first_flag = 0
        else:
            self.x_data = numpy.vstack((self.x_data, x_vector))
            self.y_data = numpy.array(self.y_vector)
        return first_flag
