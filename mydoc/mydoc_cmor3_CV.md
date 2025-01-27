---
title: Controlled Vocabulary (CMIP6)
tags: [examples, controlled_vocabulary, cmip6]
keywords: example, C, Fortran, Python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_CV/
---

### CMIP6 Controlled vocabulary minimum requirements. 

   * CMOR 3 required a new Controlled Vocabulary file which must contains 4 mandatory keys for CMIP6.
       * institutions_ids:  A dictionary of of registered institution IDs with a description.
       * source_ids:  A dictionary of registered source IDS (model) with a ```specific``` description.
       * experiment_ids:  A dictionary of experiment_ids (CMIP6) pointing to a dictionary  of ```specific``` metadata.
       * grid_labels:  A dictionary of grid labels(gr, gn, ...) pointing to a native_resolution for the selected grid.


<details><summary markdown="span"><b>Click to expand example JSON file</b></summary>

```json
{
"CV": {
    "institution_ids": { "BNU":"GCESS, BNU, Beijing, China" },
    "source_ids": { "CESM1-CAM5": "CESM1 (CAM5): model version ca. 2009" },
    "experiment_ids": { "piControl": { } },
    "grid_labels": { "gr":     { "native_resolution":"5 km" } }
   }
}
```
</details>

### To register, activities, sources or institutions
  * Contact: [cmor@listserv.llnl.gov](mailto:cmor@listserv.llnl.gov)


### CMIP6 required global attributes

* [CMIP6_CV.json](https://github.com/PCMDI/cmor/blob/main/TestTables/CMIP6_CV.json)

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
    "required_global_attributes": 
        [
        "variant_label",
        "activity_id",
        "branch_method",
        "Conventions",
        "creation_date",
        "mip_era",
        "data_specs_version",
        "experiment_id",
        "experiment",
        "forcing_index",
        "further_info_url",
        "frequency",
        "grid",
        "grid_label",
        "native_resolution",
        "initialization_index",
        "institution",
        "institution_id",
        "license",
        "physics_index",
        "product",
        "realization_index",
        "realm",
        "variant_label",
        "source",
        "source_id",
        "source_type",
        "sub_experiment",
        "sub_experiment_id",
        "table_id",
        "tracking_id",
        "variable_id"
        ],
```
</details>

* CMOR validates required attributes using list of values or regular expression(REGEX)

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
    "required_parent_attributes": [
        "parent_experiment_id"
        ],

    "variant_label": [ "^r[[:digit:]]\\{1,\\}i[[:digit:]]\\{1,\\}p[[:digit:]]\\{1,\\}f[[:digit:]]\\{1,\\}$" ],

    "sub_experiment_id": [ "^s[[:digit:]]\\{4,4\\}$", "none" ],

    "product": [ "output" ] ,

    "mip_era": [ "CMIP6" ],

    "further_info_url": [ "http://furtherinfo.es-doc.org/[[:alpha:]]\\{1,\\}" ],
```
</details>

### Registered activities 

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"activity_id":[
            "AerChemMIP",
            "C4MIP",
            "CFMIP",
            "CMIP",
            "CORDEX",
            "DAMIP",
            "DCPP",
            "DynVarMIP",
            "FAFMIP",
            "GMMIP",
            "GeoMIP",
            "HighResMIP",
            "ISMIP6",
            "LS3MIP",
            "LUMIP",
            "OMIP",
            "PMIP",
            "RFMIP",
            "SIMIP",
            "ScenarioMIP",
            "VIACSAB",
            "VolMIP"
],
```

</details>

### Registered sources

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json

    "source_ids": {
        "ACCESS1-0": "ACCESS1.0: adaptation of unified model with interactive chemistry (ca. 2012)" ,
        ...
        },
```
</details>

### Registered institutions

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
    "institution_ids": {
            "NSF-DOE-NCAR":"NSF/DOE NCAR (National Center for Atmospheric Research) Boulder, CO, USA"
            ...
    },
```

</details>

### valid grids

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
    "grid_labels": {

        "gs1x1":     { "native_resolution":"1x1" },
        "gs1x1 gn":  { "native_resolution":"1x1" },
        "gs1x1 gr":  { "native_resolution":"1x1" },
        "gn": { "native_resolution":[  "5 km",   "10 km",   "25 km",   "50 km",   "100 km", "250 km", 
                "500 km", "1000 km", "2500 km", "5000 km", "10000 km" ] },
        "gr":  { "native_resolution":[  "5 km",   "10 km",   "25 km",   "50 km",   "100 km", "250 km", 
                "500 km", "1000 km", "2500 km", "5000 km", "10000 km" ] }

    },

```

</details>

### Registered experiments

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json

experiment_ids": { 

            "piControl":{
                "activity_id":[
                    "CMIP"
                ],
                "additional_allowed_model_components":[
                    "AER",
                    "CHEM",
                    "BGC"
                ],
                "description":"DECK: control",
                "end_year":"",
                "experiment":"pre-industrial control",
                "experiment_id":"piControl",
                "min_number_yrs_per_sim":"500",
                "parent_activity_id":[
                    "CMIP"
                ],
                "parent_experiment_id":[
                    "piControl-spinup"
                ],
                "required_model_components":[
                    "AOGCM"
                ],
                "start_year":"",
                "sub_experiment_id":[
                    "none"
                ],
                "tier":"1"
}
```
 
</details>