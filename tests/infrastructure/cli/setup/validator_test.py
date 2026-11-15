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
    Defines unit tests for CLIBundleValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_py_module.core.service.iservice import IService
from gen_py_module.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_module.infrastructure.cli.setup.validator import CLIBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleValidator(TestCase):
    '''
        Defines unit tests for CLIBundleValidator class.

        It defines:

            :methods:
                | test_validate_and_is_valid - Verifies valid and invalid CLIBundle validation.
    '''

    def test_validate_and_is_valid(self) -> None:
        '''
            Verifies valid and invalid CLIBundle validation.

            :exceptions: None.
        '''
        valid_bundle: CLIBundle = CLIBundle(
            service=Mock(spec=IService),
            parser=Mock(spec=IOptionManager),
            commands=()
        )
        CLIBundleValidator.validate(valid_bundle)
        self.assertTrue(CLIBundleValidator.is_valid(valid_bundle))

        invalid_none: object = None
        invalid_field: object = 'bad'
        bad_bundle: CLIBundle = CLIBundle(
            service=invalid_field,  # type: ignore[arg-type]
            parser=Mock(spec=IOptionManager),
            commands=()
        )

        with self.assertRaises(ATSValueError):
            CLIBundleValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            CLIBundleValidator.validate(bad_bundle)

        self.assertFalse(CLIBundleValidator.is_valid(bad_bundle))


if __name__ == '__main__':
    main()

