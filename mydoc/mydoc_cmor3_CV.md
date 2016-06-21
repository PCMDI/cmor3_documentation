---
title: Control Vocabulary (CMIP6)
tags: [examples]
keywords: example, C, Fortran, Python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_CV/
---

### To register, activities, sources or institutions
  * Contact: [cmor@listserv.llnl.gov](mailto:cmor@listserv.llnl.gov)

### CMIP6 required global attributes

* [CMIP6_CV.json](https://github.com/PCMDI/cmor/blob/master/TestTables/CMIP6_CV.json)

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
        "grid_resolution",
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

* CMOR validates required attributes using list of values or regular expression(REGEX)

```json
    "required_parent_attributes": [
        "parent_experiment_id"
        ],

    "variant_label": [ "^r[[:digit:]]\\{1,\\}i[[:digit:]]\\{1,\\}p[[:digit:]]\\{1,\\}f[[:digit:]]\\{1,\\}$" ],

    "sub_experiment_id": [ "^s[[:digit:]]\\{4,4\\}$", "none" ],

    "product": [ "output" ] ,

    "mip_era": [ "CMIP6" ],

    "frequency": [ "3hr", "6hr", "day", "fx", "mon", "monClim", "subhr", "yr" ],

    "further_info_url": [ "http://furtherinfo.es-doc.org/[[:alpha:]]\\{1,\\}" ],
```

### Registered activities 

```json
    "activity_id": [
        "DECK",
        "AerChemMIP", 
        "C4MIP", 
        "CFMIP", 
        "CMIP", 
        "CORDEX", 
        "DAMIP", 
        "DCPP", 
        "DynVar", 
        "FAFMIP", 
        "GMMIP", 
        "GeoMIP", 
        "HighResMIP", 
        "ISMIP6", 
        "LS3MIP", 
        "LUMIP", 
        "OMIP", 
        "PDRMIP", 
        "PMIP", 
        "RFMIP", 
        "SIMIP", 
        "ScenarioMIP", 
        "SolarMIP", 
        "VIACSAB", 
        "VolMIP",
        "LS3MIP LUMIP",
        "RFMIP, AerChemMIP",
        "ScenarioMIP AerChemMIP",
        "ScenarioMIP AerChemMIP LUMIP"
        ],
```

### Registered sources

```json

    "source_ids": {
        "ACCESS1-0": "ACCESS1.0: adaptation of unified model with interactive chemistry (ca. 2012)" ,
        "AWI-CM": "AWI-CM:",
        "BCC": "BCC:",
        "BESM": "BESM:",
        "BNU": "BNU:",
        "CAMS-CSM": "CAMS-CSM:",
        "CAS-ESM": "CAS-ESM:",
        "CESM1-CAM5": "CESM1 (CAM5): model version ca. 2009",
        "CESS-THU": "CESS-THU:",
        "CMCC": "CMCC:",
        "CNRM": "CNRM:",
        "CanESM": "CanESM:",
        "EC-Earth": "EC-Earth:",
        "FGOALS": "FGOALS:",
        "FIO": "FIO:",
        "GFDL-CM2-1": "GFDL CM2.1",
        "GISS": "GISS:",
        "HadGEM3": "HadGEM3:",
        "IITM": "IITM:",
        "INM": "INM:",
        "IPSL": "IPSL:",
        "KMA-ACE": "KMA-ACE:",
        "MIROC-ESM": "MIROC-ESM:",
        "MIROC6-CGCM": "MIROC6-CGCM:",
        "MPI-ESM": "MPI-ESM:",
        "MRI-AGCM3-xS": "MRI-AGCM3-xS:",
        "MRI-ESM1-x": "MRI-ESM1-x:",
        "NICAM": "NICAM:",
        "NUIST-CSM": "NUIST-CSM:",
        "NorESM": "NorESM:",
        "UKESM": "UKESM:",
        "UKESM--KMA": "UKESM--KMA:"
        },
```

### Registered institutions

```json
    "institution_ids": {
            "NOAA-GFDL":"NOAA Geophysical Fluid Dynamics Laboratory",
            "BCC":"Beijing Climate Center,China Meteorological Administration,China",
            "BNU":"GCESS,BNU,Beijing,China",
            "CCCma":"Canadian Centre for Climate Modelling and Analysis, Victoria, BC, Canada",
            "CMCC":"Centro Euro-Mediterraneo per i Cambiamenti Climatici, Bologna, Italy",
            "CNRM-CERFACS":"Centre National de Recherches Meteorologiques, Meteo-France, Toulouse, France) and CERFACS (Centre Europeen de Recherches et de Formation Avancee en Calcul Scientifique, Toulouse, France",
            "COLA-CFS":"Center for Ocean-Land-Atmosphere Studies, Calverton, MD",
            "CSIRO-BOM":"Commonwealth Scientific and Industrial Research Organisation, Australia, and Bureau of Meteorology, Australia",
            "CSIRO-QCCCE":"Australian Commonwealth Scientific and Industrial Research Organization (CSIRO) Marine and Atmospheric Research (Melbourne, Australia) in collaboration with the Queensland Climate Change Centre of Excellence (QCCCE) (Brisbane, Australia)",
            "FIO":"The First Institution of Oceanography,SOA,Qingdao,China",
            "ICHEC":"European Earth System Model",
            "INM":"Institute for Numerical Mathematics, Moscow, Russia",
            "IPSL":"Institut Pierre Simon Laplace, Paris, France",
            "LASG-CESS":"Institute of Atmospheric Physics, Chinese Academy of Sciences, Beijing, China and Tsinghua University",
            "LASG-IAP":"Institute of Atmospheric Physics, Chinese Academy of Sciences,Beijing,China",
            "MIROC":"AORI (Atmosphere and Ocean Research Institute, The University of Tokyo, Chiba, Japan), NIES (National Institute for Environmental Studies, Ibaraki, Japan), JAMSTEC (Japan Agency for Marine-Earth Science and Technology, Kanagawa, Japan)",
            "MIROC":"JAMSTEC (Japan Agency for Marine-Earth Science and Technology, Kanagawa, Japan), AORI (Atmosphere and Ocean Research Institute, The University of Tokyo, Chiba, Japan), and NIES (National Institute for Environmental Studies, Ibaraki, Japan)",
            "MOHC":"Met Office Hadley Centre, Fitzroy Road, Exeter, Devon, EX1 3PB, UK.",
            "MPI-M":"Max Planck Institute for Meteorology",
            "MRI":"Meteorological Research Institute, Tsukuba, Japan",
            "NASA-GISS":"Goddard Institute for Space Studies, New York, NY",
            "NASA-GMAO":"Global Modeling and Assimilation Office, NASA Goddard Space Flight Center, Greenbelt, MD 20771",
            "NCAR":"National Center for Atmospheric Research, Boulder, CO, USA",
            "NCC":"Norwegian Climate Centre",
            "NICAM":"Nonhydrostatic Icosahedral Atmospheric Model (NICAM) Group (RIGC-JAMSTEC/AORI-U.Tokyo/AICS-RIKEN,Japan)",
            "NIMR-KMA":"National Institute of Meteorological Research, Seoul, South Korea",
            "NOAA-GFDL":"NOAA GFDL, 201 Forrestal Rd, Princeton, NJ, 08540",
            "NOAA-NCEP":"National Centers for Environmental Prediction, Camp Springs, MD",
            "NSF-DOE-NCAR":"National Center for Atmospheric Research, Boulder, CO, USA",
            "NSF-DOE-NCAR":"PNNL (Pacific Northwest National Laboratory) Richland, WA, USA/NCAR (National Center for Atmospheric Research) Boulder, CO, USA",
            "NSF-DOE-NCAR":"NSF/DOE NCAR (National Center for Atmospheric Research) Boulder, CO, USA"
    },
```

### valid grids

```json
    "grid_labels": {

        "gs1x1":     { "grid_resolution":"1x1" },
        "gs1x1 gn":  { "grid_resolution":"1x1" },
        "gs1x1 gr":  { "grid_resolution":"1x1" },
        "gn": { "grid_resolution":[  "5 km",   "10 km",   "25 km",   "50 km",   "100 km", "250 km", 
                "500 km", "1000 km", "2500 km", "5000 km", "10000 km" ] },
        "gr":  { "grid_resolution":[  "5 km",   "10 km",   "25 km",   "50 km",   "100 km", "250 km", 
                "500 km", "1000 km", "2500 km", "5000 km", "10000 km" ] }

    },

```

### Registered experiments

```json

    "experiment_ids": { 

        "hist-piNTCF": {
                               "experiment":                "historical forcing, but with pre-industrial NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "hist-piAer": {
                               "experiment":                "historical forcing, but with pre-industrial aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "hist-1950HC": {
                               "experiment":                "historical forcing, but with1950s halocarbon concentrations; initialized in 1950",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST": {
                               "experiment":                "historical prescribed SSTs and historical forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "histSST-piNTCF": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-piAer": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "histSST-piO3": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial ozone precursor emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-1950HC": {
                               "experiment":                "historical SSTs and historical forcing, but with1950 halocarbon concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-piCH4": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial methane concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-piN2O": {
                               "experiment":                "historical SSTs and historical forcings, but with pre-industrial N2O concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370": {
                               "experiment":                "Gap-filling scenario reaching 7.0 based on SSP3",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370-lowNTCF": {
                               "experiment":                "SSP3-7.0, with low NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST": {
                               "experiment":                "SSP3-7.0, with  SSTs prescribed from ssp370",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST-lowNTCF": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370SST-lowAer": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST-lowBC": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low black carbon emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST-lowO3": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low ozone precursor emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370SST-lowCH4": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low methane concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370SST-lowLu": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low land-use change",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-control": {
                               "experiment":                "pre-industrial with prescribed climatological SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP, AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-NTCF": {
                               "experiment":                "pre-industrial climatolgical SSTs and forcing, but with 2014 NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-aer": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but 2014 aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-BC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 black carbon emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-O3": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 ozone precursor emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-CH4": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 methane concentrations (including chemistry)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-N2O": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 N2O concentrations (including chemistry)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-HC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 halocarbon concentrations (including chemistry)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-NOX": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 NOx emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-VOC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 VOC emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-2xdust": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of dust",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xss": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of sea salt",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xDMS": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of DMS",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xfire": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions from fires",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xNOX": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled production of NOX due to lightning",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-2xVOC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of biogenic VOCs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "1pctCO2-bgc": {
                               "experiment":                "biogeochemically-coupled version of 1 percent per year increasing CO2 experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "CHEM AER"

                          },

        "1pctCO2Ndep": {
                               "experiment":                "1 percent per year increasing CO2 experient with increasing N-deposition",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "CHEM AER"

                          },

        "1pctCO2Ndep-bgc": {
                               "experiment":                "biogeochemically-coupled version of 1 percent per year increasing CO2 experiment with increasing N-deposition",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "CHEM AER"

                          },

        "1pctCO2-rad": {
                               "experiment":                "radiatively-coupled version of 1 percent per year increasing CO2 experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hist-bgc": {
                               "experiment":                "biogeochemically-coupled version of the simulation of the recent past with CO2 concentration prescribed ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "CHEM AER"

                          },

        "esm-ssp585": {
                               "experiment":                "update of emission-driven RCP8.5 based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "CHEM AER"

                          },

        "ssp585-bgc": {
                               "experiment":                "biogeochemically-coupled version of the updated emission-driven RCP8.5 based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "C4MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "CHEM AER"

                          },

        "abrupt-0p5xCO2": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "abrupt-2xCO2": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "abrupt-solm4p": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "abrupt-solp4p": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-p4K": {
                               "experiment":                "AMIP plus 4K SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-4xCO2": {
                               "experiment":                "control SSTs with 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-pat4K": {
                               "experiment":                "AMIP plus warming pattern SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-m4K": {
                               "experiment":                "AMIP minus 4K SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-piForcing": {
                               "experiment":                "AMIP SSTs with control forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amipFuture-4xCO2-all": {
                               "experiment":                "AMIP plus warming pattern SSTs with 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "aqua-p4K": {
                               "experiment":                "aquaplanet plus 4K SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "aqua-4xCO2": {
                               "experiment":                "aquaplanet with 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "aqua-control": {
                               "experiment":                "Aquaplanet control",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-lwoff": {
                               "experiment":                "AMIP SSTs with longwave cloud-radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-p4K-lwoff": {
                               "experiment":                "AMIP plus 4K SSTs with longwave cloud radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "aqua-p4K-lwoff": {
                               "experiment":                "aquaplanet plus 4K SSTs with longwave cloud radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "aqua-control-lwoff": {
                               "experiment":                "aquaplanet with longwave cloud radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piSST-control": {
                               "experiment":                "control SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piSST-pxK": {
                               "experiment":                "control plus scaled warming pattern",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piSST-4xCO2-rad": {
                               "experiment":                "control SSTs with radiation-only seeing 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piSST-4xCO2-all": {
                               "experiment":                "control SSTs with 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "futureSST": {
                               "experiment":                "control plus warming pattern SSTs ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "futureSST-4xCO2-all": {
                               "experiment":                "control plus warming pattern SSTs with 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "1pctCO2": {
                               "experiment":                "1 percent per year increase in CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "abrupt-4xCO2": {
                               "experiment":                "abrupt quadrupling of CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip": {
                               "experiment":                "AMIP",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piControl": {
                               "experiment":                "pre-Industrial control",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "esm-piControl": {
                               "experiment":                "pre-industrial control simulation with CO2 concentration calculated",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "CHEM AER"

                          },

        "historical": {
                               "experiment":                "all-forcing simulation of the recent past",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "esm-hist": {
                               "experiment":                "all-forcing simulation of the recent past with atmospheric CO2 concentration calculated ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "CHEM AER"

                          },

        "historical-ext": {
                               "experiment":                "post-2014 all-forcing simulation",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "esm-hist-ext": {
                               "experiment":                "post-2014 all-forcing simulation with atmospheric CO2 concentration calculated",
                               "sub_experiment_id":         "none",
                               "activity_id":               "CMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hist-aer": {
                               "experiment":                "historical anthropogenic aerosols-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-CO2": {
                               "experiment":                "historical CO2-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-all-aer2": {
                               "experiment":                "historical ALL-forcing run with alternate estimates of aerosol forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-all-nat2": {
                               "experiment":                "historical ALL-forcing run with alternate estimates of natural forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-GHG": {
                               "experiment":                "historical well-mixed GHG-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-nat": {
                               "experiment":                "historical natural-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-sol": {
                               "experiment":                "historical solar-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-stratO3": {
                               "experiment":                "historical stratospheric-ozone-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hist-volc": {
                               "experiment":                "historical volcanic-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "ssp245-aer": {
                               "experiment":                "aerosol-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "ssp245-GHG": {
                               "experiment":                "well-mixed GHG-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "ssp245-nat": {
                               "experiment":                "natural-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "ssp245-stratO3": {
                               "experiment":                "stratospheric-ozone-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DAMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER BGM"

                          },

        "hindcast": {
                               "experiment":                "hindcast initialized from observations with historical forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hindcast-control": {
                               "experiment":                "simulation initialized from control with forcing prescribed from a portion of the historical period",
                               "sub_experiment_id":         "none",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hindcast-honest": {
                               "experiment":                "hindcast initialized from observations without observed forcing after initialization",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hindcast-hist": {
                               "experiment":                "initialized from historical simulation without observed forcing after initialization",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "forecast": {
                               "experiment":                "forecast initialized from observations",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amv-control": {
                               "experiment":                "idealized Atlantic control",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amv-plus": {
                               "experiment":                "idealized positive AMV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amv-minus": {
                               "experiment":                "idealized negative AMV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "pdv-control": {
                               "experiment":                "idealized Pacific control",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "pdv-plus": {
                               "experiment":                "idealized positive PDV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "pdv-minus": {
                               "experiment":                "idealized negative PDV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "pdv-plus-extraTrop": {
                               "experiment":                "idealized positive extratropical AMV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "pdv-minus-extraTrop": {
                               "experiment":                "idealizedÊ impact of a negative extratropical AMV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amv-plus-trop": {
                               "experiment":                "idealized positive tropical AMV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amv-minus-trop": {
                               "experiment":                "idealized impact of a positive tropical AMV anomaly pattern",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "predictability-atlGyre": {
                               "experiment":                "predictability of 1990s warming of Atlantic gyre",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hindcast-novolc": {
                               "experiment":                "hindcast but with only background volcanic forcing",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "forecast-Pinatubo": {
                               "experiment":                "2015 forecast with added Pinatubo forcing",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "forecast-ElChichon": {
                               "experiment":                "2015 forecast with added El Chichon forcing",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "forecast-Agung": {
                               "experiment":                "2015 forecast with added Agung forcing",
                               "sub_experiment_id":         "initiate with year YYYY",
                               "activity_id":               "DCPP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "faf-all": {
                               "experiment":                "control plus perturbative surface fluxes of momentum, heat and water into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "FAFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "faf-heat": {
                               "experiment":                "control plus perturbative surface flux of heat into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "FAFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "faf-passiveheat": {
                               "experiment":                "control plus surface flux of passive heat tracer into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "FAFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "faf-stress": {
                               "experiment":                "control plus perturbative surface flux of momentum into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "FAFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "faf-water": {
                               "experiment":                "control plus perturbative surface flux of water into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "FAFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G1": {
                               "experiment":                "abrupt quadrupling of CO2 plus reduction in total solar irradiance",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piSST-4xCO2-solar": {
                               "experiment":                "preindustrial conrol SSTs with quadrupled CO2 + solar reduction. ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "futureSST-4xCO2-solar": {
                               "experiment":                "year 100 SSTs from abrupt4xCO2 with quadrupled CO2 + solar reduction",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G6SST1": {
                               "experiment":                "SSTs, forcings, and other prescribed conditions from year 2020 of SSP5-8.5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G6solar": {
                               "experiment":                "total solar irradiance reduction to reduce net forcing from SSP585 to SSP245",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G6SST2-solar": {
                               "experiment":                "SSTs from year 2020 of SSP5-8.5; forcings and other prescribed conditions from year 2100 of G6solar",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G6sulfur": {
                               "experiment":                "stratospheric sulfate aerosol injection to reduce net forcing from SSP585 to SSP245",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G6SST2-sulfur": {
                               "experiment":                "SSTs from year 2020 of SSP5-8.5; forcings and other prescribed conditions from year 2100 of G6sulfur",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G7cirrus": {
                               "experiment":                "G7cirrus _ increase cirrus ice crystal fall speed to reduce net forcing in SSP585 by 1 W m-2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G7SST1-cirrus": {
                               "experiment":                "SSTs from year 2020 of SSP5-8.5; forcings and other prescribed conditions from year 2020 of SSP5-8.5 + cirrus thinning",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "G7SST2-cirrus": {
                               "experiment":                "SSTs from year 2100 of SSP5-8.5; forcings and other prescribed conditions from year 2100 of G7cirrus",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GeoMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-hist": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GMMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-hld": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GMMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-TIP": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GMMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-TIP-nosh": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GMMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hist-resAMO": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GMMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hist-resIPO": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "GMMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "control-1950": {
                               "experiment":                "coupled control with fixed 1950's forcing (HighResMIP equivalent of pre-industrial control)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highres-future": {
                               "experiment":                "coupled future 2015-2050 using a scenario as close to CMIP5 RCP8.5 as possible within CMIP6",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hist-1950": {
                               "experiment":                "coupled historical 1950-2014",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highresSST-present": {
                               "experiment":                "forced atmosphere experiment for 1950-2014",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highresSST-future": {
                               "experiment":                "forced atmosphere experiment for 2015-2050 using SST/sea-ice derived from CMIP5 RCP8.5 simulations and a scenario as close to RCP8.5 as possible within CMIP6",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highresSST-LAI": {
                               "experiment":                "common LAI dataset within the highresSST-present experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highresSST-smoothed": {
                               "experiment":                "smoothed SST version of highresSST-present",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highresSST-p4K": {
                               "experiment":                "uniform 4K warming of highresSST-present SST",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "highresSST-4co2": {
                               "experiment":                "highresSST-present SST with 4xCO2 concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "HighResMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "ism-1pctCO2": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ISMIP6",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    "CHEM AER"

                          },

        "1pctCO2-withism": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ISMIP6",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "CHEM AER"

                          },

        "ism-piControl": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ISMIP6",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piControl-withism": {
                               "experiment":                "to be filled",
                               "sub_experiment_id":         "none",
                               "sub_experiment_id":         "s1968",
                               "activity_id":               "ISMIP6",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "CHEM AER"

                          },

        "ism-ssp585": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ISMIP6",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    "CHEM AER"

                          },

        "ssp585-withism": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ISMIP6",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-lfmip-pObs": {
                               "experiment":                "prescribed land (from pseudo-observations) and AMIP SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-lfmip-pdLC": {
                               "experiment":                "prescribed land (from current climatology) and AMIP SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "lfmip-pdLC": {
                               "experiment":                "prescribed land conditions (from current climate climatology) and initialized from 'historical' run year 1980",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "lfmip-initLC": {
                               "experiment":                "initialized from 'historical' run year 1980, but with land conditions initialized from pseudo-observations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "amip-lfmip-rmLC": {
                               "experiment":                "prescribed land conditions (from running mean climatology) and AMIP SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "lfmip-rmLC": {
                               "experiment":                "prescribed land conditions (from running mean climatology) and initialized from 'historical' run year 1980",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "land-future": {
                               "experiment":                "offline land simulations for future climate",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist": {
                               "experiment":                "offline land simulations for present climate",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist-princeton": {
                               "experiment":                "as land-hist with Princeton forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist-cruNcep": {
                               "experiment":                "as land-hist with CRU-NCEP forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist-wfdei": {
                               "experiment":                "as land-hist with WFDEI forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "esm-ssp585-ssp126Lu": {
                               "experiment":                "emissions-driven SSP5-8.5 with SSP1-2.6 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "CHEM AER"

                          },

        "hist-noLu": {
                               "experiment":                "historical with no land-use change",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "deforest-globe": {
                               "experiment":                "idealized transient global deforestation",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "land-hist-altStartYear": {
                               "experiment":                "historical land-only alternate start year",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist": {
                               "experiment":                "historical land-only",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LS3MIP LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-cCO2": {
                               "experiment":                "historical land-only constant CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-cClim": {
                               "experiment":                "historical land-only constant climate",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noLu": {
                               "experiment":                "historical land-only with no land-use change",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-noManage": {
                               "experiment":                "historical land-only with crops but no crop management",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-netTrans": {
                               "experiment":                "historical land-only with net land-use transitions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noFire": {
                               "experiment":                "historical land-only with no human fire management",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noWoodHarv": {
                               "experiment":                "historical land-only with no wood harvest",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noPasture": {
                               "experiment":                "historical land-only with constant pastureland",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-grass": {
                               "experiment":                "historical land-only with cropland as natural grassland",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-noIrrig": {
                               "experiment":                "historical land-only with no irrigation ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-noFert": {
                               "experiment":                "historical land-only with no fertilizer",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "ssp126-ssp370Lu": {
                               "experiment":                "SSP1-2.6 with SSP3-7.0 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "ssp370-ssp126Lu": {
                               "experiment":                "SSP3-7.0 with SSP1-2.6 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "omip-core2": {
                               "experiment":                "OMIP experiment forced by CORE-2 atmospheric data set and initialized with observed physical and biogeochemical ocean data",
                               "sub_experiment_id":         "none",
                               "activity_id":               "OMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "omip-core2-spunup": {
                               "experiment":                "OMIP experiment forced by CORE-2 atmospheric data set and initialized from at least a 2000-year spin up of the coupled physical-biogeochemical model",
                               "sub_experiment_id":         "none",
                               "activity_id":               "OMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "omip-jra55": {
                               "experiment":                "OMIP experiment forced by JRA-55 atmospheric data set and initialized with observed physical and biogeochemical ocean data",
                               "sub_experiment_id":         "none",
                               "activity_id":               "OMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "omip-jra55-spunup": {
                               "experiment":                "OMIP experiment forced by JRA-55 atmospheric data set and initialized from at least a 2000-year spin up of the coupled physical-biogeochemical model",
                               "sub_experiment_id":         "none",
                               "activity_id":               "OMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "lgm": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "PMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "lig127k": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "PMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "midHolocene": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "PMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "past1000": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "PMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "midPliocene-eoi400": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "PMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-control": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP, AerChemMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-4xCO2": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-aerO3": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-aerO3x0p1": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-aerO3x2": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-anthro": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-GHG": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-histaer03": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-histAll": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-histGHG": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-histNat": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-lu": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "CHEM AER"

                          },

        "piClim-spAer-histall": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "piClim-spAer-histaer": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "piClim-spAer-aer": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "piClim-spAer-anthro": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "hist-spAer": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    ""

                          },

        "hist-all-spAer": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    ""

                          },

        "rad-irf": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "RFMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "RAD",
                               "additional_source_type":    ""

                          },

        "ssp126": {
                               "experiment":                "update of RCP2.6 based on SSP1",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "ssp534-over": {
                               "experiment":                "overshoot of 3.4 W/m**2 branching from ssp585 in 2040",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "ssp585",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "ScenarioMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "ssp460": {
                               "experiment":                "update of RCP6.0 based on SSP4",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "ssp245": {
                               "experiment":                "update of RCP4.5 based on SSP2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "ssp370": {
                               "experiment":                "gap-filling scenario reaching 7.0 based on SSP3",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP AerChemMIP LUMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "ssp434": {
                               "experiment":                "gap-filling scenario reaching 3.4 based on SSP4",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "ssp585": {
                               "experiment":                "update of RCP8.5 based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "sspxy": {
                               "experiment":                "low-end scenario informing 1.5C goal",
                               "sub_experiment_id":         "none",
                               "activity_id":               "ScenarioMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "historical",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcCluster": {
                               "experiment":                "long volcanic-forcing-only experiment with cluster of eruption",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcEq-S60": {
                               "experiment":                "long volcanic-forcing-only experiment with single equatorial eruption",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcHL-S100": {
                               "experiment":                "long volcanic-forcing-only experiment with single high-latitude eruption",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcEq-full": {
                               "experiment":                "Pinatubo experiment with full volcanic forcing ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcEq-ini": {
                               "experiment":                "Pinatubo experiment in decadal climate prediction setup",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcEq-slab": {
                               "experiment":                "Pinatubo experiment with full volcanic forcing and slab ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM SLAB",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcEq-strat": {
                               "experiment":                "Pinatubo experiment with only long-wave forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          },

        "volcEq-surf": {
                               "experiment":                "Pinatubo experiment with only short-wave forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "VolMIP",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "CHEM AER",
                               "parent_experiment_id" :     "piControl",
                               "parent_sub_experiment_id":  "none",
                               "parent_activity_id ":       "CMIP",
                               "parent_mip_era ":           "CMIP6"
                          }


         }
     }
```
 
