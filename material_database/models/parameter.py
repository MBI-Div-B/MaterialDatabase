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

"""A :mod:`Parameter` module """

__all__ = ["Parameter"]

__docformat__ = "restructuredtext"

import logging


class Parameter():
    """Parameter

    Parameter holding information of pyhsical parameters

    """

    def __init__(self, name, data, log_level=logging.WARNING):
        self.logger = logging.getLogger(__name__)
        self.log_level = log_level
        self.logger.setLevel(level=self.log_level)
        self.name = name
        #self.__ref_ID = ''
        self.__value = 0
        self.__uncertainty = 0
        self.__unit = ''
        self.__comment = ''

        i = 0
        for ref_ID, parameter_dict in data.items():
            #self.__dict__[ref_ID] = parameter_dict
            if i == 0:
                # we populate the data of the first references directly as attributes
                self.ref_ID = ref_ID
                print(parameter_dict['value'])
                # self.value = parameter_dict['value']
                for k_first, v_first in parameter_dict.items():
                    setattr(self, k_first, v_first)
            i += 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.logger.info('setting the value is not that simple')
        self.logger.info('we need to change the value also in the dict of the corresponding '
                         'reference ID: "{:s}"'.format(self.ref_ID))
        self.__value = v
        #self.__dict__[self.ref_ID]['value'] = v

    @property
    def uncertainty(self):
        return self.__uncertainty

    @uncertainty.setter
    def uncertainty(self, v):
        self.logger.info('setting the value is not that simple')
        self.logger.info('we need to change the value also in the dict of the corresponding '
                         'reference ID: "{:s}"'.format(self.ref_ID))
        self.__uncertainty = v
        #self.__dict__[self.ref_ID]['value'] = v

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, v):
        self.logger.info('setting the value is not that simple')
        self.logger.info('we need to change the value also in the dict of the corresponding '
                         'reference ID: "{:s}"'.format(self.ref_ID))
        self.__comment = v
        #self.__dict__[self.ref_ID]['value'] = v

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, v):
        self.logger.info('setting the value is not that simple')
        self.logger.info('we need to change the value also in the dict of the corresponding '
                         'reference ID: "{:s}"'.format(self.ref_ID))
        self.__unit = v
        #self.__dict__[self.ref_ID]['value'] = v


    def dump(self):
        output = ''
        for key, value in self.__dict__.items():
            if key != 'logger':
                if isinstance(value, dict):
                    output += '{:s}:\n'.format(key)
                    for sub_key, sub_value in value.items():
                        output += '\t{:s}: {:s}\n'.format(sub_key, str(sub_value))
                else:
                    output += '{:s}: {:s}\n'.format(key, str(value))
        print(output)
