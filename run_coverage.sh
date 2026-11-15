#!/bin/bash
#
# @brief   gen_py_module
# @version 1.5.8
# @date    Sat Nov 14 20:45:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_py_module
pylint gen_py_module > gen_py_module.report
echo "Done"

