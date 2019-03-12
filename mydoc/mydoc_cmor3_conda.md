---
title: Anaconda installation
tags: [conda]
keywords: conda
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_conda/
---

### All Platforms System Requirements

  * [Anaconda](https://www.continuum.io/)
  * Make sure anaconda is in your PATH (this should happen automatically as part of installation)

### Bypassing firewalls

  * If your institution has a firewall

    ```
    conda config --set ssl_verify False
    ```

### Installing
    
  * For installation and environment management, we make the most of the tools offered by the Conda distribution. [More information about conda environments is available here](http://conda.pydata.org/docs/using/envs.html).
  * Run the following command
   
    ```bash
    # create a conda environment and install cmor, it will also install cdms2.
    # ------------------------------------------------------------------------
    conda create -n CMOR -c conda-forge cmor

    # activate your environment
    # -------------------------
    source activate CMOR  # `conda activate CMOR` for users with later versions of conda

    # Clone the CMIP6 table to your working directory.
    # ------------------------------------------------
    # why doesn't this install with CMOR?
    mkdir CMIP6_work
    cd  CMIP6_work

    # If behind a firewall, disable SSL verification
    # ----------------------------------------------
    export GIT_SSL_NO_VERIFY=true

    # Clone the CMIP6 CMOR tables repository
    # --------------------------------------
    git clone https://github.com/PCMDI/cmip6-cmor-tables.git

    # Note:
    # -----------------------------------------------------------
    # UDUNITS2_XML_PATH is set automatically by activating CMOR. 
    # if this isn't the case, you can set it with
    # export UDUNITS2_XML_PATH=${CONDA_PREFIX}/share/udunits/udunits2.xml
    #
    ```

### Obtaining Nightly builds

  * If you want to get code updates more often than just at each release, you can use the builds which are released nightly instead. 
  * Create a dedicated environment for nightly (in between releases code):
    ```
    conda create -n cmor-nightly -c pcmdi/label/nightly -c conda-forge cmor
    source activate cmor-nightly
    ```
