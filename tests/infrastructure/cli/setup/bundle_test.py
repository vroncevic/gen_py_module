# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Defines unit tests for CLIBundle dataclass.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.option.imanager import IOptionManager

from gen_py_module.core.service.iservice import IService
from gen_py_module.infrastructure.cli.setup.bundle import CLIBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundle(TestCase):
    '''
        Defines unit tests for CLIBundle dataclass.

        It defines:

            :methods:
                | test_to_dict - Verifies CLIBundle construction and dictionary serialization.
    '''

    def test_to_dict(self) -> None:
        '''
            Verifies CLIBundle construction and dictionary serialization.

            :exceptions: None.
        '''
        mock_service: Mock = Mock(spec=IService)
        mock_parser: Mock = Mock(spec=IOptionManager)
        bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=())
        data: dict[str, object] = bundle.to_dict()
        self.assertIs(data['service'], mock_service)
        self.assertIs(data['parser'], mock_parser)
        self.assertEqual(data['commands'], ())


if __name__ == '__main__':
    main()

