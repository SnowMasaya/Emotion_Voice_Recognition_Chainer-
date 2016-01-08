#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from collections import namedtuple


class Parsing_anvil_model():

    def __init__(self):
        Parsing_anvil_model = namedtuple("parsing_anvil", ["track", "re_xml_index", "re_xml_index2", "re_xml_attribute", "female", "male", "index", "emotion_dect"])
        config_file = "../enviroment.yml"
        with open(config_file, encoding="utf-8") as cf:
             e = yaml.load(cf)
             self.parsing_anvil = Parsing_anvil_model(e["parsing_anvil"]["track"], e["parsing_anvil"]["re_xml_index"], e["parsing_anvil"]["re_xml_index2"], e["parsing_anvil"]["re_xml_attribute"], e["parsing_anvil"]["female"], e["parsing_anvil"]["male"], e["parsing_anvil"]["index"], e["parsing_anvil"]["emotion_dect"])
