---
title: Controlled Vocabulary (CMIP6)
tags: [examples, controlled_vocabulary, cmip6]
keywords: example, C, Fortran, Python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_CV/
---

### CMIP7 Controlled Vocabulary (CV) in development. 

Work is currently ongoing to develop and document CMIP7 CVs. To see progress, see the following links

    * [CMIP7 Guidance Pages (Overview guidance pages for the CMIP7 project)](https://wcrp-cmip.github.io/cmip7-guidance/)
    * [WCRP Universe (master collection of cross-project MIP relevant content)](https://github.com/WCRP-CMIP/WCRP-universe)
    * [CMIP7-CVs (Controlled Vocabularies for CMIP7)](https://github.com/WCRP-CMIP/CMIP7-CVs)
    * [Variable Registry (Registry of all MIP-relevant variables, for use across MIP projects)](https://github.com/WCRP-CMIP/Variable-Registry)
    * [CMIP7 Essential Model Documentation](https://github.com/WCRP-CMIP/Essential-Model-Documentation)


### CMIP6 Controlled Vocabulary (CV) minimum requirements. 

While the CMIP6 project is now complete, the templates below are preserved and provide guidance which will look very similar
to the CMIP7 CVs once they are finalized.

   * CMOR 3 requires a new Controlled Vocabulary file which must contains 5 mandatory keys for CMIP6.
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
  * See guidance pages above, both for CMIP7 and CMIP6


### CMIP6 Controlled Vocabularies

The [CMIP6 Controlled Vocabularies (CVs)](https://github.com/WCRP-CMIP/CMIP6_CVs) are a collection of registered values, either defined by the project,
or registered by contributors to define their data contributions.

Some examples of project defined content are [`CMIP6_DRS (Data Reference Syntax)`](https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_DRS.json),
[`CMIP6_activity_id (CMIP6 registered MIPs)`](https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_activity_id.json),
[`CMIP6_experiment_id (CMIP6 experiments sponsored by a MIP)`](https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_experiment_id.json), etc.

Examples of contributor defined content are [`CMIP6_institution_id`](https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_institution_id.json),
[`CMIP6_source_id`](https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_source_id.json)

Below are some expanded examples of registered content.

### CMIP6 required global attributes

* [CMIP6_CV.json:required_global_attributes](https://github.com/PCMDI/cmip6-cmor-tables/blob/087fe45d21c082e28723e0f930e4266abe91b853/Tables/CMIP6_CV.json#L3-L34)

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"required_global_attributes": [
    "Conventions",
    "activity_id",
    "creation_date",
    "data_specs_version",
    "experiment",
    "experiment_id",
    "forcing_index",
    "frequency",
    "further_info_url",
    "grid",
    "grid_label",
    "initialization_index",
    "institution",
    "institution_id",
    "license",
    "mip_era",
    "nominal_resolution",
    "physics_index",
    "product",
    "realization_index",
    "realm",
    "source",
    "source_id",
    "source_type",
    "sub_experiment",
    "sub_experiment_id",
    "table_id",
    "tracking_id",
    "variable_id",
    "variant_label"
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

"variant_label": [ "r[[:digit:]]\\{1,\\}i[[:digit:]]\\{1,\\}p[[:digit:]]\\{1,\\}f[[:digit:]]\\{1,\\}$" ],

"product": [ "model-output" ] ,

"mip_era": [ "CMIP6" ],

"further_info_url": [ "https://furtherinfo.es-doc.org/.*" ],
```
</details>

* CMOR can also validate required attributes using JSON objects containing key-value pairs where the "key" is a value option for the attribute and the "value" is a description of the value

<details><summary markdown="span"><b>Click to expand example JSON section</b></summary>

```json
"sub_experiment_id":{
    "none":"none",
    "s1910":"initialized near end of year 1910",
    "s1920":"initialized near end of year 1920",
    "s1950":"initialized near end of year 1950"
}
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

* [CMIP6_CV.json:activity_id](https://github.com/PCMDI/cmip6-cmor-tables/blob/087fe45d21c082e28723e0f930e4266abe91b853/Tables/CMIP6_CV.json#L48-L73)

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