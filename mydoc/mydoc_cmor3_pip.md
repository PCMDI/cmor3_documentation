---
title: pip installation
tags: [python]
keywords: pip, python, wheels
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_pip/
---

### Creating a Python environment

  * Create and activate a virtual environment for CMOR.

    ```bash
    python -m venv cmor_venv
    source cmor_venv/bin/activate
    python -m pip install --upgrade pip
    ```

### Installing CMOR with pip

  * CMOR is not currently published on PyPI.

  * To install a released CMOR wheel with `pip`, download the wheel for your platform and Python version from the [CMOR releases page](https://github.com/PCMDI/cmor/releases){:target="_blank"}, then install it locally.

    ```bash
    pip install /path/to/cmor-<version>-<python tag>-<abi tag>-<platform tag>.whl
    ```

  * Install the nightly Python build of CMOR.

    ```bash
    pip install cmor --extra-index-url https://pcmdi.github.io/cmor
    ```

### Running CMOR's Python tests

  * If you want to run CMOR's Python tests from a source checkout, first install the extra Python packages used by the tests.

    ```bash
    pip install netcdf4 pyfive hdf5plugin
    ```

  * Point the NetCDF library to the bundled zstandard filter plugins.

    ```bash
    export HDF5_PLUGIN_PATH="$(python -c 'import hdf5plugin; print(hdf5plugin.PLUGINS_PATH)')"
    ```

  * Clone the CMOR repository with its table submodule.

    ```bash
    git clone --recursive https://github.com/PCMDI/cmor.git
    cd cmor
    ```

    * If you already cloned the repository without submodules, run:

      ```bash
      git submodule update --init
      ```

  * Run the Python test scripts you want from the repository root. For example:

    ```bash
    python Test/test_doc.py
    python Test/test_cmor_CMIP7.py
    ```

### Notes

  * These instructions install the Python package only. For installing the C and Fortran API, use the [Miniforge/Mamba](/mydoc_cmor3_conda/){:target="_blank"} or [Source (GitHub)](/mydoc_cmor3_github/){:target="_blank"} installation instructions.
