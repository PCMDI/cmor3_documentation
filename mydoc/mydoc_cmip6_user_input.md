---
title: CMIP6 User Input
tags: [cmip6]
keywords: cmip6, cmor
sidebar: mydoc_sidebar
permalink: /mydoc_cmip6_user_input/
---

### Notes

1. Keys beginning with character **_** will not be written in netCDF file as attribute.  They can be use for template filename of template path.
1. Keys beginning with character **#** can be used as comment.

### CMIP6 CMOR User Input

[CMIP6_global_attributes_filenames_CVs.doc](https://docs.google.com/document/d/1h0r8RZr_f3-8egBMMh7aqLwy3snpD6_MrDz1q8n5XUk)

* *_controlled_vocabulary_file*:"Specify Controlled Vocabulary file name -- default: CMIP6_CV.json"

* *_AXIS_ENTRY_FILE*:        "Specify Coordinate table file(axes) -- default: CMIP6_coordinate.json"

* *_FORMULA_VAR_FILE*:       "Speciry Formula terms table file -- defalut: CMIP6_formula_terms.json"

* *_cmip6_option*:           "used to trigger validation for CMIP6 only."

* *activity_id*:             "Specify an activity PMIP, GeoMIP"

* *output*:                  "Output Path where files are written -- must be created by the user."

* *experiment_id*:           "Correspond to id found in \"_controlled_vocabulary_file\""

* *source_type*:             "type of model used",

* *sub_experiment*:          "description of sub-experiment",

* *sub_experiment_id*:       "none",

* *parent_sub_experiment_id*:     

* *parent_mip_era*:              

* *mip_era*:                    

* *institution*:     
            
* *source*:         

* *calendar*:     

* *realization_index*:      

* *initialization_index*:  

* *physics_index*:       

* *forcing_index*:        

* *contact *:           

* *history*:          

* *comment*:        

* *references*:   

* *institution_id*:      

* *model_id*:          

* *forcing*:         

* *parent_variant_label*:  

* *parent_experiment_id*:

* *branch_time*:       


* *parent_activity_id*: 

* *parent_source_id*:   

* *branch_method*:        
* *branch_time_in_child*: 
* *branch_time_in_parent*:
* *branch_time_units_in_parent*:


* *further_info_url*:       "http://furtherinfo.es-doc.org/\<mip_era\>/\<institution_id\>\<source_id\>\<experiment_id\>\<sub_experiment_id\>\<variant_label\>",
* *grid*:                  
* *grid_label*:           
* *nominal_resolution*:     
* *run_variant*:      
* *source_id*:       

* *output_path_template*:    "\<mip_era\>\<activity_id\>\<institution_id\>\<source_id\>\<experiment_id\>\<member_id\>\<table\>\<variable_id\>\<grid_label\>\<version\>",

* *output_file_template*:    "\<variable_id\>\<table\>\<source_id\>\<experiment_id\>\<member_id\>\<grid_label\>[\<time_range\>]",

* *license*: Use the following template
    * "CMIP6 model data produced by **\<institution's name\>** is licensed under a **\<license\>**. Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file)**[ and at \<URL\>]**. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law."

    * Choose one of the following for **\<license\>**
        * Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/)
        * Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (https://creativecommons.org/licenses/by-nc-sa/4.0/)
        * Creative Commons Attribution-ShareAlike 4.0 International License (https://creativecommons.org/licenses/by-sa/4.0/)
        * Creative Commons CC0 1.0 Universal Public Domain Dedication License (https://creativecommons.org/publicdomain/zero/1.0/)


