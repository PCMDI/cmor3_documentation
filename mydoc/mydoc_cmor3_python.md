---
title: Example Python
tags: [example]
keywords: example, python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_python/
---
### CMOR user Input


[common_user_input.json](https://github.com/PCMDI/cmor/blob/master/Test/common_user_input.json)

```json
{
           "_control_vocabulary_file": "CMIP6_CV.json",
           "_cmip6_option":           "CMIP6",

           "tracking_prefix":        "hdl:21.14100",
           "activity_id":            "ISMIP6",

           "branch_method":          "standard",
           "branch_time_in_child":   "365.0",

           "#output":                "Output Path where files are written",
           "outpath":                "CMIP6",

           "#experiment_id":         "CMIP6 valid experiment_ids are found in CMIP6_CV.json",
           "experiment_id":          "piControl-withism",
           "sub_experiment_id":      "none",
           "sub_experiment":         "none",

           "source_type":            "AOGCM ISM AER",
           "parent_mip_era":         "N/A",
           "mip_era":                "CMIP6",
           "calendar":               "360_day",
           "branch_time":            "1.34",

           "realization_index":      "11",
           "initialization_index":   "1",
           "physics_index":          "1",
           "forcing_index":          "1",

           "#contact ":              "Not required",
           "contact ":              "Python Coder (coder@a.b.c.com)",

           "#history":               "not required, supplemented by CMOR",
           "history":                "Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256.",

           "#comment":               "Not required",
           "comment":                "Equilibrium reached after 30-year spin-up after which data were output starting with nominal date of January 2030",

           "#references":            "Not required",
           "references":             "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html  2XCO2 simulation described in Dorkey et al. '(Clim. Dyn., 2003, 323-357.)'",

           "grid":                   "gs1x1",
           "grid_label":             "gr",
           "nominal_resolution":     "5 km",

           "institution_id":         "PCMDI",

           "parent_activity_id":     "CMIP",
           "parent_experiment_id":   "histALL",
           "parent_source_id":       "GFDL-CM2-1",
           "parent_variant_label":   "r1i1p1f3",


           "#run_variant":           "Description of run variant (Recommended).",
           "run_variant":            "forcing: black carbon aerosol only",

           "#source_id":              "Model Source",
           "source_id":               "PCMDI-test-1-0",

           "#source":                "source title, first part is source_id",
           "source":                 "PCMDI-test 1.0",


           "#output_path_template":   "Template for output path directory using tables keys or global attributes",
           "output_path_template":    "<activity_id><institution_id><source_id><experiment_id><variant_label><table><variable_id><grid_label><version>",
           "output_file_template":    "<variable_id><table><experiment_id><source_id><variant_label><grid_label>",

           "license":                  "CMIP6 model data produced by PCMDI is licensed under a Creative Commons Attribution \"Share Alike\" 4.0 International License (http://creativecommons.org/licenses/by/4.0/). Use of the data should be acknowledged following guidelines found at https://pcmdi.llnl.gov/home/CMIP6/citation.html. [Permissions beyond the scope of this license may be available at http://pcmdi.llnl.gov.] Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in data files). The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law."

}

```


### Python source code

[test_doc.py](https://github.com/PCMDI/cmor/blob/master/Test/test_doc.py)

[CMIP6_Amon.json](https://github.com/PCMDI/cmor/blob/master/TestTables/CMIP6_Amon.json)

```python
import cmor

cmor.setup(inpath='Tables',netcdf_file_action=cmor.CMOR_REPLACE_4)

cmor.dataset_json("Test/common_user_input.json")
    
table='CMIP6_Amon.json'
cmor.load_table(table)

itime = cmor.axis(table_entry= 'time',
                  units= 'days since 2000-01-01 00:00:00',
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

axis_ids = [itime,ilat,ilon]
              
varid = cmor.variable('ts', 'K', axis_ids)
cmor.write(varid, [273])
outfile=cmor.close(varid, file_name=True)
print "File written: ",outfile
cmor.close()


```
