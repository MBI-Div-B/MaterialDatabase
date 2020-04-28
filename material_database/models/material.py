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

# import numpy as np


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

    def __init__(self, data_dict={}):
        self.ID = -1
        self.name = ''

    def build_from_dict(self, data_dict):
        """build_from_dict

        Some documentation here.

        """
        pass

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

    def add_parameter(self, parameter):
        """add_parameter

        Some documentation here.

        """
        pass

    def add_reference(self, reference):
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
