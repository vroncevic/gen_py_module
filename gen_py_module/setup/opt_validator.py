# -*- coding: UTF-8 -*-

'''
Module
    opt_validator.py
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
    Validator for GenPyModuleBundleOptions.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_py_module.setup.keys import GenPyModuleBundleKeys
from gen_py_module.setup.options import GenPyModuleBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyModuleBundleOptionsValidator:
    '''
        Validator for GenPyModuleBundleOptions.

        It defines:

            :methods:
                | validate - Validates GenPyModule bundle options.
                | is_valid - Checks if GenPyModule bundle options are valid.
    '''

    @classmethod
    def validate(cls, options: GenPyModuleBundleOptions) -> None:
        '''
            Validates GenPyModule bundle options.

            :param options: Bundle options to validate.
            :exceptions:
                | ATSValueError: If options or any required entry is None.
                | ATSTypeError: If options or any entry has invalid type.
        '''
        ctx: str = 'gen_py_module_bundle_options_validator::validate(...)'
        not_none(options, ctx, 'the gen_py_module bundle options must be provided')
        istype(options, Mapping, ctx, 'the gen_py_module bundle options must be a Mapping')

        for attr_name, expected_type in GenPyModuleBundleKeys.get_option_to_type().items():
            label: str = attr_name.replace('_', ' ')
            attribute: object = options.get(attr_name)
            not_none(attribute, ctx, f'the {label} must be provided')
            istype(attribute, expected_type, ctx, f'the {label} must be an instance of {expected_type.__name__}')

    @classmethod
    def is_valid(cls, options: GenPyModuleBundleOptions) -> bool:
        '''
            Checks if GenPyModule bundle options are valid.

            :param options: Bundle options to check.
            :return: True if valid, False otherwise.
            :exceptions: None.
        '''
        try:
            cls.validate(options)
            return True
        except (ATSValueError, ATSTypeError):
            return False

