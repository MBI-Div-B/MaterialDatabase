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

import yaml
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase


class PyYamlParser():
    """PyYamlParser

    PyYamlParser parsing data

    """

    def __init__(self, path):
        self.path = path

    def load(self):
        """load a yaml file

        load a yaml from the given path and return a dictionary.

        """
        # read yaml file
        yaml_file = open(self.path, 'r')
        yaml_text = yaml_file.read()

        # split yaml string into three strings for the three different
        # sections meta, references and data
        meta = yaml_text.split('data:')[0]
        meta_no_ref = meta.split('references:')[0]
        bibtex = meta.split('references:')[1]
        data = 'data:' + yaml_text.split('data:')[1]

        # convert references string into bibtex dictionary
        bib_dict = bibtexparser.loads(bibtex).entries
        # convert meta and data string into dictionaries
        meta_dict = yaml.load(meta_no_ref, Loader=yaml.FullLoader)
        data_dict = yaml.load(data, Loader=yaml.FullLoader)

        # insert the bibtex dict into the meta dict
        meta_dict["meta"]["references"] = bib_dict

        # concat the meta and the data dict to one dict which is then returned.
        dict1 = dict(meta_dict, **data_dict)

        return dict1

    def dump(self, material_data):
        """dump dictionary to yaml file

        converts a dictionary into a yaml file which is returned by this function

        """

        # divide the dict into three dict. BibDict contains the references,
        # metaDict contains the meta dates and dataDict contains the data.
        bib_dict = material_data["meta"]["references"]
        meta_dict = dict(material_data)
        data_dict = dict(material_data)

        del meta_dict["meta"]["references"]
        del meta_dict["data"]

        del data_dict["meta"]

        # convert the meta dict to a yaml string
        yaml_meta = (yaml.dump(meta_dict,
                               allow_unicode=True,
                               sort_keys=False)).rstrip(" ")

        # convert the reference data into bibtex strings
        bib_obj = BibDatabase()
        bib_obj.entries = bib_dict
        bib_str = bibtexparser.dumps(bib_obj)

        # add four spaces in front of each bibtex line and
        # insert a reference header with two spaces in front
        split_Bib = bib_str.split("\n")
        split_Bib[0] = '    '+split_Bib[0]
        yaml_bib = ('  references: \n' + '\n     '.join(split_Bib)).rstrip('\n ')

        # add a data header
        yaml_data = 'data:\n'

        '''
        Loop through the parameter names and reference names and add each key
        to the yaml data string.
        The data string has two spaces in front and the reference name four spaces.
        The type of value determines which flow_style is used to convert the
        value dict into a yaml string.
        Values that are dict are converted as flow_style = None and
        scalar values as flow_style = False
        '''

        for par_name in data_dict['data'].keys():
            yaml_data += '  ' + par_name+':\n'
            par = data_dict['data'][par_name]
            for ref_name in par.keys():

                yaml_data += '    ' + ref_name + ':\n'
                value = par[ref_name]['value']

                if(type(value) == dict):
                    tmp_yaml = yaml.dump(par[ref_name],
                                         default_flow_style=None,
                                         allow_unicode=True,
                                         sort_keys=False)
                else:
                    tmp_yaml = yaml.dump(par[ref_name],
                                         default_flow_style=False,
                                         allow_unicode=True,
                                         sort_keys=False)

                # Six spaces are added in front of each value line.
                split_tmp = tmp_yaml.split('\n')
                split_tmp[0] = '      ' + split_tmp[0]
                yaml_par = '\n      '.join(split_tmp)
                yaml_data += yaml_par

            yaml_data = yaml_data.rstrip(' ')

        # Concat the meta, references and data yaml string and return it
        yamlFile = yaml_meta + yaml_bib + '\n' + yaml_data

        return yamlFile
