---
title: Anaconda installation
tags: [conda]
keywords: conda
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_conda/
---

### All Platforms System Requirements

  * **CMOR 3.7.0 on conda-forge has support for Python 3.7, 3.8, 3.9, and 3.10.**

  * [Anaconda](https://www.continuum.io/)

  * Make sure anaconda is in your PATH (assuming ananconda is installed in ${HOME}/anaconda)

    ```sh
    export PATH=${HOME}/anaconda/bin:${PATH} # for [ba]sh
    setenv PATH ${HOME}/anaconda/bin:${PATH} # for [t]csh
    ``` 

### Bypassing firewalls

  * If your institution has a firewall

    ```
    conda config --set ssl_verify False
    ```

### Installing CMOR and PrePARE

  * Run the following commands
   
    ```bash
    # install cmor
    # ------------------------------------------------
    conda create -n CMOR -c conda-forge cmor
    conda activate CMOR

    # Clone the CMIP6 table to your working directory.
    # ------------------------------------------------
    mkdir CMIP6_work
    cd  CMIP6_work

    # Disable SSL verification (firewall only).
    # -----------------------------------------
    export GIT_SSL_NO_VERIFY=true
    git clone https://github.com/PCMDI/cmip6-cmor-tables.git

    # Note:
    # -----------------------------------------------------------
    # UDUNITS2_XML_PATH is set automatically by activating CMOR. 
    # export UDUNITS2_XML_PATH=${CONDA_PREFIX}/share/udunits/udunits2.xml
    #
    ```

### Testing

  * Run the CMIP6 CV Python tests
   
    ```bash
    # Install cmor with cdms2 and testsrunner
    # ------------------------------------------------
    conda install -n CMOR -c cdat/label/nightly -c cdat -c conda-forge cdms2 testsrunner

    # Clone the CMOR repository to your working directory.
    # ------------------------------------------------
    git clone https://github.com/PCMDI/cmor.git
    cd cmor

    # Update the CMIP6 tables submodule.
    # ------------------------------------------------
    git submodule init
    git submodule update

    # Set PYTHONPATH to the Test directory.
    # ------------------------------------------------
    export PYTHONPATH=Test/

    # Run the tests.
    # ------------------------------------------------
    python run_tests.py -v2 -H -n1 Test/test_python_CMIP6_CV*.py
    ```

  * Run the full test suite for C, Fortran, and Python
    
    Install gcc and gfortran and linking environment variable

    Linux:
    ```bash
    conda install -n CMOR -c conda-forge gcc_linux-64 gfortran_linux-64
    export LDSHARED_FLAGS="-shared -pthread"
    ```
    Mac:
    ```bash
    conda install -n CMOR -c conda-forge clang_osx-64 gfortran_osx-64
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

### Conda environment

  * Create your different CMOR environment with anaconda.

    ```
    conda create -n [YOUR_ENV_NAME_HERE] -c conda-forge cmor
    source activate [YOUR_ENV_NAME_HERE]
    ```

  * [To learn more about conda environments](http://conda.pydata.org/docs/using/envs.html)

### Obtaining Nighlty builds

  * Create a dedicated environment for nightly (in between releases code):
    ```
    conda create -n [YOUR_ENV_NAME_HERE] -c pcmdi/label/nightly -c conda-forge cmor
    source activate [YOUR_ENV_NAME_HERE]
    ```
