#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

class Input_arff():

    def __init__(self, file_name):
        self.file_name = file_name
        self.x_data = numpy.array([])
        self.y_data = numpy.array([])

    def input_data(self):
        f = open(self.file_name, 'r')
        first_flag = 1
        for line in f:
            vec_data = line.split(",")
            y_data = (vec_data.pop()).replace("\n", "")
            y_vector = numpy.array([y_data])
            x_vector = numpy.array(vec_data)
            if first_flag == 1:
               self.x_data = numpy.hstack((self.x_data, x_vector))
               self.y_data = numpy.hstack((self.y_data, y_vector))
               first_flag = 0
            else:
               self.x_data = numpy.vstack((self.x_data, x_vector))
               self.y_data = numpy.hstack((self.y_data, y_vector))
        f.close()
