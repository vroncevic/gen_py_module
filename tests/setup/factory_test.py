# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Defines unit tests for GenPyModuleBundleFactory class.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_py_module.setup.bundle import GenPyModuleBundle
from gen_py_module.setup.factory import GenPyModuleBundleFactory
from gen_py_module.setup.options import GenPyModuleBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyModuleBundleFactory(TestCase):
    '''
        Defines unit tests for GenPyModuleBundleFactory class.

        It defines:

            :methods:
                | test_create_bundle_default - Verifies default GenPyModuleBundle creation.
                | test_create_bundle_with_options - Verifies GenPyModuleBundle creation with explicit options.
                | test_get_version - Verifies factory version string.
    '''

    def test_create_bundle_default(self) -> None:
        '''
            Verifies default GenPyModuleBundle creation.

            :exceptions: None.
        '''
        bundle: GenPyModuleBundle = GenPyModuleBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenPyModuleBundle)

    def test_create_bundle_with_options(self) -> None:
        '''
            Verifies GenPyModuleBundle creation with explicit options.

            :exceptions: None.
        '''
        bundle: GenPyModuleBundle = GenPyModuleBundleFactory.create_bundle(
            options=GenPyModuleBundleOptions(info_file=GenPyModuleBundleFactory.DEFAULT_INFO_FILE)
        )
        self.assertIsInstance(bundle, GenPyModuleBundle)

    def test_get_version(self) -> None:
        '''
            Verifies factory version string.

            :exceptions: None.
        '''
        self.assertEqual(GenPyModuleBundleFactory.get_version(), '1.5.8')


if __name__ == '__main__':
    main()

