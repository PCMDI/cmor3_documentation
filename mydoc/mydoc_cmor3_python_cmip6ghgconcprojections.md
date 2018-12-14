---
title: Example Python CMIP6 GHG Concentration Projections
tags: [example]
keywords: example, python, cmip6
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_python/
---

This example shows how to re-write a file which has been produced using some other software, and just needs to be tidied up. In order to run this example, you should have:

* downloaded the starting nc file [TODO: work out a way to include/share this file...]
* downloaded the Python script below
* downloaded the common user input json file given below
* cloned the CMIP6 CMOR tables, ```bash git clone https://github.com/PCMDI/cmip6-cmor-tables.git```
* cloned the CMIP6 input4MIPs CMOR tables, ```bash git clone https://github.com/PCMDI/input4MIPs-cmor-tables.git```
* installed netcdf4 in your CMOR conda environment, `conda install -c conda-forge netcdf4`
* it will probably also be helpful to have the [CMIP6 CMOR tables](https://github.com/PCMDI/cmip6-cmor-tables/tree/master/Tables) or [CMIP6input4MIPS CMOR tables](https://github.com/PCMDI/input4MIPs-cmor-tables) open as you write your own file

### CMOR user input

A marked up version of this table can be found in [CMOR_input_example.json](https://github.com/PCMDI/cmor/blob/master/Test/CMOR_input_example.json).

```json
{
		   "#note": "leave these identifiers alone, except might have to change CMIP6 to input4MIPs...",
           "_control_vocabulary_file": "CMIP6_CV.json",
           "_AXIS_ENTRY_FILE":         "CMIP6_coordinate.json",
           "_FORMULA_VAR_FILE":        "CMIP6_formula_terms.json",
           "_cmip6_option":           "CMIP6",

           "tracking_prefix":        "hdl:21.14100",
           "activity_id":            "input4MIPs",


           "#output":                "Output Path where files are written",
           "outpath":                "CMIP6GHGConcProjections",

           "#experiment_id":         "CMIP6 valid experiment_ids are found in CMIP6_CV.json",
           "experiment_id":          "ScenarioMIP",
           "sub_experiment_id":      "none",
           "sub_experiment":         "none",

           "source_type":            "no idea what this is",
           "parent_mip_era":         "N/A",
           "mip_era":                "CMIP6",
           "calendar":               "365_day",

           "#contact ":              "Not required",
           "contact ":               "malte.meinshausen@unimelb.edu.au",

           "#history":               "not required, supplemented by CMOR",
           "history":                "Processed output from MAGICC7.0.0-alpha",

           "#comment":               "Not required",
           "comment":                "Note: Zonal means for 15-degree lat bands or 0.5-degree lat bands available in _gr0p5x360_ or _gr15x360_ files.",

           "#references":            "Not required",
           "references":             "Malte Meinshausen, Zebedee Nicholls, et al. Future surface greenhouse gas concentrations, GMD Special Issue (please update for final reference) http://www.geosci-model-dev.net/special_issue590.html",

           "grid":                   "global and hemispheric means - area-averages from the original latitudinal 15-degree bands",
           "grid_label":             "gr1-GMNHSH",
           "nominal_resolution":     "10000 km",

           "institution_id":         "UoM",

           "#source_id":              "Model Source",
           "source_id":               "UoM-REMIND-MAGPIE-ssp585-1-2-1",

           "#source":                "source title, first part is source_id",
           "source":                 "UoM-REMIND-MAGPIE-ssp585-1-2-1 GHG Projections",


           "#output_path_template":   "Template for output path directory using tables keys or global attributes. Here we match the input4MIPs DRS",
           "output_path_template":    "<activity_id><mip_era><target_mip><institution_id><source_id><realm><frequency><variable_id><grid_label><version>",
           "output_file_template":    "<variable_id><activity_id><dataset_category><target_mip><source_id><grid_label>",

           "license":                 "GHG concentrations produced by UoM are licensed under a Creative Commons Attribution \\\"Share Alike\\\" 4.0 International License (http://creativecommons.org/licenses/by/4.0/). The data producers and data providers make no warranty, either express or implied, including but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law"

}
```

### Drive script

```python
from os.path import join


import cmor
from netCDF4 import Dataset  # xarray may be a better choice


INPUT_FILE = join(
  "/home",
  "zebedee",
  "Documents",
  "AGCEC",
  "Data",
  "CMIP6GHGConcentrationProjections_1_1_0",
  "mole-fraction-of-so2f2-in-air_input4MIPs_GHGConcentrations_ScenarioMIP_UoM-ssp585-1-1-0_gr1-GMNHSH_2015-2500.nc"
)

cmor.setup(
	inpath='./cmip6-cmor-tables/Tables',  # this has to point to the CMIP6 CMOR tables path
  # outpath is set in the json file read in below
	netcdf_file_action=cmor.CMOR_REPLACE_4
)

cmor.dataset_json("common_user_input_cmip6ghgprojections.json")    

raw_file = Dataset(INPUT_FILE, "r")

# from here down is a bomb site
# here is where you add your axes
itime = cmor.axis(table_entry= 'time',
                  units= "{}".format(raw_file.variables["time"].units),
                  coord_vals= [15,],
                  cell_bounds= [0, 30])
ilat = cmor.axis(table_entry= 'latitude',
                 units= 'degrees_north',
                 coord_vals= [0],
                 cell_bounds= [-1, 1])
ilon = cmor.axis(table_entry= 'longitude',
                 units= 'degrees_east',
                 coord_vals= [90],
                 cell_bounds= [89, 91])

axis_ids = [itime, ilat, ilon]
              
# here we create a variable with appropriate name, units and axes
varid = cmor.variable('mole-fraction-of-so2f2-in-air', 'ppt', axis_ids)

# then we can write the variable along with the data
cmor.write(varid, [273])

# finally we close the file and print where it was saved
outfile = cmor.close(varid, file_name=True)
print("File written to: {}".format(outfile))
cmor.close()
```

### Writing your file

Having done this, and read through the comments in [test_doc.py](https://github.com/PCMDI/cmor/blob/master/Test/test_doc.py), you can then write your file, the output should look as shown below. When writing your own data, each of the warnings tells you where CMOR has updated your input metadata/data, review them carefully to ensure it has done something sensible.

```bash
# if using conda environments, make sure you have activated it
(CMOR) $ python test_generate_file.py
C Traceback:
In function: _CV_checkSourceID
! called from: cmor_setGblAttr
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute "source" with value 
! "PCMDI-test 1.0" will be replaced with value 
! "PCMDI-test 1.0 (1989): 
aerosol: none
atmos: Earth1.0-gettingHotter (360 x 180 longitude/latitude; 50 levels; top level 0.1 mb)
atmosChem: none
land: Earth1.0
landIce: none
ocean: BlueMarble1.0-warming (360 x 180 longitude/latitude; 50 levels; top grid cell 0-10 m)
ocnBgchem: none
seaIce: Declining1.0-warming (360 x 180 longitude/latitude)".
! 
! 
!  See Control Vocabulary JSON file.(./cmip6-cmor-tables/Tables/CMIP6_CV.json)
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_checkExperiment
! called from: cmor_setGblAttr
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute "parent_activity_id" with value 
! "ISMIP6" will be replaced with value "no parent"
! as defined for experiment_id "piControl-withism".
! 
!  See Control Vocabulary JSON file.(./cmip6-cmor-tables/Tables/CMIP6_CV.json)
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_checkExperiment
! called from: cmor_setGblAttr
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute "parent_experiment_id" with value 
! "histALL" will be replaced with value "no parent"
! as defined for experiment_id "piControl-withism".
! 
!  See Control Vocabulary JSON file.(./cmip6-cmor-tables/Tables/CMIP6_CV.json)
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_CompareNoParent
! called from: _CV_checkParentExpID
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute parent_mip_era with value "CMIP6" 
! will be replaced with value "no parent".
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_CompareNoParent
! called from: _CV_checkParentExpID
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute parent_source_id with value "PCMDI-test-1-0" 
! will be replaced with value "no parent".
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_CompareNoParent
! called from: _CV_checkParentExpID
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute parent_time_units with value "days since 1970-01-01" 
! will be replaced with value "no parent".
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_CompareNoParent
! called from: _CV_checkParentExpID
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute parent_variant_label with value "r123i1p33f5" 
! will be replaced with value "no parent".
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_CompareNoParent
! called from: _CV_checkParentExpID
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute branch_method with value "Spin-up documentation" 
! will be replaced with value "no parent".
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!


C Traceback:
In function: _CV_checkParentExpID
! 

!!!!!!!!!!!!!!!!!!!!!!!!!
!
! Warning: Your input attribute branch_time_in_parent 12345.0 
! has been replaced with 0.0 
! 
!
!!!!!!!!!!!!!!!!!!!!!!!!!

File written to: CMIP6/CMIP6/ISMIP6/PCMDI/PCMDI-test-1-0/piControl-withism/r11i1p1f1/Amon/ts/gr/v20181214/ts_Amon_PCMDI-test-1-0_piControl-withism_r11i1p1f1_gr_200001-200001.nc
! ------
! CMOR is now closed.
! ------
! During execution we encountered:
!   9 Warning(s)
!   0 Error(s)
! ------
! Please review them.
! ------
! 
```
