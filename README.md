# Generate Python module

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/gen_py_module_logo.png" width="25%">

**gen_py_module** is toolset for generation of Clean Architecture Python modules.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_py_module python checker](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python_checker.yml) [![gen_py_module package checker](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_package_checker.yml) [![gen_py_module interface checker](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_interface_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_interface_checker.yml) [![gen_py_module isp checker](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_isp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_isp_checker.yml) [![gen_py_module srp checker](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_srp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_srp_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_py_module.svg)](https://github.com/vroncevic/gen_py_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_py_module.svg)](https://github.com/vroncevic/gen_py_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/debtux.png)

[![gen_py_module python3 build](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python3_build.yml)

Currently there are four ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_py_module** is located at **[pypi.org](https://pypi.org/project/gen_py_module/)**.

You can install by using pip

```bash
# python3
pip3 install gen_py_module
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_py_module/releases/)** download and extract release archive.

To install **gen_py_module** type the following

```bash
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
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_py_module/releases)** download and extract release archive.

To install **gen_py_module** locate and run setup.py with arguments

```bash
tar xvzf gen_py_module-x.y.z.tar.gz
cd gen_py_module-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies

**gen_py_module** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_py_module** is based on OOP and Clean Architecture.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
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
```
</details>

#### ✨ Features

* Generates Clean Architecture Python 3.12+ modules across 7 supported module types: `empty`, `main`, `class`, `protocol`, `dataclass`, `base`, and `abc`.
* Strictly adheres to SOLID principles, structural `Protocol` interfaces, and inward dependency inversion.
* Robust validation of project bundles, dependencies, and options via `ats-utilities`.
* High code quality with full static typing, 10.00/10 `pylint` score, and 100% unit test coverage.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_py_module/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/core/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/core/model/module_type.py` | 21 | 0 | 100%|
| `gen_py_module/core/model/project_setup.py` | 17 | 0 | 100%|
| `gen_py_module/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/core/service/engine.py` | 34 | 0 | 100%|
| `gen_py_module/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_py_module/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_py_module/engine.py` | 57 | 0 | 100%|
| `gen_py_module/infrastructure/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/infrastructure/cli/engine.py` | 43 | 0 | 100%|
| `gen_py_module/infrastructure/cli/icli.py` | 16 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/bundle.py` | 23 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/dep_validator.py` | 33 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/factory.py` | 29 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/opt_validator.py` | 33 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/options.py` | 17 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/registry.py` | 24 | 0 | 100%|
| `gen_py_module/infrastructure/cli/setup/validator.py` | 35 | 0 | 100%|
| `gen_py_module/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/infrastructure/command/bundle.py` | 19 | 0 | 100%|
| `gen_py_module/infrastructure/command/definition.py` | 31 | 0 | 100%|
| `gen_py_module/infrastructure/command/executor.py` | 32 | 0 | 100%|
| `gen_py_module/infrastructure/command/idefinition.py` | 21 | 0 | 100%|
| `gen_py_module/infrastructure/command/iexecutor.py` | 15 | 0 | 100%|
| `gen_py_module/infrastructure/subprocessor.py` | 64 | 0 | 100%|
| `gen_py_module/setup/__init__.py` | 9 | 0 | 100%|
| `gen_py_module/setup/bundle.py` | 25 | 0 | 100%|
| `gen_py_module/setup/dep_validator.py` | 33 | 0 | 100%|
| `gen_py_module/setup/dependencies.py` | 21 | 0 | 100%|
| `gen_py_module/setup/factory.py` | 45 | 0 | 100%|
| `gen_py_module/setup/keys.py` | 27 | 0 | 100%|
| `gen_py_module/setup/opt_validator.py` | 33 | 0 | 100%|
| `gen_py_module/setup/options.py` | 12 | 0 | 100%|
| `gen_py_module/setup/registry.py` | 24 | 0 | 100%|
| `gen_py_module/setup/validator.py` | 38 | 0 | 100%|
| **Total** | 976 | 0 | 100% |

</details>

### 🛠 Usage

Install package

```bash
pip3 install gen_py_module
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_py_module/main/main.py) or create your own.

```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_py_module/main/main.py
```

Running tool for creating Python modules across supported `--type` templates:

```bash
python3 main.py create --name core_pkg --type empty --output ./demo/empty
python3 main.py create --name app_entry --type main --output ./demo/main
python3 main.py create --name core_module --type class --output ./demo/class
python3 main.py create --name core_module --type protocol --output ./demo/protocol
python3 main.py create --name core_module --type dataclass --output ./demo/dataclass
python3 main.py create --name core_module --type base --output ./demo/base
python3 main.py create --name core_module --type abc --output ./demo/abc
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen_py_module/badge/?version=latest)](https://gen_py_module.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_py_module.readthedocs.io](https://gen_py_module.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_py_module](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2026 by [vroncevic.github.io/gen_py_module](https://vroncevic.github.io/gen_py_module)

**gen_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
