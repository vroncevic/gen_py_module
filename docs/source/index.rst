Generate Python module
----------------------

**gen_py_module** is toolset for generation of Clean Architecture Python modules.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_py_module python checker| |gen_py_module python package| |gen_py_module interface checker| |gen_py_module isp checker| |gen_py_module srp checker| |github issues| |documentation status| |github contributors|

.. |gen_py_module python checker| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python_checker.yml

.. |gen_py_module python package| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_package_checker.yml

.. |gen_py_module interface checker| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_interface_checker.yml

.. |gen_py_module isp checker| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_isp_checker.yml

.. |gen_py_module srp checker| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_srp_checker.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_py_module.svg
   :target: https://github.com/vroncevic/gen_py_module/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_py_module.svg
   :target: https://github.com/vroncevic/gen_py_module/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_py_module/badge/?version=latest
   :target: https://gen_py_module.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
---------------

|gen_py_module python3 build|

.. |gen_py_module python3 build| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_py_module/releases

To install **gen_py_module** type the following

.. code-block:: bash

    tar xvzf gen_py_module-x.y.z.tar.gz
    cd gen_py_module-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_py_module-*-py3-none-any.whl
    rm -f get-pip.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen_py_module

📦 Dependencies
---------------

**gen_py_module** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-----------------

**gen_py_module** is based on OOP and Clean Architecture.

Tool structure

.. code-block:: bash

    gen_py_module/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   ├── module_type.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── bundle.py
         │   │   ├── definition.py
         │   │   ├── executor.py
         │   │   ├── idefinition.py
         │   │   ├── iexecutor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_py_module.cfg
         │   │   ├── gen_py_module.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 46 files

✨ Features
-----------

* Generates Clean Architecture Python 3.12+ modules across 7 supported module types: ``empty``, ``main``, ``class``, ``protocol``, ``dataclass``, ``base``, and ``abc``.
* Strictly adheres to SOLID principles, structural ``Protocol`` interfaces, and inward dependency inversion.
* Robust validation of project bundles, dependencies, and options via ``ats-utilities``.
* High code quality with full static typing, 10.00/10 ``pylint`` score, and 100% unit test coverage.

📊 Code coverage
----------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
--------

Install package

.. code-block:: bash

    pip3 install gen_py_module

Prepare main entry point by downloading ``main.py`` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_py_module/main/main.py

Running tool for creating Python modules across supported ``--type`` templates

.. code-block:: bash

    python3 main.py create --name core_pkg --type empty --output ./demo/empty
    python3 main.py create --name app_entry --type main --output ./demo/main
    python3 main.py create --name core_module --type class --output ./demo/class
    python3 main.py create --name core_module --type protocol --output ./demo/protocol
    python3 main.py create --name core_module --type dataclass --output ./demo/dataclass
    python3 main.py create --name core_module --type base --output ./demo/base
    python3 main.py create --name core_module --type abc --output ./demo/abc

📚 Docs
-------

More documentation and info at

* `gen_py_module.readthedocs.io <https://gen_py_module.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
---------------

`Contributing to gen_py_module <https://github.com/vroncevic/gen_py_module/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
-------------------------

Copyright (C) 2017 - 2026 by `vroncevic.github.io/gen_py_module <https://vroncevic.github.io/gen_py_module>`_

**gen_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.
