# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Defines CLIBundleDependencies TypedDict for CLI bundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TypedDict

from ats_utilities.option.imanager import IOptionManager

from gen_py_module.core.model.project_setup import ProjectSetup
from gen_py_module.core.service.iservice import IService
from gen_py_module.infrastructure.command.bundle import CommandBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleDependencies(TypedDict):
    '''
        Encapsulates dependencies required to construct a CLIBundle.

        It defines:

            :attributes:
                | service - Service for module generation execution.
                | parser - Option manager for command line arguments.
                | commands - Sequence of command definition/executor bundles.
    '''

    service: IService[ProjectSetup, Mapping[str, object]]
    parser: IOptionManager
    commands: Sequence[CommandBundle]

