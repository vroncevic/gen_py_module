# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Defines unit tests for GenPyModuleBundleDependenciesValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_py_module.setup.bundle import GenPyModuleBundle
from gen_py_module.setup.dep_validator import GenPyModuleBundleDependenciesValidator
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


class TestGenPyModuleBundleDependenciesValidator(TestCase):
    '''
        Defines unit tests for GenPyModuleBundleDependenciesValidator class.

        It defines:

            :methods:
                | test_validate_and_is_valid - Verifies valid and invalid GenPyModule bundle dependencies.
    '''

    def test_validate_and_is_valid(self) -> None:
        '''
            Verifies valid and invalid GenPyModule bundle dependencies.

            :exceptions: None.
        '''
        bundle: GenPyModuleBundle = GenPyModuleBundleFactory.create_bundle()
        valid_deps: GenPyModuleBundleDependencies = GenPyModuleBundleDependencies(
            base=bundle.base,
            service=bundle.service,
            subprocessor=bundle.subprocessor,
            cli=bundle.cli
        )
        GenPyModuleBundleDependenciesValidator.validate(valid_deps)
        self.assertTrue(GenPyModuleBundleDependenciesValidator.is_valid(valid_deps))

        invalid_none: object = None
        invalid_entry: object = {
            'base': 'bad',
            'service': bundle.service,
            'subprocessor': bundle.subprocessor,
            'cli': bundle.cli
        }

        with self.assertRaises(ATSValueError):
            GenPyModuleBundleDependenciesValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            GenPyModuleBundleDependenciesValidator.validate(invalid_entry)  # type: ignore[arg-type]

        self.assertFalse(GenPyModuleBundleDependenciesValidator.is_valid(invalid_none))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()

