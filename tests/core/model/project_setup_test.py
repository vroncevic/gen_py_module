# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
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
    Defines unit tests for ProjectSetup domain model.
'''

from __future__ import annotations

from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from gen_py_module.core.model.project_setup import ProjectSetup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestProjectSetup(TestCase):
    '''
        Defines unit tests for ProjectSetup domain model.

        It defines:

            :methods:
                | test_attributes_and_to_dict - Verifies attributes and dictionary serialization.
                | test_immutability - Verifies frozen dataclass immutability.
    '''

    def test_attributes_and_to_dict(self) -> None:
        '''
            Verifies attributes and dictionary serialization.

            :exceptions: None.
        '''
        setup: ProjectSetup = ProjectSetup(
            name='core_mod',
            module_type='class',
            output='./out'
        )
        self.assertEqual(setup.name, 'core_mod')
        self.assertEqual(setup.module_type, 'class')
        self.assertEqual(setup.output, './out')
        self.assertEqual(
            setup.to_dict(),
            {'name': 'core_mod', 'module_type': 'class', 'output': './out'}
        )

    def test_immutability(self) -> None:
        '''
            Verifies frozen dataclass immutability.

            :exceptions: None.
        '''
        setup: ProjectSetup = ProjectSetup(
            name='core_mod',
            module_type='class',
            output='./out'
        )
        with self.assertRaises(FrozenInstanceError):
            setup.name = 'mutated'  # type: ignore[misc]


if __name__ == '__main__':
    main()

