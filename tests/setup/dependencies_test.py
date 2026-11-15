# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Defines unit tests for GenPyModuleBundleDependencies TypedDict.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_py_module.setup.bundle import GenPyModuleBundle
from gen_py_module.setup.dependencies import GenPyModuleBundleDependencies
from gen_py_module.setup.factory import GenPyModuleBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyModuleBundleDependencies(TestCase):
    '''
        Defines unit tests for GenPyModuleBundleDependencies TypedDict.

        It defines:

            :methods:
                | test_typed_dict_construction - Verifies GenPyModuleBundleDependencies construction.
    '''

    def test_typed_dict_construction(self) -> None:
        '''
            Verifies GenPyModuleBundleDependencies construction.

            :exceptions: None.
        '''
        bundle: GenPyModuleBundle = GenPyModuleBundleFactory.create_bundle()
        deps: GenPyModuleBundleDependencies = GenPyModuleBundleDependencies(
            base=bundle.base,
            service=bundle.service,
            subprocessor=bundle.subprocessor,
            cli=bundle.cli
        )
        self.assertIs(deps['base'], bundle.base)
        self.assertIs(deps['service'], bundle.service)
        self.assertIs(deps['subprocessor'], bundle.subprocessor)
        self.assertIs(deps['cli'], bundle.cli)


if __name__ == '__main__':
    main()

