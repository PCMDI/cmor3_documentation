---
title: Controlled Vocabulary (CMIP6)
tags: [examples, controlled_vocabulary, cmip6]
keywords: example, C, Fortran, Python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_CV/
---

### CMIP6 Controlled vocabulary minimum requirements. 

   * CMOR 3 required a new Controlled Vocabulary file which must contains 5 mandatory keys for CMIP6.
       * institutions_ids:  A dictionary of of registered institution IDs with a description.
       * source_ids:  A dictionary of registered source IDS (model) with a ```specific``` description.
       * experiment_ids:  A dictionary of experiment_ids (CMIP6) pointing to a dictionary  of ```specific``` metadata.
       * grid_labels:  An array or dictionary of grid labels (gr, gn, ...).
       * nominal_resolution: An array or dictionary of grid resolutions ("0.5 km", "1 km", "10 km", ...).


<details><summary markdown="span"><b>Click to expand example JSON file</b></summary>

```json
{
"CV": {
    "institution_ids": { "BNU":"GCESS, BNU, Beijing, China" },
    "source_ids": { "CESM1-CAM5": "CESM1 (CAM5): model version ca. 2009" },
    "experiment_ids": { "piControl": { } },
    "grid_labels": { "gn": "data reported on a model's native grid" },
    "nominal_resolution": [ "0.5 km" ]
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
"required_global_attributes": [
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

### CV attribute format

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

* CMOR can also validate required attributes using JSON objects containing key-value pairs where the "key" is a value option for the attribute and the "value" is a description of the value

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"realm":{
    "aerosol":"Aerosol",
    "atmos":"Atmosphere",
    "atmosChem":"Atmospheric Chemistry",
    "land":"Land Surface",
    "landIce":"Land Ice",
    "ocean":"Ocean",
    "ocnBgchem":"Ocean Biogeochemistry",
    "seaIce":"Sea Ice"
},
"frequency":{
    "1hr":"sampled hourly",
    "1hrCM":"monthly-mean diurnal cycle resolving each day into 1-hour means",
    "1hrPt":"sampled hourly, at specified time point within an hour",
    "3hr":"3 hourly mean samples",
    "3hrPt":"sampled 3 hourly, at specified time point within the time period",
    "6hr":"6 hourly mean samples",
    "6hrPt":"sampled 6 hourly, at specified time point within the time period",
    "day":"daily mean samples",
    "dec":"decadal mean samples",
    "fx":"fixed (time invariant) field",
    "mon":"monthly mean samples",
    "monC":"monthly climatology computed from monthly mean samples",
    "monPt":"sampled monthly, at specified time point within the time period",
    "subhrPt":"sampled sub-hourly, at specified time point within an hour",
    "yr":"annual mean samples",
    "yrPt":"sampled yearly, at specified time point within the time period"
},
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
"source_id": {
    "ACCESS-CM2":{
        "activity_participation":[
            "CMIP",
            "DAMIP",
            "FAFMIP",
            "OMIP",
            "RFMIP",
            "SIMIP",
            "ScenarioMIP"
        ],
        "cohort":[
            "Published"
        ],
        "institution_id":[
            "CSIRO-ARCCSS"
        ],
        "license_info":{
            "exceptions_contact":"@csiro.au <- access_csiro",
            "history":"2019-11-08: initially published under CC BY-SA 4.0; 2022-06-10: relaxed to CC BY 4.0",
            "id":"CC BY 4.0",
            "license":"Creative Commons Attribution 4.0 International (CC BY 4.0; https://creativecommons.org/licenses/by/4.0/)",
            "source_specific_info":"",
            "url":"https://creativecommons.org/licenses/by/4.0/"
        },
        "source_id":"ACCESS-CM2",
        "source":"ACCESS-CM2 (2019): \naerosol: UKCA-GLOMAP-mode\natmos: MetUM-HadGEM3-GA7.1 (N96; 192 x 144 longitude/latitude; 85 levels; top level 85 km)\natmosChem: none\nland: CABLE2.5\nlandIce: none\nocean: ACCESS-OM2 (GFDL-MOM5, tripolar primarily 1deg; 360 x 300 longitude/latitude; 50 levels; top grid cell 0-10 m)\nocnBgchem: none\nseaIce: CICE5.1.2 (same grid as ocean)"
    },
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

### Valid grids

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"grid_labels": {
    "gm":"global mean data",
    "gn":"data reported on a model's native grid",
    "gna":"data reported on a native grid in the region of Antarctica",
    "gng":"data reported on a native grid in the region of Greenland",
    "gnz":"zonal mean data reported on a model's native latitude grid",
    "gr":"regridded data reported on the data provider's preferred target grid"
},
```

</details>

### Grid resolutions

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"nominal_resolution":[
    "0.5 km",
    "1 km",
    "10 km",
    "100 km",
    "1000 km",
    "10000 km",
    "1x1 degree",
    "2.5 km",
    "25 km",
    "250 km",
    "2500 km",
    "5 km",
    "50 km",
    "500 km",
    "5000 km"
],
```

</details>

### Registered experiments

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"experiment_id": { 
    "piControl":{
        "activity_id":[
            "CMIP"
        ],
        "additional_allowed_model_components":[
            "AER",
            "CHEM",
            "BGC"
        ],
        "experiment":"pre-industrial control",
        "experiment_id":"piControl",
        "parent_activity_id":[
            "CMIP"
        ],
        "parent_experiment_id":[
            "piControl-spinup"
        ],
        "required_model_components":[
            "AOGCM"
        ],
        "sub_experiment_id":[
            "none"
        ]
    },
}
```
 
</details>