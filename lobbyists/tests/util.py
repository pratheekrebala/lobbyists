#
# util.py - Test utilities.
# Copyright (C) 2008 Drew Hess <dhess@bothan.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

"""Unit test utilities for lobbyists.py."""

import os.path

def testpath(basename):
    return os.path.join('lobbyists', 'tests', 'data', basename)

def sqlscript(basename):
    f = open(os.path.join('lobbyists', basename))
    return ''.join(f.readlines())

def flatten(lst):
    result = list()
    for x in lst:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result