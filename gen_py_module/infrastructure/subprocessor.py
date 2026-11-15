# -*- coding: UTF-8 -*-

'''
Module
    subprocessor.py
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
    Defines SubProcessor adapter implementing ISubProcessor structurally.
'''

from __future__ import annotations

from collections.abc import Mapping
from datetime import date
from logging import INFO
from os import walk
from os.path import dirname, realpath, relpath
from typing import ClassVar

from ats_utilities.exceptions import ATSValueError
from ats_utilities.generation.data import GeneratorData
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_py_module.core.model.module_type import ModuleType
from gen_py_module.core.model.project_setup import ProjectSetup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SubProcessor:
    '''
        Defines class SubProcessor implementing ISubProcessor contract structurally.
        Adapter that generates Python module files from packaged templates.

        It defines:

            :attributes:
                | SCHEME_PATH - Relative path to scheme configuration JSON file.
                | TEMPLATES_PATH - Relative path to templates archive file.
                | _generator - Generator manager used to render module files.
                | _logger - Logger used to log operational messages.
            :methods:
                | __init__ - Initializes SubProcessor adapter.
                | run - Executes template generation for ProjectSetup.
                | is_initialized - Checks if the subprocessor is initialized.
                | __str__ - Returns SubProcessor string representation.
    '''

    SCHEME_PATH: ClassVar[str] = 'config/scheme.json'
    TEMPLATES_PATH: ClassVar[str] = 'config/templates.tgz'

    _generator: IGeneratorManager
    _logger: ILogger

    def __init__(self, generator: IGeneratorManager) -> None:
        '''
            Initializes SubProcessor adapter.

            :param generator: Generator manager instance.
            :exceptions:
                | ATSValueError: If generator is None.
                | ATSTypeError: If generator does not satisfy IGeneratorManager.
        '''
        ctx: str = 'subprocessor::init(...)'
        msg_generator_none: str = 'the generator must be provided'
        msg_generator_istype: str = f'the generator must be an instance of {IGeneratorManager.__name__}'

        not_none(generator, ctx, msg_generator_none)
        istype(generator, IGeneratorManager, ctx, msg_generator_istype)

        self._generator = generator
        self._logger = generator.get_context().logger

    def run(self, *, params: ProjectSetup) -> Mapping[str, object]:
        '''
            Executes template generation for ProjectSetup.

            :param params: ProjectSetup containing module name, type, and output directory.
            :return: Mapping with returncode, stdout, and stderr messages.
            :exceptions: None.
        '''
        module_name: str = 'unknown'

        try:
            ctx: str = 'subprocessor::run(...)'
            not_none(params, ctx, 'the params must be provided')
            istype(params, ProjectSetup, ctx, f'the params must be an instance of {ProjectSetup.__name__}')

            module_name = params.name

            if params.module_type not in ModuleType.values():
                raise ATSValueError(ctx, f'unsupported module type {params.module_type}')

            current_dir: str = dirname(realpath(__file__))
            pascal_name: str = ''.join(word.capitalize() for word in module_name.replace('-', '_').split('_'))

            success: bool = self._generator.generate(
                data=GeneratorData(
                    archive_path=f'{current_dir}/{self.TEMPLATES_PATH}',
                    target_dir=params.output,
                    template_key=params.module_type,
                    scheme=f'{current_dir}/{self.SCHEME_PATH}',
                    template_values={
                        'project_name': module_name,
                        'protocol_name': f'i{module_name}',
                        'MOD': module_name,
                        'MODCL': pascal_name,
                        'PRO': module_name,
                        'YEAR': str(date.today().year),
                    }
                )
            )

            if success:
                self._logger.write_log(INFO, '    Generated files:')

                for root, _, files in walk(params.output):
                    for file in files:
                        rel_dir: str = relpath(root, params.output)

                        if rel_dir == '.':
                            self._logger.write_log(INFO, f'      {file}')
                        else:
                            self._logger.write_log(INFO, f'      {rel_dir}/{file}')

            return {
                'returncode': 0 if success else 1,
                'stdout': f'module {module_name} successfully generated.' if success else '',
                'stderr': f'failed to generate {module_name} module.' if not success else ''
            }

        except Exception as exc:
            return {'returncode': 1, 'stdout': '', 'stderr': f'failed to generate {module_name} module {exc}'}

    def is_initialized(self) -> bool:
        '''
            Checks if the subprocessor is initialized.

            :return: True if the subprocessor is initialized, False otherwise.
            :exceptions: None.
        '''
        return self._generator.is_initialized()

    def __str__(self) -> str:
        '''
            Returns SubProcessor string representation.

            :return: String representation of SubProcessor.
            :exceptions: None.
        '''
        return to_str(self)
