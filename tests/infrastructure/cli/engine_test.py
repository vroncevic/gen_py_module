# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Defines unit tests for CLI inbound adapter class.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSRuntimeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_py_module.core.service.iservice import IService
from gen_py_module.infrastructure.cli.engine import CLI
from gen_py_module.infrastructure.cli.setup.factory import CLIBundleFactory
from gen_py_module.infrastructure.cli.setup.options import CLIBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLI(TestCase):
    '''
        Defines unit tests for CLI inbound adapter class.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates CLIBundle.
                | test_run_success_and_missing_command - Verifies command dispatch and unknown command.
                | test_run_ats_exception_and_state - Verifies ATS exception catch, is_initialized, and str.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates CLIBundle.

            :exceptions: None.
        '''
        invalid_none: object = None
        with self.assertRaises(ATSValueError):
            CLI(bundle=invalid_none)  # type: ignore[arg-type]

    def test_run_success_and_missing_command(self) -> None:
        '''
            Verifies command dispatch and unknown command.

            :exceptions: None.
        '''
        mock_service: Mock = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0, 'stdout': 'ok', 'stderr': ''}

        mock_parser: Mock = Mock(spec=IOptionManager)
        mock_parser.parse_command.return_value = ('create', {'name': 'mod', 'type': 'class', 'output': './out'})

        cli: CLI = CLI(
            CLIBundleFactory.create_bundle(
                options=CLIBundleOptions(service=mock_service, parser=mock_parser)
            )
        )
        ok_res: Mapping[str, object] = cli.run()
        self.assertEqual(ok_res['returncode'], 0)

        mock_parser.parse_command.return_value = ('unknown', {})
        missing_res: Mapping[str, object] = cli.run()
        self.assertEqual(missing_res['returncode'], 1)
        self.assertIn('command not found', str(missing_res['stderr']))

    def test_run_ats_exception_and_state(self) -> None:
        '''
            Verifies ATS exception catch, is_initialized, and str.

            :exceptions: None.
        '''
        mock_service: Mock = Mock(spec=IService)
        mock_parser: Mock = Mock(spec=IOptionManager)
        mock_parser.parse_command.side_effect = ATSRuntimeError('ctx', 'parse error')

        cli: CLI = CLI(
            CLIBundleFactory.create_bundle(
                options=CLIBundleOptions(service=mock_service, parser=mock_parser)
            )
        )
        err_res: Mapping[str, object] = cli.run()
        self.assertEqual(err_res['returncode'], 1)
        self.assertTrue(cli.is_initialized())
        self.assertIsInstance(str(cli), str)


if __name__ == '__main__':
    main()

