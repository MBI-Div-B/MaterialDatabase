#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the material_database module.
#
# material_database is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2020 Felix Steinbach, Daniel Schick

"""A :mod:`PyYamlParser` module """

__all__ = ["PyYamlParser"]

__docformat__ = "restructuredtext"

import numpy as np
import yaml
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase


class PyYamlParser():
    """PyYamlParser

    PyYamlParser parsing data

    """
    def __init__(self, path):
        '''
        Constructor
        '''
        self.__path = path

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def load(self):
        f = open(self.__path, "r")
        yamlText = f.read()

        meta = yamlText.split("data:")[0]
        metaNoRef = meta.split("references:")[0]
        bibtex = meta.split("references:")[1]
        data = "data:"+yamlText.split("data:")[1]

        bibDict = bibtexparser.loads(bibtex).entries
        metaDict = yaml.load(metaNoRef, Loader=yaml.FullLoader)
        dataDict = yaml.load(data, Loader=yaml.FullLoader)

        metaDict["meta"]["references"] = bibDict

        dict1 = dict(metaDict, **dataDict)

        return dict1

    def dump(self, dict1):
        bibDict = dict1["meta"]["references"]

        metaDict = dict(dict1)

        del metaDict["meta"]["references"]
        del metaDict["data"]
        yamlMeta = (yaml.dump(metaDict,
                              allow_unicode=True,
                              sort_keys=False)).rstrip(" ")

        bibObj = BibDatabase()
        bibObj.entries = bibDict
        bibStr = bibtexparser.dumps(bibObj)

        splitBib = bibStr.split("\n")
        splitBib[0] = "    "+splitBib[0]
        yamlBib = ("  references: \n" + "\n     ".join(splitBib)).rstrip("\n ")

        dataDict = dict(dict1)
        del dataDict["meta"]

        yamlData = "data:\n"

        for i in dataDict["data"].keys():
            yamlData += "  " + i+":\n"
            par = dataDict["data"][i]
            for j in par.keys():

                yamlData += "    " + j+":\n"
                value = par[j]["value"]

                if(type(value) == dict):
                    tmpYaml = yaml.dump(par[j],
                                        default_flow_style=None,
                                        allow_unicode=True,
                                        sort_keys=False)
                else:
                    tmpYaml = yaml.dump(par[j],
                                        default_flow_style=False,
                                        allow_unicode=True,
                                        sort_keys=False)

                splitTmp = tmpYaml.split("\n")
                splitTmp[0] = "      "+splitTmp[0]
                yamlPar = "\n      ".join(splitTmp)
                yamlData += yamlPar

            yamlData = yamlData.rstrip(" ")

        yamlFile = yamlMeta + yamlBib + "\n" + yamlData

        return yamlFile
