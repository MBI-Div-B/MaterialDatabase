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

"""A :mod:`Material` module """

__all__ = ["Material"]

__docformat__ = "restructuredtext"

import logging
import re
from .parameter import Parameter
from .reference import Reference
from ..helpers import name_to_identifer


class Material():
    """Material

    Material holding information of pyhsical parameters

    Args:
        data_dict: dictionary holding all information of the material

    Attributes:
        ID (int): unique integer ID
        name (str): name of the material
        description (str): description of properties of the material
        last_updated (str): date of the last update (YYYY-MM-DD)
        parameters (dict): dictionary holding paramter objects
        references (dics): dictionary holding references

    """

    def __init__(self, material_data={}, log_level=logging.WARNING):
        self.logger = logging.getLogger(__name__)
        self.log_level = log_level
        self.logger.setLevel(level=self.log_level)

        self.ID = -1
        self.name = ''
        self.description = ''
        self.comment = ''
        self.last_updated = ''
        self.parameters = {}
        self.references = {}
        if material_data:
            self.build_from_dict(material_data)

    def build_from_dict(self, material_data):
        """build_from_dict

        Some documentation here.

        """
        self.ID = material_data['ID']
        self.name = material_data['meta']['name']
        self.description = material_data['meta']['description']
        self.comment = material_data['meta']['comment']
        self.last_updated = material_data['meta']['last_updated']

        # add references
        for ref_ID, ref_data in material_data['meta']['references'].items():
            ID = name_to_identifer(ref_ID)
            self.references[ID] = Reference(ID, ref_data)
            self.logger.info('added reference with key {:s}'.format(ID))

        for par_name, par_data in material_data['data'].items():
            name = name_to_identifer(par_name)
            self.__dict__[name] = Parameter(name, par_data, log_level=self.log_level)
            self.logger.info('added parameter with name {:s}'.format(name))

    def dump_to_dict(self):
        """dump_to_dict

        Some documentation here.

        """
        pass

    def validate(self):
        """validate

        Some documentation here.

        """
        pass

    def add_parameter(self, parameter_dict):
        """add_parameter

        Some documentation here.

        """
        pass

    def add_reference(self, reference_dict):
        """add_reference

        Some documentation here.

        """
        pass

    def list_parameters(self):
        """list_parameters

        Some documentation here.

        """
        pass

    def list_references(self):
        """list_references

        Some documentation here.

        """
        pass
