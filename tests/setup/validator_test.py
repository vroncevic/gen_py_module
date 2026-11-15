# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Defines unit tests for GenPyModuleBundleValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_py_module.setup.bundle import GenPyModuleBundle
from gen_py_module.setup.factory import GenPyModuleBundleFactory
from gen_py_module.setup.validator import GenPyModuleBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyModuleBundleValidator(TestCase):
    '''
        Defines unit tests for GenPyModuleBundleValidator class.

        It defines:

            :methods:
                | test_validate_and_is_valid - Verifies valid and invalid GenPyModuleBundle validation.
    '''

    def test_validate_and_is_valid(self) -> None:
        '''
            Verifies valid and invalid GenPyModuleBundle validation.

            :exceptions: None.
        '''
        valid_bundle: GenPyModuleBundle = GenPyModuleBundleFactory.create_bundle()
        GenPyModuleBundleValidator.validate(valid_bundle)
        self.assertTrue(GenPyModuleBundleValidator.is_valid(valid_bundle))

        invalid_none: object = None
        invalid_field: object = 'bad'
        bad_bundle: GenPyModuleBundle = GenPyModuleBundle(
            base=invalid_field,  # type: ignore[arg-type]
            service=valid_bundle.service,
            subprocessor=valid_bundle.subprocessor,
            cli=valid_bundle.cli
        )

        with self.assertRaises(ATSValueError):
            GenPyModuleBundleValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            GenPyModuleBundleValidator.validate(bad_bundle)

        self.assertFalse(GenPyModuleBundleValidator.is_valid(bad_bundle))


if __name__ == '__main__':
    main()

