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

"""A :mod:`Reference` module """

__all__ = ["Reference"]

__docformat__ = "restructuredtext"

import logging


class Reference():
    """Reference

    Reference holding information of references

    """

    def __init__(self, ID, data, log_level=logging.WARNING):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=log_level)
        self.ID = ID

        for key, value in data.items():
            self.__dict__[key] = value

    def dump(self):
        output = ''
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                output += '{:s}: {:s}\n'.format(key, value)
        print(output)
