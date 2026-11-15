#!/bin/bash
#
# @brief   gen_py_module
# @version 1.5.8
# @date    Sat Nov 14 20:45:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "core_pkg" --type "empty" --output "./demo/empty"
python3 main.py create --name "app_entry" --type "main" --output "./demo/main"
python3 main.py create --name "core_module" --type "class" --output "./demo/class"
python3 main.py create --name "core_module" --type "protocol" --output "./demo/protocol"
python3 main.py create --name "core_module" --type "dataclass" --output "./demo/dataclass"
python3 main.py create --name "core_module" --type "base" --output "./demo/base"
python3 main.py create --name "core_module" --type "abc" --output "./demo/abc"

