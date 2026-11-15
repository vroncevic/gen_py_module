# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Registry assembling and validating GenPyModuleBundle instances.
'''

from __future__ import annotations

from gen_py_module.setup.bundle import GenPyModuleBundle
from gen_py_module.setup.dep_validator import GenPyModuleBundleDependenciesValidator
from gen_py_module.setup.dependencies import GenPyModuleBundleDependencies
from gen_py_module.setup.keys import GenPyModuleBundleKeys
from gen_py_module.setup.validator import GenPyModuleBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyModuleBundleRegistry:
    '''
        Registry assembling and validating GenPyModuleBundle instances.

        It defines:

            :methods:
                | create_bundle - Creates a validated GenPyModuleBundle from dependencies.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenPyModuleBundleDependencies) -> GenPyModuleBundle:
        '''
            Creates a validated GenPyModuleBundle from dependencies.

            :param dependencies: GenPyModule bundle dependencies.
            :return: Validated GenPyModuleBundle instance.
            :exceptions:
                | ATSValueError: If dependencies or bundle values are missing.
                | ATSTypeError: If dependencies or bundle types are invalid.
        '''
        GenPyModuleBundleDependenciesValidator.validate(dependencies)

        bundle: GenPyModuleBundle = GenPyModuleBundle(
            base=dependencies[GenPyModuleBundleKeys.DEPENDENCY_BASE],
            service=dependencies[GenPyModuleBundleKeys.DEPENDENCY_SERVICE],
            subprocessor=dependencies[GenPyModuleBundleKeys.DEPENDENCY_SUBPROCESSOR],
            cli=dependencies[GenPyModuleBundleKeys.DEPENDENCY_CLI]
        )

        GenPyModuleBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: Registry version string.
            :exceptions: None.
        '''
        return __version__

