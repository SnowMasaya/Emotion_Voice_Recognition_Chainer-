#!/usr/bin/env python
# -*- coding: utf-8 -*-
import chainer
import chainer.functions as F
import chainer.links as L


class EmotionRecognitionVoice(chainer.Chain):

    """Multi-layer perceptron for Emotion Recognition Voice.
    This is a very simple implementation of an Emotion Recognition Voice. You can modify this code to
    build your own neural net.
    """
    def __init__(self, n_in, n_units, n_out):
        super(EmotionRecognitionVoice, self).__init__(
            l1=L.Linear(n_in, n_units),
            l2=L.Linear(n_units, n_units),
            l3=L.Linear(n_units, n_out),
        )

    def __call__(self, x):
        h1 = F.sigmoid(self.l1(x))
        h2 = F.sigmoid(self.l2(h1))
        return self.l3(h2)
