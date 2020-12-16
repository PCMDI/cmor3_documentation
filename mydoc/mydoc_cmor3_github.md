---
title: Source installation
tags: [github]
keywords: github
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_github/
---

### Obtaining the source code and CMIP6 tables

  * Clone the repo from gituhb
    ```bash
    git clone git://github.com/pcmdi/cmor
    cd cmor
    git submodule init
    git submodule update
    ```

### Anaconda System Requirements (if building using anaconda compilers)


#### Getting Anaconda

  * [Anaconda](https://www.continuum.io/)
  * Make sure anaconda is in your PATH (assuming ananconda is installed in ${HOME}/anaconda)

    ```bash
    export PATH=${HOME}/anaconda/bin:${PATH} # for [ba]sh
    ``` 

#### Bypassing firewalls

  * If your institution has a firewall

    ```bash
    conda config --set ssl_verify False
    ```

#### Creating the conda environement with compilers and needed libraries

  * Depending on your os conda brings different compilers

    For Linux
    ```bash
    export CONDA_COMPILERS="gcc_linux-64 gfortran_linux-64"
    ```

    For Mac
    ```bash
    export CONDA_COMPILERS="clang_osx-64 gfortran_osx-64"
    ```

  * Run the following command to build CMOR for your version of Python

    For Python 2.7
   
    ```bash
    conda create -q -n cmor_dev -c cdat/label/nightly -c conda-forge -c cdat six libuuid json-c udunits2 hdf5 libnetcdf openblas netcdf4 numpy openssl lazy-object-proxy cdms2 python=2.7 $CONDA_COMPILERS testsrunner
    ```

    For Python 3.8
   
    ```bash
    conda create -q -n cmor_dev -c cdat/label/nightly -c conda-forge -c cdat six libuuid json-c udunits2 hdf5 libnetcdf openblas netcdf4 numpy openssl lazy-object-proxy cdms2 python=3.8 $CONDA_COMPILERS testsrunner
    ```
  * Activate the conda environment

    ```bash
    source activate cmor_dev
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

### Building CMOR

  * Run

  ```bash
  make install
  ```

### Testing the installation

  Two sets of test can be used
   
  * C and Fortran tests
   ```bash
   make test
   ```
  * Python tests
   ```bash
   export PYTHONPATH=Test/
   python run_tests.py -v2 -H -n1 Test/test_python_CMIP6_CV*.py
   ```
