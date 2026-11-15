#!/bin/bash
#
# @brief   gen_py_module
# @version 1.5.8
# @date    Sat Nov 14 20:45:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_py_module
python3 gates/gates/isp_checker.py gen_py_module
python3 gates/gates/limits_checker.py gen_py_module
python3 gates/gates/srp_checker.py gen_py_module

echo "Done"
