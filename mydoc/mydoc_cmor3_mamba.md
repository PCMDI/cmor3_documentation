---
title: Mamba installation
tags: [conda, mamba]
keywords: conda, mamba
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_conda/
---

### Installing Miniforge

  * **CMOR 3.14.0 on conda-forge has support for Python 3.10, 3.11, 3.12, 3.13, and 3.14.**

  * Download the [Miniforge installer](https://conda-forge.org/download/){:target="_blank"} for your system.
    * CMOR is currently only supported for Linux and macOS x86_64, and macOS arm64 (Apple Silicon)

  * Start the install with the following command

    ```bash
    bash Miniforge3-$(uname)-$(uname -m).sh
    ``` 

### Installing CMOR and PrePARE

  * Run the following commands
   
    ```bash
    # install cmor
    # ------------------------------------------------
    mamba create -n CMOR -c conda-forge cmor
    mamba activate CMOR

    # Clone the CMIP6 table to your working directory.
    # ------------------------------------------------
    mkdir CMIP6_work
    cd  CMIP6_work
    git clone https://github.com/PCMDI/cmip6-cmor-tables.git

    # Note:
    # -----------------------------------------------------------
    # UDUNITS2_XML_PATH is set automatically by activating CMOR. 
    # export UDUNITS2_XML_PATH=${CONDA_PREFIX}/share/udunits/udunits2.xml
    #
    ```

### Testing

  * Run the full test suite for C, Fortran, and Python
   
    Clone CMOR code and CMIP6 tables

    ```bash
    # Clone the CMOR repository to your working directory.
    # ------------------------------------------------
    git clone https://github.com/PCMDI/cmor.git
    cd cmor

    # Update the CMIP6 tables submodule.
    # ------------------------------------------------
    git submodule init
    git submodule update
    ```
    
    Install gcc and gfortran and linking environment variable

    Linux:
    ```bash
    mamba install -n CMOR -c conda-forge gcc_linux-64 gfortran_linux-64
    export LDSHARED_FLAGS="-shared -pthread"
    ```
    Mac:
    ```bash
    mamba install -n CMOR -c conda-forge clang_osx-64 gfortran_osx-64
    export LDSHARED_FLAGS=" -bundle -undefined dynamic_lookup"
    ```
    Build and run tests
    ```bash
    # Set prefix for configure step.
    # ------------------------------------------------
    export PREFIX=$(python -c "import sys; print(sys.prefix)")

    # Configure the Makefile.
    # ------------------------------------------------
    ./configure --prefix=$PREFIX --with-python --with-uuid=$PREFIX --with-json-c=$PREFIX --with-udunits2=$PREFIX --with-netcdf=$PREFIX  --enable-verbose-test

    # Run the tests with the Makefile (without rebuilding CMOR).
    # ------------------------------------------------
    make test -o cmor -o python
    ```

### Mamba environment

  * Create your different CMOR environment with mamba.

    ```
    mamba create -n [YOUR_ENV_NAME_HERE] -c conda-forge cmor
    mamba activate [YOUR_ENV_NAME_HERE]
    ```

  * [To learn more about mamba environments](https://mamba.readthedocs.io/en/latest/user_guide/concepts.html){:target="_blank"}

### Obtaining Nighlty builds

  * Create a dedicated environment for nightly (in between releases code):
    ```
    mamba create -n [YOUR_ENV_NAME_HERE] -c pcmdi/label/nightly -c conda-forge cmor
    mamba activate [YOUR_ENV_NAME_HERE]
    ```

  * Create an environment with compilers for development/testing:
    ```
    mamba create -n [YOUR_ENV_NAME_HERE] -c pcmdi/label/nightly -c conda-forge cmor gcc_linux-64 gfortran_linux-64
    mamba activate [YOUR_ENV_NAME_HERE]
    ```
