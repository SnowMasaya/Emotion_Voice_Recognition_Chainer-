#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chainer Emotion Recognition by Voice 
Recognition Emotion by Voice.
Calculate accuracy, loss, recall, precision
bias function is the apply the bias to output
"""

from __future__ import absolute_import

import numpy as np

import chainer
from chainer import cuda
import chainer.links as L
from chainer import serializers 

import net


class Predict_Emotion():

    def __init__(self, x_data, y_data, feature, initmodel, gpu = -1):
        self.N = 5000
        self.N_test = 766
        self.total = self.N + self.N_test
        self.emotion_weight = {0: self.total / 716, 1: self.total / 325, 2: self.total / 1383, 3: self.total / 743, 4: self.total / 2066, 5: self.total / 74, 6: self.total / 17, 7: self.total / 35, 8: self.total / 404,  9: self.total / 3}
        self.x_data = x_data.astype(np.float32)
        self.x_data = np.vstack((self.x_data, self.x_data))
        self.y_data = y_data.astype(np.int32)
        self.y_data = np.vstack((self.y_data, self.y_data))
        if feature == "IS2009":
            self.input_layer = 384
        elif feature == "IS2010":
            self.input_layer = 1582
        self.n_units = 256
        self.output_layer = 10
        self.model = L.Classifier(net.EmotionRecognitionVoice(self.input_layer, self.n_units, self.output_layer))
        self.gpu = gpu
        self.__set_cpu_or_gpu()
        self.emotion = {0: "Anger", 1: "Happiness", 2: "Excited", 3: "Sadness", 4: "Frustration", 5: "Fear", 6: "Surprise", 7: "Other", 8: "Neutral state", 9: "Disgust"}
        # Init/Resume
        serializers.load_hdf5(initmodel, self.model)

    def __set_cpu_or_gpu(self):
        # Prepare multi-layer perceptron model, defined in net.py
        if self.gpu >= 0:
            cuda.get_device(self.gpu).use()
            self.model.to_gpu()
        self.xp = np if self.gpu < 0 else cuda.cupy

    def method(self):
        x_test = self.x_data
        y_test = self.y_data.astype(np.int32)

        # predict
        x = chainer.Variable(self.xp.asarray(x_test),volatile='on')
        t = chainer.Variable(self.xp.asarray(y_test),volatile='on')
        self.model(x, t)
        self.model.y.data = self.__bias(self.model.y.data, t.data)
        predict = np.argmax(self.model.y.data)
        print("Emotion       ,", self.emotion[int(np.argmax(predict[0]))])

    def __bias(self, x_data, t_data):
        weight_dict = {}
        label_count = 0
        for label in t_data:
            weight_dict[label_count] = self.emotion_weight[label]
            label_count = label_count + 1
        for i in range(len(x_data)):
            x_data[i] = x_data[i] * weight_dict[i]
        return x_data
