---
title: Getting started overview
tags: [getting_started]
sidebar: mydoc_sidebar
type: homepage
---

## Design Considerations and Overview

This document describes Version 3 of a software library called "Climate Model Output Rewriter" (CMOR3)[\[1\]](#1), written in C with access also provided via Fortran 90 and through Python[\[2\]](#2).  CMOR is used to produce CF-compliant[\[3\]](#3) netCDF[\[4\]](#4) files.  The structure of the files created by CMOR and the metadata they contain fulfill the requirements of many of the climate community's standard model experiments (which are referred to here as "MIPs"[\[5\]](#5) and include, for example, AMIP, PMIP, APE, and IPCC [DN1] scenario runs).  
 
CMOR was not designed to serve as an all-purpose writer of CF-compliant netCDF files, but simply to reduce the effort required to prepare and manage MIP model output.  Although MIPs encourage systematic analysis of results across models, this is only easy to do if the model output is written in a common format with files structured similarly and with sufficient metadata uniformly stored according to a common standard.  Individual modeling groups store their data in different ways, but if a group can read its own data, then it should easily be able to transform the data, using CMOR, into the common format required by the MIPs.   The adoption of CMOR as a standard code for exchanging climate data will facilitate participation in MIPs because after learning how to satisfy the output requirements of one MIP, it will be easy to prepare output for other MIPs.
 
CMOR output has the following characteristics:

* Each file contains a single primary output variable (along with coordinate/grid variables, attributes and other metadata) from a single model and a single simulation (i.e., from a single ensemble member of a single climate experiment).  This method of structuring model output best serves the needs of most researchers who are typically interested in only a few of the many variables in the MIP databases.  Data requests can be satisfied by simply sending the appropriate file(s) without first extracting the individual field(s) of interest.

* There is flexibility in specifying how many time slices (samples) are stored in a single file. A single file can contain all the time-samples for a given variable and climate experiment, or the samples can be distributed in a sequence of files.

* Much of the metadata written to the output files is defined in MIP-specific tables of information, which in this document are referred to simply as "MIP tables".  These tables are JSON files that can be read by CMOR and are typically made available from MIP web sites.  Because these tables contain much of the metadata that is useful in the MIP context, they are the key to reducing the programming burden imposed on the individual users contributing data to a MIP.  Additional tables can be created as new MIPs are born.

* For metadata, different MIPs may have different requirements, but these are accommodated by CMOR, within the constraints of the CF convention and as specified in the MIP tables (e.g. [CMIP6 MIP tables](https://github.com/PCMDI/cmip6-cmor-tables)).

CMOR relies on NetCDF4 [See unidata web page](http://www.unidata.ucar.edu/software/netcdf) to write the output files and can take advantage of its compression and chunking capabilities.  CMOR3 outputs NetCDF4 files by default.  For CMIP6, the NetCDF4/NC_CLASSIC_Model mode is used.  As of CMOR 3.9, there is now support for zstandard compression and [lossy compression via quantization](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.12/cf-conventions.html#lossy-compression-via-quantization).  More on quantization in NetCDF4 [here](https://docs.unidata.ucar.edu/netcdf-c/4.9.2/md__media_psf_Home_Desktop_netcdf_releases_v4_9_2_release_netcdf_c_docs_quantize.html).

* CMOR also must be linked against the udunits2 library [see http://www.unidata.ucar.edu/software/udunits/](http://www.unidata.ucar.edu/software/udunits/), which enables CMOR to check that the units attribute is correct[\[6\]](#6). Finally CMOR3 must also be linked against the uuid library [see http://www.ossp.org/pkg/lib/uuid](http://www.ossp.org/pkg/lib/uuid) in order to produce a unique tracking number for each file.   
 
Although the CMOR output adheres to a fairly rigid structure, there is considerable flexibility allowed in the design of codes that write data through the CMOR functions.  Depending on how the source data are stored, one might want to structure a code to read and rewrite the data through CMOR in several different ways.  Consider, for example, a case where data are originally stored in "history" files that contain many different fields, but a single time sample.   If one were to process several different fields through CMOR and one wanted to include many time samples per file, then it would usually be more efficient to read all the fields from the single input file at the same time, and then distribute them to the appropriate CMOR output files, rather than to process all the time-samples for a single field and then move on to the next field.  If, however, the original data were stored already by field (i.e., one variable per file), then it would make more sense to simply loop through the fields, one at a time.  The user is free to structure the conversion program in either of these ways (among others).

The following input files are typically needed by CMOR:

* The "User Input File" (e.g., CMIP6_input_example.json), which provides user-supplied metadata and configuration directives.
* A "controlled vocabulary file" (e.g., "CMIP6_CV.json), which concatenates into a single file most of the CMIP6 controlled vocabularies archived at https://github.com/WCRP-CMIP/CMIP6_CVs . This file is updated frequently as additional models and institutions register to participate in CMIP6.
* A "CMOR Table" (e.g., CMIP6_Amon.json), which provides for each variable that might be written by CMOR much of the required metatdata. It also provides additional information that CMOR uses to correctly write the data and to enable certain QC checks.
* A "Vertical Coordinate Formula Terms Table" (e.g., CMIP6_formula_terms.json)
* A "Coordinates Table" (e.g., CMIP6_coordinate.json) CMIP6
* CMIP6_grids.json supplements the Coordinates Table with axis information that is sometimes needed in the treatment of unstructured grids.

The files used by CMOR for CMIP6 are archived in [https://github.com/PCMDI/cmip6-cmor-tables/tree/master/Tables](https://github.com/PCMDI/cmip6-cmor-tables/tree/master/Tables), and all but the CMIP6_input_example.json file must not be modifed by the user. The CMIP6_input_example.json file must be edited to accurately reflect the output being written by the user (but do not modify the lines of text appearing after the comment line, "#note_CV": " **** The following will be obtained from the CV and do not need to be defined here"). Note that the CMIP6_CV.json file found in [https://github.com/PCMDI/cmip6-cmor-tables/tree/master/Tables](https://github.com/PCMDI/cmip6-cmor-tables/tree/master/Tables) is updated whenever new models and institutions are registered to participate in CMIP6.
 
Converting data with CMOR typically involves the following steps (with the CMOR function names given in parentheses):

* Initialize CMOR and specify where output will be written and how error messages will be handled (cmor_setup).
* Provide information directing where output should be placed and identifying the data source, project name, experiment, etc. (cmor_dataset_json).  User need to provide a User Input CMOR file to define each attribute.
* Set any additional "dataset" (i.e. global) attributes (cmor_set_cur_dataset function).  Note that all CMIP6 attributes can also be defined in the CMOR input user JSON file (cmor_dataset_json).
* Define the axes (i.e., the coordinate values) associated with each of the dimensions of the data to be written and obtain "handles", to be used in the next step, which uniquely identify the axes (cmor_axis).  
* In the case of non-Cartesian longitude-latitude grids or for "station data", define the grid and its mapping parameters (cmor_grid and cmor_set_grid_mapping)
* Define the variables to be written by CMOR, indicate which axes are associated with each variable, and obtain "handles", to be used in the next step, which uniquely identify each variable (cmor_variable).  For each variable defined, this function fills internal table entries containing file attributes passed by the user or obtained from a MIP table, along with coordinate variables and other related information. Thus, nearly all of the file's metadata is collected during this step.
* Write an array of data that includes one or more time samples for a defined variable (cmor_write).  This step will typically be repeated to output additional variables or to append additional time samples of data.
* Close one or all files created by CMOR (cmor_close)
 
There is an additional function (cmor_zfactor), which enables one to define metadata associated with dimensionless vertical coordinates.
 
CMOR was designed to reduce the effort required of those contributing data to various MIPs.  An important aim was to minimize any transformations that the user would have to perform on their original data structures to meet the MIP requirements.  Toward this end, the code allows the following flexibility (with the MIP requirements obtained by CMOR from the appropriate MIP table and automatically applied):

* The input data can be structured with dimensions in any order and with coordinate values either increasing or decreasing monotonically; CMOR will rearrange them to meet the MIP's requirements before writing out the data.

* The input data and coordinate values can be provided in an array declared to be whatever "type" is convenient for the user (e.g., in the case of coordinate data, the user might pass type "real" values (32-bit floating-point numbers on most platforms) even though the output will be written type double (64-bit IEEE floating-point); CMOR will transform the data to the required type before writing.

* The input data can be provided in units different from what is required by a MIP.  If those units can be transformed to the correct units using the udunits (version 2) software (see udunits)[http://www.unidata.ucar.edu/software/udunits/], then CMOR performs the transformation before writing the data.  Otherwise, CMOR will return an error. Time units are handled via the built-in cdtime interface [\[7\]](#7).

* So-called "scalar dimensions" (sometimes referred to as "singleton dimensions") are automatically inserted by CMOR. Thus, for example, the user can provide surface air temperature (at 2 meters) as a function of longitude, latitude, and time, and CMOR adds as a "coordinate" attribute the "height" dimension, consistent with the metadata requirements of CF.  If the model output does not conform to the MIP requirements (e.g., carries temperature at 1.5 m instead of 2 m), then the user can override the MIP table specifications.

The code does not, however, include a capability to interpolate data, either in the vertical or horizontally.  If data originally stored on model levels, is supposed to be stored on standard pressure levels, according to MIP specifications, then the user must interpolate before passing the data to CMOR. 
 
The output resulting from CMOR is "self-describing" and includes metadata summarized below, organized by attribute type (global, coordinate, or variable attributes) and by its source (specified by the user or in a MIP table, or generated by CMOR).
 

*Global attributes typically provided by the MIP table or generated by CMOR:*
 
* *title*, identification of the project, experiment, and table.
* *Conventions*, ('CF-1.4')
* *history*, any user-provided history along with a "timestamp" generated by CMOR and a statement that the data conform to both the CF standards and those of a particular MIP.
* *activity_id*, scientific project that inspired this simulation (e.g., CMIP6)
* *table_id*, MIP table used to define variable.
* *data_specs_version* Base on the latest CMIP6-Datarequest latest database version.
* *mip_era*,  define what cycle of CMIP dictates the experiment and data specificiation.
* *experiment*, a long name title for the experiment.
* *realm(s)* to which the variable belongs (e.g., ocean, land, atmosphere, etc.).
* *tracking_id*,  a unique identification string generated by uuid, which is useful at least within the ESG distributed data archive.
* *cmor_version*, version of the library used to generate the files.
* *frequency*, the approximate time-sampling interval for a time-series of data.
* *creation_date*, the date and time (UTZ) that the file was created.
* *product*, a descriptive string that distinguishes among various model data products.
 
*Global attributes typically provided by the user in a call to a CMOR function:*
 
* *institution*, identifying the modeling center contributing the output.
* *institute_id*, a shorter identifying name of the modeling center (which would be appropriate for labeling plots in which results from many models might appear).
* *source*, identifying the model version that generated the output.
* *contact*, providing the name and email of someone responsible for the data
* *source_id*, an acronym that identifies the model used to generate the output.
* *experiment_id*, a short name for the experiment.
* *history*, providing an "audit trail" for the data, which will be supplemented with CMOR-generated information described above.
* *references*, typically containing documentation of the model and the model simulation.
* *comment*, typically including initialization and spin-up information for the simulation.
* *realization_index*, an integer distinguishing among simulations that differ only from different equally reasonable initial conditions.  This number should be greater than or equal to 1. 
* *initialization_index*, an integer distinguishing among simulations that differ only in the method of initialization.  This number should be greater than or equal to 1.
* *physics_index*, an integer indicating which of several closely related physics versions of a model produced the simulation.
* *parent_experiment_id*, a string indicating which experiment this branches from. For CMIP6 this should match the short name of the parent experiment id.
* *parent_experiment_rip*, a string indicating <span style="color:red">which member of an ensemble of parent experiment runs this simulation branched from.</span>
* *branch_time*, time in parent experiment when this simulation started (in the units of the parent experiment).
 
Note: additional global attributes can be added by the user via the cmor_set_cur_dataset_attribute function (see below).
 
*Coordinate attributes typically provided by a MIP table or generated by CMOR:*
 
* *standard_name*, as defined in the CF standard name table.
* *units*, specifying the units for the coordinate variable.
* *axis*, indicating whether axis is of type x, y, z, t, or none of these.
* *bounds*, (when appropriate) indicating where the cell bounds are stored.
* *positive*, (when appropriate) indicating whether a vertical coordinate increases upward or downward.
* *formula_terms*, (when appropriate) providing information needed to transform from a dimensionless vertical coordinate to the actual location (e.g., from sigma-level to pressure).
 
* Coordinate or grid mapping attributes typically provided by the user in a call to a CMOR function:*
 
* *calendar*, (when appropriate) indicating the calendar type assumed by the model.
* *grid_mapping_name* and the names of various mapping parameters, when necessary to describe grids other than lat-lon.  See CF conventions at: [http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html#appendix-grid-mappings](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html#appendix-grid-mappings)
 
* Variable attributes typically provided by a MIP table or generated by CMOR:*
 
* *standard_name* as defined in the CF standard name table.
* *units*, specifying the units for the variable.
* *long_name*, describing the variable and useful as a title on plots.
* *missing_value* and *_FillValue*, specifying how missing data will be identified.
* *cell_methods*, (when appropriate) typically providing information concerning calculation of means or climatologies, which may be supplemented by information provided by the user.
* *cell_measures*, when appropriate, indicates the names of the variables containing cell areas and volumes.
* *comment*, providing clarifying information concerning the variable (e.g., whether precipitation includes both liquid and solid forms of precipitation).
* *history*, indicating what CMOR has done to the user supplied data (e.g., transforming its units or rearranging its order to be consistent with the MIP requirements)
* *coordinates*, (when appropriate) supplying either scalar (singleton) dimension information or the name of the labels containing names of geographical regions.
* *flag_values* and *flag_meanings*
* *modeling_realm*, providing the realm associated to the variable (ocean, land, aerosol, SeaIce, LandIce, ...)
 
*Variable attributes typically provided by the user in a call to a CMOR function:*
 
* *grid_mappingi*
* *original_name*, containing the name of the variable as it is known at the user's home institution.i*
* *original_units*, the units of the data passed to CMOR.
* *history*, (when appropriate) information concerning processing of the variable prior to sending it to CMOR.  (This information may be supplemented by further history information generated by CMOR.)
* *comment*, (when appropriate) providing miscellaneous information concerning the variable, which will supplement any comment contained in the MIP table.
 
As is evident from the above summary of metadata, a substantial fraction of the information is defined in the MIP tables, which explains why writing MIP output through CMOR is much easier than writing data without the help of the MIP tables.   Besides the attribute information, the MIP tables also include information that controls the structure of the output and allows CMOR to apply some rudimentary quality assurance checks.  Among this ancillary information in the MIP tables is the following:
 
* The direction each coordinate should be stored when it is output (i.e., either in order of increasing or decreasing values).  The user need not be concerned with this since, if necessary, CMOR will reorder the coordinate values and the data.
* The acceptable values for coordinates (e.g., for a pressure coordinate axis, for example, perhaps the WCRP standard pressure levels).
* The acceptable values for various arguments passed to CMOR functions (e.g., acceptable calendars, experiment i.d.'s, etc.)
* The "type" of each output array (whether real, double precision, or integer).  The user need not be concerned with this since, if necessary, CMOR will convert the data to the specified type.
* The order of the dimensions for output arrays. The user need not be concerned with this since, if necessary, CMOR will reorder the data consistent with the specified dimension order.
* The normally applied values for "scalar dimensions" (i.e., "singleton dimensions").
* The range of acceptable values for output arrays.
* The acceptable range for the spatial mean of the absolute value of all elements in output arrays.
* The minimal global attributes required.

<span id='1'>[1] CMOR is pronounced "C-more", which suggests that CMOR should enable a wide community of scientists to "see more" climate data produced by modeling centers around the world.  CMOR also reminds us of Ecinae Corianus, the revered ancient Greek scholar, known to his friends as "Seymour".  Seymour spent much of his life translating into Greek nearly all the existing climate data, which had originally been recorded on largely inscrutable hieroglyphic and cuneiform tablets.  His resulting volumes, organized in a uniform fashion and in a language readable by the common scientists of the day, provided the basis for much subsequent scholarly research.  Ecinae Corianus was later indirectly honored by early inhabitants of the British Isles who reversed the spelling of his name and used the resulting string of letters, grouped differently, to form new words referring to the major elements of climate.</span>

<span id="2">[2] CMOR1 was written in Fortran 90 with access also provided through Python.</span>

<span id="3">[3] See http://www.cgd.ucar.edu/cms/eaton/cf-metadata </span>

<span id="4">[4] See http://my.unidata.ucar.edu/content/software/netcdf/</span>

<span id="5">[5] "MIP" is an acronym for "model intercomparison project".</span>

<span id="6">[6] CMOR1 was linked to an earlier version of the netCDF library and udunits was optional.</span>

<span id="7">[7] Cdtime is now built into CMOR. Therefore linking against cdms is no longer necessary.</span>


---

## Preliminary notes

In the following, all arguments should be passed using keywords (to improve readability and flexibility in ordering the arguments).  Those arguments appearing below that are followed by an equal sign may be optional and, if not passed by the user, are assigned the default value that follows the equal sign.  The information in a MIP-specific input table determines whether or not an argument shown in brackets is optional or required, and the table provides MIP-specific default values for some parameters.  All arguments not in brackets and not followed by an equal sign are always required.

Three versions of each function are shown below.  The first one is for <span style="color:green">Fortran (green text)</span> the second for <span style="color:blue">C (blue text)</span>, and the third for <span style="color:coral">Python (orange text)</span>.   In the following, text that applies to only one of the coding languages appears in the appropriate color.

Some of the arguments passed to CMOR (e.g., names of variables and axes are only unambiguously defined in the context of a specific CMOR table, and in the Fortran version of the functions this is specified by one of the function arguments, whereas in the C and Python versions it is specified through a call to cmor_load_table and cmor_set_table.

All functions are type “integer”.  If a function results in an error, <span style="color:coral">an “exception” will be raised in the Python version (otherwise None will be returned)</span>, and in either the Fortran or C versions, the error will be indicated by the integer returned by the function itself.  <span style="color:blue">In C an integer other than 0 will be returned,</span> <span style="color:green"> and in Fortran errors will result in a negative integer (except in the case of cmor_grid, which will return a positive integer).</span>


If no error is encountered, some functions will return information needed by the user in subsequent calls to CMOR.  In almost all cases this information is indicated by the value of a single integer that in Fortran and Python is returned as the value of the function itself, whereas in C it is returned as an output argument).  There are two cases in the Fortran version of CMOR, however, when a string argument may be set by CMOR (cmor_close and cmor_create_output_path).  These are the only cases when the value of any of the Fortran function’s arguments might be modified by CMOR.     

