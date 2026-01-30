---
title: Source installation
tags: [github]
keywords: github
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_github/
---

### Obtaining the CMOR and PrePARE source code and CMIP6 tables

  * Clone the repo from gituhb
    ```bash
    git clone git://github.com/pcmdi/cmor
    cd cmor
    git submodule init
    git submodule update
    ```

### Installing Miniforge

  * **CMOR 3.14.0 has support for Python 3.10, 3.11, 3.12, 3.13, and 3.14.**

  * Download the [Miniforge installer](https://conda-forge.org/download/){:target="_blank"} for your system.
    * CMOR is currently only supported for Linux and macOS x86_64, and macOS arm64 (Apple Silicon)

  * Start the install with the following command

    ```bash
    bash Miniforge3-$(uname)-$(uname -m).sh
    ``` 

#### Creating the mamba environement with compilers and needed libraries

  * Depending on your os mamba brings different compilers

    For Linux
    ```bash
    export CONDA_COMPILERS="gcc_linux-64 gfortran_linux-64"
    ```

    For Intel Mac
    ```bash
    export CONDA_COMPILERS="clang_osx-64 gfortran_osx-64"
    ```

    For Apple Silicon Mac
    ```bash
    export CONDA_COMPILERS="clang_osx-arm64 gfortran_osx-arm64"
    ```

  * Run the following command to create the mamba environment for building CMOR

    ```bash
    mamba create -n cmor_dev -c conda-forge six libuuid json-c udunits2 hdf5 libnetcdf openblas netcdf4 numpy openssl python $CONDA_COMPILERS
    ```

  * Activate the mamba environment

    ```bash
    mamba activate cmor_dev
    ```

### Configuring cmor

  * Depending on your OS linking environment variables are different

    For Linux
    ```bash
    export LDSHARED_FLAGS="-shared -pthread"
    ```

    For Mac
    ```bash
    export LDSHARED_FLAGS=" -bundle -undefined dynamic_lookup"
    ```
  * Set the PREFIX

    Since your environment can use a different name and its location is system dependent use:

    ```bash
    export PREFIX=$(python -c "import sys; print(sys.prefix)")
    ```

  * configure cmor:

    ```bash
    ./configure --prefix=$PREFIX --with-python --with-uuid=$PREFIX --with-json-c=$PREFIX --with-udunits2=$PREFIX --with-netcdf=$PREFIX  --enable-verbose-test
    ```

### Building and installing CMOR and PrePARE

  * Run

    ```bash
    make install
    ```

### Testing the installation

  * Run C, Fortran, and Python tests
    ```bash
    make test
    ```
