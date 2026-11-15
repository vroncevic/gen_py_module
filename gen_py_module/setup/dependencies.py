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
    Defines GenPyModuleBundleDependencies TypedDict.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import TypedDict

from ats_utilities.base.setup.bundle import BaseBundle

from gen_py_module.core.model.project_setup import ProjectSetup
from gen_py_module.core.service.iservice import IService
from gen_py_module.core.service.isubprocessor import ISubProcessor
from gen_py_module.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyModuleBundleDependencies(TypedDict):
    '''
        Dependencies required to construct a GenPyModuleBundle.

        It defines:

            :attributes:
                | base - Base bundle with framework components.
                | service - Service orchestrating gen_py_module execution.
                | subprocessor - Adapter executing template generation.
                | cli - Command-line interface adapter.
    '''

    base: BaseBundle
    service: IService[ProjectSetup, Mapping[str, object]]
    subprocessor: ISubProcessor[ProjectSetup, Mapping[str, object]]
    cli: ICLI

