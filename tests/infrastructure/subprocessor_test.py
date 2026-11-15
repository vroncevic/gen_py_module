# -*- coding: UTF-8 -*-

'''
Module
    subprocessor_test.py
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
    Defines unit tests for SubProcessor adapter.
'''

from __future__ import annotations

from collections.abc import Mapping
from os import makedirs
from os.path import exists, join
from tempfile import TemporaryDirectory
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.logger.ilogger import ILogger

from gen_py_module.core.model.module_type import ModuleType
from gen_py_module.core.model.project_setup import ProjectSetup
from gen_py_module.infrastructure.subprocessor import SubProcessor
from gen_py_module.setup.bundle import GenPyModuleBundle
from gen_py_module.setup.factory import GenPyModuleBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSubProcessor(TestCase):
    '''
        Defines unit tests for SubProcessor adapter.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates generator.
                | test_run_success_and_nested_logging - Verifies template generation and file logging.
                | test_run_real_templates - Verifies end-to-end generation for all 7 ModuleType variants.
                | test_run_failures - Verifies unsuccessful generation, unsupported type, and exceptions.
                | test_state_and_str - Verifies is_initialized and string representation.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates generator.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ATSValueError):
            SubProcessor(generator=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            SubProcessor(generator=invalid_type)  # type: ignore[arg-type]

    def test_run_success_and_nested_logging(self) -> None:
        '''
            Verifies template generation and file logging.

            :exceptions: None.
        '''
        mock_logger: Mock = Mock(spec=ILogger)
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=mock_logger)
        mock_generator.generate.return_value = True

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)

        with TemporaryDirectory() as tmp_dir:
            with open(join(tmp_dir, 'demo_mod.py'), 'w', encoding='utf-8') as root_file:
                root_file.write('# root\n')

            sub_dir: str = join(tmp_dir, 'pkg')
            makedirs(sub_dir, exist_ok=True)
            with open(join(sub_dir, 'nested.py'), 'w', encoding='utf-8') as nested_file:
                nested_file.write('# nested\n')

            result: Mapping[str, object] = subprocessor.run(
                params=ProjectSetup(name='demo_mod', module_type='class', output=tmp_dir)
            )

        self.assertEqual(result['returncode'], 0)
        self.assertIn('demo_mod', str(result['stdout']))
        self.assertGreaterEqual(mock_logger.write_log.call_count, 3)

    def test_run_real_templates(self) -> None:
        '''
            Verifies end-to-end generation for all 7 ModuleType variants.

            :exceptions: None.
        '''
        bundle: GenPyModuleBundle = GenPyModuleBundleFactory.create_bundle()
        expected_files: dict[str, str] = {
            ModuleType.EMPTY.value: '__init__.py',
            ModuleType.MAIN.value: 'main.py',
            ModuleType.CLASS.value: 'sample_mod.py',
            ModuleType.PROTOCOL.value: 'isample_mod.py',
            ModuleType.DATACLASS.value: 'sample_mod.py',
            ModuleType.BASE.value: 'sample_mod_base.py',
            ModuleType.ABC.value: 'sample_mod_abc.py',
        }

        with TemporaryDirectory() as tmp_dir:
            for mod_type, expected_file in expected_files.items():
                out_dir: str = join(tmp_dir, mod_type)
                result: Mapping[str, object] = bundle.subprocessor.run(
                    params=ProjectSetup(name='sample_mod', module_type=mod_type, output=out_dir)
                )
                self.assertEqual(result['returncode'], 0)
                self.assertTrue(exists(join(out_dir, expected_file)))

    def test_run_failures(self) -> None:
        '''
            Verifies unsuccessful generation, unsupported type, and exceptions.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        mock_generator.generate.return_value = False

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)
        failed: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(name='demo_mod', module_type='class', output='./out')
        )
        self.assertEqual(failed['returncode'], 1)
        self.assertIn('failed to generate demo_mod', str(failed['stderr']))

        unsupported: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(name='demo_mod', module_type='invalid_type', output='./out')
        )
        self.assertEqual(unsupported['returncode'], 1)
        self.assertIn('unsupported module type', str(unsupported['stderr']))

        invalid_none: object = None
        exc_result: Mapping[str, object] = subprocessor.run(params=invalid_none)  # type: ignore[arg-type]
        self.assertEqual(exc_result['returncode'], 1)

    def test_state_and_str(self) -> None:
        '''
            Verifies is_initialized and string representation.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        mock_generator.is_initialized.return_value = True

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)
        self.assertTrue(subprocessor.is_initialized())
        self.assertIsInstance(str(subprocessor), str)


if __name__ == '__main__':
    main()

