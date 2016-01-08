#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Input_anvil():

    def __init__(self, file_name):
        self.file_name = file_name

    def input_data(self):
        f = open(self.file_name, 'r')
        anvil_list = Input_anvil.read_line(f)
        return anvil_list

    @staticmethod
    def read_line(f):
        anvil_list = []
        for line in f:
            data = line.replace("\n", "")
            anvil_list.append(data)
        f.close()
        anvil_list.sort()
        return anvil_list
