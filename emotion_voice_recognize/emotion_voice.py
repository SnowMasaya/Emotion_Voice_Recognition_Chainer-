#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chainer Emotion Recognition by Voice 
Recognition Emotion by Voice.
Calculate accuracy, loss, recall, precision
bias function is the apply the bias to output
"""

from __future__ import absolute_import
from sklearn import preprocessing
from sklearn.metrics import recall_score, precision_score, f1_score

import numpy as np
import six

import chainer
from chainer import computational_graph
from chainer import cuda
import chainer.links as L
from chainer import optimizers
from chainer import serializers

import net


class Emotion_voice():

    def __init__(self, x_data, y_data, iteration_number, feature, gpu = -1):
        self.N = 5000
        self.N_test = 766
        self.total = self.N + self.N_test
        self.emotion_weight = {0: self.total / 716, 1: self.total / 325, 2: self.total / 1383, 3: self.total / 743, 4: self.total / 2066, 5: self.total / 74, 6: self.total / 17, 7: self.total / 35, 8: self.total / 404,  9: self.total / 3}
        self.label_precision = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,  9: 0}
        self.label_counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,  9: 0}
        self.label_data = [0, 1, 2, 3, 4, 5, 6, 7, 8,  9]
        self.x_data = x_data.astype(np.float32)
        self.y_data = y_data.astype(np.int32)
        self.y_predict_data = [] 
        scaler = preprocessing.StandardScaler()
        self.x_data = scaler.fit_transform(self.x_data)
        self.iteration_number = iteration_number
        if feature == "IS2009":
            self.input_layer = 384
        elif feature == "IS2010":
            self.input_layer = 1582 
        self.n_units = 256
        self.output_layer = 10 
        self.batchsize = 25 
        self.model = L.Classifier(net.EmotionRecognitionVoice(self.input_layer, self.n_units, self.output_layer))
        self.gpu = gpu
        self.__set_cpu_or_gpu()

    def __set_cpu_or_gpu(self):
        # Prepare multi-layer perceptron model, defined in net.py
        if self.gpu >= 0:
            cuda.get_device(self.gpu).use()
            self.model.to_gpu()
        self.xp = np if self.gpu < 0 else cuda.cupy

    def method(self):
        x_train, x_test = np.split(self.x_data, [self.N])
        y_train, y_test = np.split(self.y_data.astype(np.int32), [self.N])
        self.N_test = y_test.size
        optimizer = optimizers.SGD()
        optimizer.setup(self.model)
        for k in self.label_counter.keys():
            self.label_counter[k] = 0
        for epoch in range(self.iteration_number):
            perm = np.random.permutation(self.N)

            sum_accuracy = 0
            sum_loss = 0
            for i in six.moves.range(0, self.N, self.batchsize):
                x = chainer.Variable(self.xp.asarray(x_train[perm[i:i + self.batchsize]]))
                t = chainer.Variable(self.xp.asarray(y_train[perm[i:i + self.batchsize]]))

                # Pass the loss function (Classifier defines it) and its arguments
                optimizer.update(self.model, x, t)

                if epoch == 1 and i == 0:
                    with open('graph.dot', 'w') as o:
                        g = computational_graph.build_computational_graph(
                            (self.model.loss, ), remove_split=True)
                        o.write(g.dump())
                    print('graph generated')

                #Apply the bias for output
                self.model.y.data = self.__bias(self.model.y.data, t.data)
                sum_loss += float(self.model.loss.data) * len(t.data)
                sum_accuracy += float(self.model.accuracy.data) * len(t.data)

            print('train mean loss={}, accuracy={}'.format(
                sum_loss / self.N, sum_accuracy / self.N))

        # evaluation
        sum_accuracy = 0
        sum_loss = 0
        self.y_predict_data = []
        sum_loss, sum_accuracy = 0, 0
        sum_recall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sum_precision = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sum_f_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in six.moves.range(0, self.N_test, self.batchsize):
            x = chainer.Variable(self.xp.asarray(x_test[i:i + self.batchsize]),
                                 volatile='on')
            t = chainer.Variable(self.xp.asarray(y_test[i:i + self.batchsize]),
                                 volatile='on')
            loss = self.model(x, t)
            for i in range(len(self.model.y.data)):
                self.y_predict_data.append(np.argmax(self.model.y.data[i]))
            sum_loss += float(loss.data) * len(t.data)
            sum_accuracy += float(self.model.accuracy.data) * len(t.data)
            sum_precision, sum_recall, sum_f_score = self.__calculate_metrics(t, sum_precision, sum_recall, sum_f_score)
            self.y_predict_data = []

        print('test  mean loss={}, accuracy={}'.format(
            sum_loss / self.N_test, sum_accuracy / self.N_test))        
        mean_recall = [n/self.N_test for n in sum_recall]
        mean_precision = [n/self.N_test for n in sum_precision]
        mean_f_score = [n/self.N_test for n in sum_f_score]
        print("mean_recall     ,", [x for x in mean_recall])
        print("mean_precision  ,", [x for x in mean_precision])
        print("mean_f_score  ,", [x for x in mean_f_score])
        # Save the model and the optimizer
        print('save the model')
        serializers.save_hdf5('emotion_recognition.model', self.model)
        print('save the optimizer')
        serializers.save_hdf5('emotion_recognition.state', optimizer)

    def __bias(self, x_data, t_data):
        weight_dict = {}
        label_count = 0
        for label in t_data:
            weight_dict[label_count] = self.emotion_weight[label]
            label_count = label_count + 1
        for i in range(len(x_data)):
            x_data[i] = x_data[i] * weight_dict[i]
        return x_data

    def __calculate_metrics(self, t, sum_precision, sum_recall, sum_f_score):
       tmp_precision = [n * self.batchsize for n in precision_score(t.data.tolist(), self.y_predict_data, labels=self.label_data, average=None)]
       sum_precision = [sum_precision[i] + tmp_precision[i] for i in range(len(tmp_precision))]
       tmp_recall = [n * self.batchsize for n in recall_score(t.data.tolist(), self.y_predict_data, labels=self.label_data, average=None)]
       sum_recall = [sum_recall[i] + tmp_recall[i] for i in range(len(tmp_recall))]
       tmp_f_score = [n * self.batchsize for n in f1_score(t.data.tolist(), self.y_predict_data, labels=self.label_data, average=None)]
       sum_f_score = [sum_f_score[i] + tmp_f_score[i] for i in range(len(tmp_f_score))]
       return sum_precision, sum_recall, sum_f_score
