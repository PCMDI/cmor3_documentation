---
title: User Input
tags: [cmip6, cmip7]
keywords: cmip6, cmip7, cmor
sidebar: mydoc_sidebar
permalink: /mydoc_cmip6_user_input/
---

### Overview

User input is used by CMOR to set the global attributes in netCDF files, and to set other parameters that control CMOR's behavior. They are passed to CMOR in a JSON file using the [``cmor_dataset_json``](/mydoc_cmor3_api/#cmor_dataset_json).

```python
import cmor

cmor.setup(
    inpath='Tables',
    netcdf_file_action=cmor.CMOR_REPLACE_4
)

cmor.dataset_json("Test/CMOR_input_example.json")  
```

### Controlled Vocabulary Attributes

Attributes are entries used by CMOR to set global attributes in netCDF files. The values of these attributes must be valid according to the controlled vocabulary.

```json
    "source_id":              "ACCESS-CM2",
    "experiment_id":          "1pctCO2",
    "activity_id":            "AerChemMIP",
```

### CMOR parameters

CMOR parameters are entries used by CMOR for setting paths to table files, directory and file templates, and other settings.

#### Controlled Vocabulary and Varialbe Table Paths

* **_controlled_vocabulary_file**: Specify Controlled Vocabulary file name -- default: CMIP6_CV.json
* **_AXIS_ENTRY_FILE**: Specify Coordinate table file(axes) -- default: CMIP6_coordinate.json
* **_FORMULA_VAR_FILE**: Speciry Formula terms table file -- defalut: CMIP6_formula_terms.json

#### String-Valued Index Attributes

* **_use_strings_for_indexes**: Used to allow string values rather than integers for the attributes `realization_index`, `initialization_index`, `physics_index`, and `forcing_index`.

#### CMIP-Specific Checks

* **_cmip6_option**: Enables the validation of attributes for CMIP6, which includes checks related to source and experiment IDs, grid resolution, parent attributes, and subexperiments.
* **_cmip7_option**: Enables the validation of attributes for CMIP7, which are similar to the CMIP6 checks but without the subexperiments. This will also allow for the use of string for index attributes just like `_use_strings_for_indexes`.

#### Output Directory and Filename Templates

Templates are strings composed of attribute names within `<>` that are filled out by their corresponding attribute values of the current dataset used by CMOR.

* **output_path_template**: Template of the output directory for netCDF files. -- default: `<mip_era><activity_id><institution_id><source_id><experiment_id><member_id><table><variable_id><grid_label><version>`

* **output_file_template**: Template of the names of netCDF files. -- default`<variable_id><table><source_id><experiment_id><member_id><grid_label>`

#### Dataset Version

* **version**: Set this to name the \<version\> part of the output path template.  If not set, then CMOR will use the current date as the version in the format of "vYYYYMMDD" (ex. "v20220718"),

### Internal Attributes

Internal attributes are entries with keys that begin with a **_** character that will be added to a CMOR variable's attribute list but will not be written to the netCDF file as global attributes. These can be used for setting values in directory or filename templates.

```json
    "_dev_directory":                  "debug",
```

### Comments

Comments are entries with keys that begin with a **#** character. These will be ignored by CMOR.

```json
    "#note":                  "CMIP6 valid experiment_ids are found in CMIP6_CV.json",
```

### CMIP6 User Input Example

Below is an example of a user input file used for CMIP6. More details on CMIP6 global attributes can be found in [CMIP6_global_attributes_filenames_CVs.doc](https://docs.google.com/document/d/1h0r8RZr_f3-8egBMMh7aqLwy3snpD6_MrDz1q8n5XUk)

```json
{
    "#note":           "explanation of what source_type is goes here",
    "source_type":            "AOGCM ISM AER",
 
    "#note":                  "CMIP6 valid experiment_ids are found in CMIP6_CV.json",
    "experiment_id":          "piControl-withism",
    "activity_id":            "ISMIP6",
    "sub_experiment_id":      "none",
 
    "realization_index":      "3",
    "initialization_index":   "1",
    "physics_index":          "1",
    "forcing_index":          "1",
 
    "#note":                  "Text stored in attribute variant_info (recommended, not required description of run variant)",
    "run_variant":            "3rd realization",
 
    "parent_experiment_id":   "no parent",
    "parent_activity_id":     "no parent",
    "parent_source_id":       "PCMDI-test-1-0",
    "parent_variant_label":   "r3i1p1f1",
 
    "parent_time_units":      "days since 1850-01-01",
    "branch_method":          "standard",
    "branch_time_in_child":   59400.0,
    "branch_time_in_parent":  59400.0,
 
    "#note":                  "institution_id must be registered at https://github.com/WCRP-CMIP/CMIP6_CVs/issues/new ",
    "institution_id":         "PCMDI",
 
    "#note":                  "source_id (model name) must be registered at https://github.com/WCRP-CMIP/CMIP6_CVs/issues/new ",
    "source_id":              "PCMDI-test-1-0",
 
    "calendar":               "360_day",
 
    "grid":                   "native atmosphere regular grid (3x4 latxlon)",
    "grid_label":             "gn",
    "nominal_resolution":     "10000 km",
 
    "license":                 "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law.",
 
    "#output":                "Root directory for output (can be either a relative or full path)",
    "outpath":                "CMIP6",
 
    "#note":                  " **** The following descriptors are optional and may be set to an empty string ",  
 
    "contact ":               "Python Coder (coder@a.b.c.com)",
    "history":                "Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256.",
    "comment":                "",
    "references":             "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html.  The ssp245 simulation is described in Dorkey et al. '(Clim. Dyn., 2003, 323-357.)'",
 
    "#note":                  " **** The following will be obtained from the CV and do not need to be defined here", 
 
    "sub_experiment":         "none",
    "institution":            "",
    "source":                 "PCMDI-test 1.0 (1989)",
 
    "#note":                  " **** The following are set correctly for CMIP6 and should not normally need editing",  
 
    "_controlled_vocabulary_file": "CMIP6_CV.json",
    "_AXIS_ENTRY_FILE":         "CMIP6_coordinate.json",
    "_FORMULA_VAR_FILE":        "CMIP6_formula_terms.json",
    "_cmip6_option":           "CMIP6",
 
    "mip_era":                "CMIP6",
    "parent_mip_era":         "CMIP6",
 
    "tracking_prefix":        "hdl:21.14100",
    "_history_template":       "%s ;rewrote data to be consistent with <activity_id> for variable <variable_id> found in table <table_id>.",
 
    "#output_path_template":   "Template for output path directory using tables keys or global attributes, these should follow the relevant data reference syntax",
    "output_path_template":    "<mip_era><activity_id><institution_id><source_id><experiment_id><_member_id><table><variable_id><grid_label><version>",
    "output_file_template":    "<variable_id><table><source_id><experiment_id><_member_id><grid_label>"
 }
```
