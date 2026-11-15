# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
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
    Defines unit tests for GenPyModuleBundleKeys class.
'''

from __future__ import annotations

from types import MappingProxyType
from unittest import TestCase, main

from ats_utilities.base.setup.bundle import BaseBundle

from gen_py_module.core.service.iservice import IService
from gen_py_module.core.service.isubprocessor import ISubProcessor
from gen_py_module.infrastructure.cli.icli import ICLI
from gen_py_module.setup.keys import GenPyModuleBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyModuleBundleKeys(TestCase):
    '''
        Defines unit tests for GenPyModuleBundleKeys class.

        It defines:

            :methods:
                | test_dependency_mapping - Verifies get_dependency_to_type immutable mapping.
                | test_option_mapping - Verifies get_option_to_type immutable mapping.
    '''

    def test_dependency_mapping(self) -> None:
        '''
            Verifies get_dependency_to_type immutable mapping.

            :exceptions: None.
        '''
        dep_map: MappingProxyType[str, type] = GenPyModuleBundleKeys.get_dependency_to_type()
        self.assertIsInstance(dep_map, MappingProxyType)
        self.assertIs(dep_map[GenPyModuleBundleKeys.DEPENDENCY_BASE], BaseBundle)
        self.assertIs(dep_map[GenPyModuleBundleKeys.DEPENDENCY_SERVICE], IService)
        self.assertIs(dep_map[GenPyModuleBundleKeys.DEPENDENCY_SUBPROCESSOR], ISubProcessor)
        self.assertIs(dep_map[GenPyModuleBundleKeys.DEPENDENCY_CLI], ICLI)

    def test_option_mapping(self) -> None:
        '''
            Verifies get_option_to_type immutable mapping.

            :exceptions: None.
        '''
        opt_map: MappingProxyType[str, type] = GenPyModuleBundleKeys.get_option_to_type()
        self.assertIsInstance(opt_map, MappingProxyType)
        self.assertIs(opt_map[GenPyModuleBundleKeys.OPTION_INFO_FILE], str)


if __name__ == '__main__':
    main()

