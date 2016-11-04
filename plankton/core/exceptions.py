# -*- coding: utf-8 -*-
# *********************************************************************
# plankton - a library for creating hardware device simulators
# Copyright (C) 2016 European Spallation Source ERIC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# *********************************************************************


class PlanktonException(Exception):
    """
    This exception type is used to distinguish exceptions that are expected
    from unexpected ones. This enables better error handling and more importantly
    better presentation of errors to the users.
    """


class StubAccessException(Exception):
    """
    This exception type is raised when an attribute is accessed on a dummy object instead
    of a real object (see plankton.utils.From).
    """
