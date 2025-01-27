---
title: PrePARE
tags: [cmip6]
keywords: cmip6, table, validator, PrePARE
sidebar: mydoc_sidebar
permalink: /mydoc_cmip6_validator/
---

### Note

In order to use PrePARE please follow these instructions.

 * [Anaconda installation](https://cmor.llnl.gov/mydoc_cmor3_conda/)

PrePARE has been created to validate CMIP6 data before publishing files to ESGF.  It may not work properly on CMIP5 files.

### Usage
```
PrePARE  [-h] [-l [CWD]] [--variable VARIABLE] [-v] [--table-path TABLE_PATH] 
         [--max-processes 4] [--all] [--hide-progress] [--no-text-color] 
         [--ignore-dir PYTHON_REGEX] [--include-file PYTHON_REGEX] 
         [--exclude-file PYTHON_REGEX]
         input [input ...]
```
where:

  * __input__ Input CMIP6 netCDF data to validate. If a directory is submitted all netCDF recursively found will be validated independently.

  * __-h__ Display synopsis of the program.

  * __-l, --log__ Logfile directory. Default is the working directory. If not, standard output is used. Only available in multiprocessing mode.
  
  * __--variable__ Specify geophysical variable name. If not variable is deduced from filename. 

  * __-v, --version__ Version of software.

  * __--table-path__ Specify the CMIP6 CMOR tables path (JSON file). If not submitted read the CMIP6_CMOR_TABLES environment variable if it exists. If a directory is submitted table is deduced from filename (default is "./Tables").  
    * [CMIP6 tables](https://github.com/PCMDI/cmip6-cmor-tables/)

  * __--max-processes__  Maximum number of processes to simultaneously validate several files. Set to one seems sequential processing (default). Set to "-1" uses all available resources as returned by "multiprocessing.cpu_count()".
  
  * __--all__ Show all results. Default only shows error(s) (i.e., file(s) not compliant).

  * __--hide-progress__ Do not show the percentage of progress / number of files checked while running PrePARE.

  * __--no-text-color__ Remove text color from output.
  
  * __--ignore-dir__ Filter directories NON-matching the regular expression. Default ignores paths with folder name(s) starting with ".".
  
  * __--exclude-file__ Filter files NON-matching the regular expression. Duplicate the flag to set several filters. Default only exclude hidden files (with names not starting with ".").


### Validation

PrePARE will verify that all attributes in the input file are present and conform to CMIP6 for publication into ESGF.  We also recommand running the python program [cfchecker](https://pypi.python.org/pypi/cfchecker) created by the University of Reading in the UK to confirm that your file is CF-1 compliant.

  * In order to validate all CMIP6 required attributes by PrePARE, a [Controlled Vocabulary file](https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_CV.json) is read by the program where a JSON dictionary called  ["required_global_attributes"](https://github.com/PCMDI/cmip6-cmor-tables/blob/a46dcbf17ec5e11af23dc2d55107f5e52afbcade/Tables/CMIP6_CV.json#L3) points to a list of strings.  Each element of that list corresponds to a global attribute.  
  * PrePARE can also use regular expressions to validate the value of the some global attributes.  Here is an [example](https://github.com/PCMDI/cmip6-cmor-tables/blob/a46dcbf17ec5e11af23dc2d55107f5e52afbcade/Tables/CMIP6_CV.json#L11554-L11555) used for variant_label.

  * Institutions and institution_ids need to be registered into a list.   PrePARE will only accept institutions which have been pre-registered for CMIP6 publication into ESGF.   Click [here](https://github.com/PCMDI/cmip6-cmor-tables/blob/a46dcbf17ec5e11af23dc2d55107f5e52afbcade/Tables/CMIP6_CV.json#L74) for the list of institutions.  If you wish to register your institution write to the [cmor mailing list](mailto:cmor@listserv.llnl.gov).

  * Source and Source ID also need to be registered for CMIP6 publication.  Here is the [list](https://github.com/PCMDI/cmip6-cmor-tables/blob/a46dcbf17ec5e11af23dc2d55107f5e52afbcade/Tables/CMIP6_CV.json#L125) of registered sources.

  * Only experiments found in the Controlled Vocabulary files are accepted for CMIP6 publication. A list of [experiment_ids](https://github.com/PCMDI/cmip6-cmor-tables/blob/a46dcbf17ec5e11af23dc2d55107f5e52afbcade/Tables/CMIP6_CV.json#L3708) have been pre-defined including mandatory attributes.  A warning will be displayed if one experiment attribute is missing or is not properly set by your program.

  * grid and nominal_resolution are mandatory global attributes in CMIP6.  PrePARE will make sure that these attributes are conformed to one of the following syntax:

     |  grid              |  nominal_resolution |
     |--------------------|------------------|
     | gs1x1              |  1x1 degree  |
     | gs1x1 or gn0 to gn9|  1x1 degree  |
     | gs1x1 or gr0 to gr9|  1x1 degree  |
     |  gn0 to gn9        |  "5 km" or   "10 km" or   "25 km" or   "50 km" or  "100 km" or "250 km" or "500 km" or "1000 km" or "2500 km" or "5000 km" or "10000 km" |
     |  gr0 to gr9        |  "5 km" or   "10 km" or   "25 km" or   "50 km" or   "100 km" or "250 km" or "500 km" or "1000 km" or "2500 km" or "5000 km" or "10000 km" |

  
  * PrePARE verifies that the creation date found in the netCDF file is conform to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.

  * The Further Info URL attribute has to be set according to a very specific template.  The PrePARE will use global attribute names found in the netCDF input file and replace the corresponding tag found in a template to rebuild proper CMIP6 link.  If the reconstructed URL does not correspond to the value found in the input file, PrePARE will display an critical error on the screen.
    * Below is the defaul template used for the __furtherinfourl__ attribute.  Each string found between the "<>" characters correspond to a global attribute.  The program will replace these strings with the corresponding global attribute values and add the __"."__ character between each tag.

```
http://furtherinfo.es-doc.org/<mip_era><institution_id><source_id><experiment_id><sub_experiment_id><variant_label>

becomes

http://furtherinfo.es-doc.org/CMIP6.CSIRO-BOM.NICAM.piControl.none.r1i1p1f1" 
```

  * PrePARE will also verify variable attributes necessary for CMIP6 publication.   It validates: long_name, standard_name, units and missing_value according the CMIP6 tables information. 




