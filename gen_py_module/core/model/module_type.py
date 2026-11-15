# -*- coding: UTF-8 -*-

'''
Module
    module_type.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_py_module is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_py_module is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines ModuleType enumeration for supported Python module templates.
'''

from __future__ import annotations

from enum import StrEnum

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ModuleType(StrEnum):
    '''
        Defines supported Python module template types.

        It defines:

            :attributes:
                | EMPTY - Empty package initialization module template.
                | MAIN - Executable script module template with main guard.
                | CLASS - Standard domain/adapter class module template.
                | PROTOCOL - Structural runtime-checkable Protocol module template.
                | DATACLASS - Immutable frozen slots dataclass module template.
                | BASE - Base class module template.
                | ABC - Abstract base class module template.
            :methods:
                | values - Returns tuple of all supported module type string values.
    '''

    EMPTY = 'empty'
    MAIN = 'main'
    CLASS = 'class'
    PROTOCOL = 'protocol'
    DATACLASS = 'dataclass'
    BASE = 'base'
    ABC = 'abc'

    @classmethod
    def values(cls) -> tuple[str, ...]:
        '''
            Returns tuple of all supported module type string values.

            :return: Immutable tuple of module type values.
            :exceptions: None.
        '''
        return tuple(member.value for member in cls)

