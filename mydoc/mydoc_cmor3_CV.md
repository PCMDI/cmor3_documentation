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

experiment_ids": { 

        "hist-piNTCF": {
                               "experiment":                "historical forcing, but with pre-industrial NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER CHEM",
                               "additional_source_type":    "BGM"

                          },

        "hist-piAer": {
                               "experiment":                "historical forcing, but with pre-industrial aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER",
                               "additional_source_type":    "CHEM BGM"

                          },

        "hist-1950HC": {
                               "experiment":                "historical forcing, but with1950s halocarbon concentrations; initialized in 1950",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER CHEM",
                               "additional_source_type":    "BGM"

                          },

        "histSST": {
                               "experiment":                "historical prescribed SSTs and historical forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "histSST-piNTCF": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-piAer": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "histSST-piO3": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial ozone precursor emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-1950HC": {
                               "experiment":                "historical SSTs and historical forcing, but with1950 halocarbon concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-piCH4": {
                               "experiment":                "historical SSTs and historical forcing, but with pre-industrial methane concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "histSST-piN2O": {
                               "experiment":                "historical SSTs and historical forcings, but with pre-industrial N2O concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    "BGM"

                          },

        "ssp370-lowNTCF": {
                               "experiment":                "SSP3-7.0, with low NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM AER",
                               "additional_source_type":    "CHEM BGM"

                          },

        "ssp370SST": {
                               "experiment":                "SSP3-7.0, with  SSTs prescribed from ssp370",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST-lowNTCF": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370SST-lowAer": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST-lowBC": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low black carbon emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "ssp370SST-lowO3": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low ozone precursor emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370SST-lowCH4": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with low methane concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "ssp370SST-ssp126Lu": {
                               "experiment":                "SSP3-7.0, prescribed SSTs, with SSP1-2.6 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-NTCF": {
                               "experiment":                "pre-industrial climatolgical SSTs and forcing, but with 2014 NTCF emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-aer": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but 2014 aerosol emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-BC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 black carbon emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-O3": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 ozone precursor emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-CH4": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 methane concentrations (including chemistry)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-N2O": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 N2O concentrations (including chemistry)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-HC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 halocarbon concentrations (including chemistry)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-NOX": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 NOx emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-VOC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with 2014 VOC emissions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-2xdust": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of dust",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xss": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of sea salt",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xDMS": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of DMS",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xfire": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions from fires",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER",
                               "additional_source_type":    "CHEM"

                          },

        "piClim-2xNOX": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled production of NOX due to lightning",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "piClim-2xVOC": {
                               "experiment":                "pre-industrial climatological SSTs and forcing, but with doubled emissions of biogenic VOCs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM AER CHEM",
                               "additional_source_type":    ""

                          },

        "1pctCO2-bgc": {
                               "experiment":                "biogeochemically-coupled version of 1 percent per year increasing CO2 experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM"

                          },

        "1pctCO2Ndep": {
                               "experiment":                "1 percent per year increasing CO2 experient with increasing N-deposition",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "1pctCO2Ndep-bgc": {
                               "experiment":                "biogeochemically-coupled version of 1 percent per year increasing CO2 experiment with increasing N-deposition",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM"

                          },

        "1pctCO2-rad": {
                               "experiment":                "radiatively-coupled version of 1 percent per year increasing CO2 experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM"

                          },

        "hist-bgc": {
                               "experiment":                "biogeochemically-coupled version of the simulation of the recent past with CO2 concentration prescribed ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM"

                          },

        "esm-ssp585": {
                               "experiment":                "emission-driven RCP8.5 based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "AER CHEM"

                          },

        "ssp585-bgc": {
                               "experiment":                "biogeochemically-coupled version of the RCP8.5 based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM"

                          },

        "ssp585-over-bgc": {
                               "experiment":                "biogeochemically-coupled version of the RCP3.4-overshoot based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM BGM",
                               "additional_source_type":    "AER CHEM"

                          },

        "abrupt-0p5xCO2": {
                               "experiment":                "abrupt halving of CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "abrupt-2xCO2": {
                               "experiment":                "abrupt doubling of CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "abrupt-solm4p": {
                               "experiment":                "abrupt 4% decrease in solar constant",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "abrupt-solp4p": {
                               "experiment":                "abrupt 4% increase in solar constant",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-p4K": {
                               "experiment":                "AMIP with uniform 4K SST increase",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-4xCO2": {
                               "experiment":                "AMIP SSTs with 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-future4K": {
                               "experiment":                "AMIP with patterned 4K SST increase",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-m4K": {
                               "experiment":                "AMIP with uniform 4K SST decrease",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-piForcing": {
                               "experiment":                "AMIP SSTs with pre-industrial anthro and natural forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "aqua-p4K": {
                               "experiment":                "aquaplanet with uniform 4K SST increase",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "aqua-4xCO2": {
                               "experiment":                "aquaplanet with control SST and 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "aqua-control": {
                               "experiment":                "aquaplanet control",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-lwoff": {
                               "experiment":                "AMIP experiment with longwave cloud-radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-p4K-lwoff": {
                               "experiment":                "AMIP experiment with uniform 4K SST increase and with longwave cloud radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "aqua-p4K-lwoff": {
                               "experiment":                "aquaplanet with uniform 4K SST increase and with longwave cloud radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "aqua-control-lwoff": {
                               "experiment":                "aquaplanet control with longwave cloud radiative effects off",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piSST": {
                               "experiment":                "experiment forced with pre-industrial SSTs, sea ice and atmospheric constituents.",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piSST-pxK": {
                               "experiment":                "as piSST with uniform SST increase with magnitude based on abrupt4xCO2 response",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piSST-4xCO2-rad": {
                               "experiment":                "as piSST with radiation-only seeing 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piSST-4xCO2": {
                               "experiment":                "as piSST with radiation and vegetation seeing 4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "a4SST": {
                               "experiment":                "as piSST but with SSTs from abrupt4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "a4SSTice": {
                               "experiment":                "as piSST but with SSTs and sea ice from abrupt4xCO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "a4SSTice-4xCO2": {
                               "experiment":                "as piSST but with SSTs and sea ice from abrupt4xCO2, and 4xCO2 seen by radiation and vegetation.",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-a4SST-4xCO2": {
                               "experiment":                "as AMIP but with warming pattern from abrupt4xCO2 added to SSTs and 4xCO2 seen by radiation and vegetation",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "1pctCO2": {
                               "experiment":                "1 percent per year increase in CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "abrupt-4xCO2": {
                               "experiment":                "abrupt quadrupling of CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "amip": {
                               "experiment":                "AMIP",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piControl": {
                               "experiment":                "pre-industrial control",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "esm-piControl": {
                               "experiment":                "pre-industrial control simulation with CO2 concentration calculated",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piControl-spinup": {
                               "experiment":                "pre-industrial control (spin-up)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "esm-piControl-spinup": {
                               "experiment":                "pre-industrial control simulation with CO2 concentration calculated (spiin-up)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "AER CHEM"

                          },

        "historical": {
                               "experiment":                "all-forcing simulation of the recent past",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "esm-hist": {
                               "experiment":                "all-forcing simulation of the recent past with atmospheric CO2 concentration calculated ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "AER CHEM"

                          },

        "historical-ext": {
                               "experiment":                "post-2014 all-forcing simulation",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "esm-hist-ext": {
                               "experiment":                "post-2014 all-forcing simulation with atmospheric CO2 concentration calculated",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "AER CHEM"

                          },

        "hist-aer": {
                               "experiment":                "historical anthropogenic aerosols-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-CO2": {
                               "experiment":                "historical CO2-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-all-aer2": {
                               "experiment":                "historical ALL-forcing run with alternate estimates of aerosol forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-all-nat2": {
                               "experiment":                "historical ALL-forcing run with alternate estimates of natural forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-GHG": {
                               "experiment":                "historical well-mixed GHG-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-nat": {
                               "experiment":                "historical natural-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-sol": {
                               "experiment":                "historical solar-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-stratO3": {
                               "experiment":                "historical stratospheric-ozone-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "hist-volc": {
                               "experiment":                "historical volcanic-only run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "ssp245-aer": {
                               "experiment":                "aerosol-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "ssp245-GHG": {
                               "experiment":                "well-mixed GHG-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "ssp245-nat": {
                               "experiment":                "natural-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "ssp245-stratO3": {
                               "experiment":                "stratospheric-ozone-only SSP2-4.5 run",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM, BGM"

                          },

        "dcppA-hindcast": {
                               "experiment":                "year 1-5 hindcast initialized based on observations and using historical forcing",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppA-historical": {
                               "experiment":                "climate simulations initialized from control with forcing prescribed from the historical period and future scenario as in A1",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppA-assim": {
                               "experiment":                "assimilation runs (if available) that are used to generate initial conditions for hindcasts and which parallel the historical simulations and use the same forcing ",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppA-hindcast-niff": {
                               "experiment":                "hindcast initialized from observations without future observed forcing after initialization",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppA-historical-niff": {
                               "experiment":                "hindcast initialized from historical climate simulations without observed forcing after initialization",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppB-forecast": {
                               "experiment":                "year 1-5 forecast initialized from observations",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-atl-control": {
                               "experiment":                "idealized Atlantic control",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-amv-plus": {
                               "experiment":                "idealized positive AMV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-amv-minus": {
                               "experiment":                "idealized negative AMV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-pac": {
                               "experiment":                "idealized Pacific control",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-ipv-plus": {
                               "experiment":                "idealized positive IPV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-ipv-minus": {
                               "experiment":                "idealized negative IPV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-amv-extrop-plus": {
                               "experiment":                "idealized positive extratropical AMV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-amv-extrop-minus": {
                               "experiment":                "idealizedÊ impact of a negative extratropical AMV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-amv-trop-plus": {
                               "experiment":                "idealized positive tropical AMV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-amv-trop-minus": {
                               "experiment":                "idealized impact of a positive tropical AMV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-ipv-nextrop-plus": {
                               "experiment":                "idealized impact of a positive northern extratropical IPV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-ipv-nextrop-minus": {
                               "experiment":                "idealized impact of a negative northern extratropical IPV anomaly pattern",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-pac-pacemaker": {
                               "experiment":                "pacemaker pacific experiment",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-atl-pacemaker": {
                               "experiment":                "pacemaker atlantic experiment ",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-atl-spg": {
                               "experiment":                "predictability of 1990s warming of Atlantic sub-polar gyre",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-hindcast-noPinatubo": {
                               "experiment":                "hindcast but with only background volcanic forcing",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-hindcast-noElChichon": {
                               "experiment":                "",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-hindcast-noAgung": {
                               "experiment":                "",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-forecast-addPinatubo": {
                               "experiment":                "2015 forecast with added Pinatubo forcing",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-forecast-addElChichon": {
                               "experiment":                "2015 forecast with added El Chichon forcing",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "dcppC-forecast-addAgung": {
                               "experiment":                "2015 forecast with added Agung forcing",
                               "sub_experiment_id":         "initialized near end of year YYYY",
                               "activity_id":               "",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "faf-all": {
                               "experiment":                "control plus perturbative surface fluxes of momentum, heat and water into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "faf-heat": {
                               "experiment":                "control plus perturbative surface flux of heat into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "faf-passiveheat": {
                               "experiment":                "control plus surface flux of passive heat tracer into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "faf-stress": {
                               "experiment":                "control plus perturbative surface flux of momentum into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "faf-water": {
                               "experiment":                "control plus perturbative surface flux of water into ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "G1": {
                               "experiment":                "abrupt quadrupling of CO2 plus reduction in total solar irradiance",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "piSST-4xCO2-solar": {
                               "experiment":                "preindustrial conrol SSTs with quadrupled CO2 + solar reduction. ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "futureSST-4xCO2-solar": {
                               "experiment":                "year 100 SSTs from abrupt4xCO2 with quadrupled CO2 + solar reduction",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "G6SST1": {
                               "experiment":                "SSTs, forcings, and other prescribed conditions from year 2020 of SSP5-8.5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "G6solar": {
                               "experiment":                "total solar irradiance reduction to reduce net forcing from SSP585 to SSP245",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "G6SST2-solar": {
                               "experiment":                "SSTs from year 2020 of SSP5-8.5; forcings and other prescribed conditions from year 2100 of G6solar",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "G6sulfur": {
                               "experiment":                "stratospheric sulfate aerosol injection to reduce net forcing from SSP585 to SSP245",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "G6SST2-sulfur": {
                               "experiment":                "SSTs from year 2020 of SSP5-8.5; forcings and other prescribed conditions from year 2100 of G6sulfur",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "G7cirrus": {
                               "experiment":                "G7cirrus _ increase cirrus ice crystal fall speed to reduce net forcing in SSP585 by 1 W m-2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "G7SST1-cirrus": {
                               "experiment":                "SSTs from year 2020 of SSP5-8.5; forcings and other prescribed conditions from year 2020 of SSP5-8.5 + cirrus thinning",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "G7SST2-cirrus": {
                               "experiment":                "SSTs from year 2100 of SSP5-8.5; forcings and other prescribed conditions from year 2100 of G7cirrus",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-hist": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-hld": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-TIP": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-TIP-nosh": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "hist-resAMO": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "hist-resIPO": {
                               "experiment":                "",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "control-1950": {
                               "experiment":                "coupled control with fixed 1950's forcing (HighResMIP equivalent of pre-industrial control)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "highres-future": {
                               "experiment":                "coupled future 2015-2050 using a scenario as close to CMIP5 RCP8.5 as possible within CMIP6",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "hist-1950": {
                               "experiment":                "coupled historical 1950-2014",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "highresSST-present": {
                               "experiment":                "forced atmosphere experiment for 1950-2014",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "highresSST-future": {
                               "experiment":                "forced atmosphere experiment for 2015-2050 using SST/sea-ice derived from CMIP5 RCP8.5 simulations and a scenario as close to RCP8.5 as possible within CMIP6",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "highresSST-LAI": {
                               "experiment":                "common LAI dataset within the highresSST-present experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "highresSST-smoothed": {
                               "experiment":                "smoothed SST version of highresSST-present",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "highresSST-p4K": {
                               "experiment":                "uniform 4K warming of highresSST-present SST",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "highresSST-4co2": {
                               "experiment":                "highresSST-present SST with 4xCO2 concentrations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "ism-1pctCO2to4x-std": {
                               "experiment":                "offline ice sheet model forced by ISMIP6-specified AOGCM 1pctCO2to4x output ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "ism-1pctCO2to4x-self": {
                               "experiment":                "offline ice sheet model forced by ISM's own AOGCM 1pctCO2to4x output ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "1pctCO2to4x-withism": {
                               "experiment":                "simulation with interactive ice sheet forced by 1 percent per year increase in CO2 to 4xCO2 (subsequently held fixed)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ism-pdControl-std": {
                               "experiment":                "offline ice sheet forced by ISMIP6-specified AOGCM pdControl output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "ism-piControl-self": {
                               "experiment":                "offline ice sheet forced by ISM's own AOGCM piControl output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "piControl-withism": {
                               "experiment":                "preindustrial control with interactive ice sheet",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ism-historical-std": {
                               "experiment":                "offline ice sheet forced by ISMIP6-specified AOGCM historical output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "ism-historical-self": {
                               "experiment":                "offline ice sheet forced by ISM's own AOGCM historical output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "historical-withism": {
                               "experiment":                "historical with interactive ice sheet",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ism-ssp585-std": {
                               "experiment":                "offline ice sheet forced by ISMIP6-specified AOGCM ssp585 output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "ism-ssp585-self": {
                               "experiment":                "offline ice sheet forced by ISM's own AOGCM ssp585 output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "ssp585-withism": {
                               "experiment":                "ssp585 with interactive ice sheet",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM ISM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ism-amip-std": {
                               "experiment":                "offline ice sheet forced by ISMIP6-specified AGCM AMIP output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "ism-lig127k-std": {
                               "experiment":                "offline ice sheet forced by ISMIP6-specified AGCM last interglacial output",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ISM",
                               "additional_source_type":    ""

                          },

        "amip-lfmip-pObs": {
                               "experiment":                "prescribed land (from pseudo-observations) and AMIP SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "amip-lfmip-pdLC": {
                               "experiment":                "prescribed land (from current climatology) and AMIP SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "lfmip-pdLC": {
                               "experiment":                "prescribed land conditions (from current climate climatology) and initialized from 'historical' run year 1980",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "lfmip-initLC": {
                               "experiment":                "initialized from 'historical' run year 1980, but with land conditions initialized from pseudo-observations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "amip-lfmip-rmLC": {
                               "experiment":                "prescribed land conditions (from running mean climatology) and AMIP SSTs",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "lfmip-rmLC": {
                               "experiment":                "prescribed land conditions (from running mean climatology) and initialized from 'historical' run year 1980",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "land-future": {
                               "experiment":                "future land-only",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist": {
                               "experiment":                "historical land-only",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist-princeton": {
                               "experiment":                "as land-hist with Princeton forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist-cruNcep": {
                               "experiment":                "as land-hist with CRU-NCEP forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-hist-wfdei": {
                               "experiment":                "as land-hist with WFDEI forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "esm-ssp585-ssp126Lu": {
                               "experiment":                "emissions-driven SSP5-8.5 with SSP1-2.6 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "ESM",
                               "additional_source_type":    "AER CHEM"

                          },

        "hist-noLu": {
                               "experiment":                "historical with no land-use change",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "deforest-globe": {
                               "experiment":                "idealized transient global deforestation",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "land-hist-altStartYear": {
                               "experiment":                "historical land-only alternate start year",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-cCO2": {
                               "experiment":                "historical land-only constant CO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-cClim": {
                               "experiment":                "historical land-only constant climate",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noLu": {
                               "experiment":                "historical land-only with no land-use change",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-noManage": {
                               "experiment":                "historical land-only with crops but no crop management",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-netTrans": {
                               "experiment":                "historical land-only with net land-use transitions",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noFire": {
                               "experiment":                "historical land-only with no human fire management",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noWoodHarv": {
                               "experiment":                "historical land-only with no wood harvest",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-noPasture": {
                               "experiment":                "historical land-only with constant pastureland",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-grass": {
                               "experiment":                "historical land-only with cropland as natural grassland",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-noIrrig": {
                               "experiment":                "historical land-only with no irrigation ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "land-crop-noFert": {
                               "experiment":                "historical land-only with no fertilizer",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "LND",
                               "additional_source_type":    ""

                          },

        "ssp126-ssp370Lu": {
                               "experiment":                "SSP1-2.6 with SSP3-7.0 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp370-ssp126Lu": {
                               "experiment":                "SSP3-7.0 with SSP1-2.6 land use",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "omipv1": {
                               "experiment":                "OMIP experiment forced by Large & Yeager (CORE-2, NCEP) atmospheric data set and initialized with observed physical and biogeochemical ocean data",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "omipv1-spunup": {
                               "experiment":                "OMIP experiment forced by Large & Yeager (CORE-2, NCEP) atmospheric data set and initialized from at least a 2000-year spin up of the coupled physical-biogeochemical model",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "omipv2": {
                               "experiment":                "OMIP experiment forced by JRA-55 atmospheric data set and initialized with observed physical and biogeochemical ocean data",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "omipv2-spunup": {
                               "experiment":                "OMIP experiment forced by JRA-55 atmospheric data set and initialized from at least a 2000-year spin up of the coupled physical-biogeochemical model",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "OGCM",
                               "additional_source_type":    ""

                          },

        "lgm": {
                               "experiment":                "last glacial maximum ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "lig127k": {
                               "experiment":                "last interglacial (127k)",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "midHolocene": {
                               "experiment":                "mid-Holocene",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "past1000": {
                               "experiment":                "last millenium",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "midPliocene-eoi400": {
                               "experiment":                "mid-Pliocene warm period",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "piClim-control": {
                               "experiment":                "effective radiative forcing in present-day ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-4xCO2": {
                               "experiment":                "effective radiative forcing by 4xCO2 ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-aerO3": {
                               "experiment":                "effective radiative forcing by present-day aerosols and ozone",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-aerO3x0p1": {
                               "experiment":                "effective radiative forcing by present-day aerosols and ozone scaled by 0.1 ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-aerO3x2": {
                               "experiment":                "effective radiative forcing by present-day aerosols and ozone scaled by 2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-anthro": {
                               "experiment":                "effective radiative forcing by present day anthropogenic agents",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-GHG": {
                               "experiment":                "effective radiative forcing by present-day greenhouse gases",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-histaer03": {
                               "experiment":                "transient effective radiative forcing by aerosols ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-histAll": {
                               "experiment":                "transient effective radiative forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-histGHG": {
                               "experiment":                "transient effective radiative forcing by greenhouse gases",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-histNat": {
                               "experiment":                "transient effective radiative forcing by natural perturbations",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-lu": {
                               "experiment":                "effective radiative forcing by present-day land use ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    "AER CHEM"

                          },

        "piClim-spAerO3-histall": {
                               "experiment":                " transient effective radiative forcing with specified anthropogenic aerosol optical properties, all forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "piClim-spAerO3-histaer": {
                               "experiment":                "transient effective radiative forcing with specified anthropogenic aerosol optical properties, aerosol forcing",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "piClim-spAerO3-aer": {
                               "experiment":                "effective radiative forcing at present day with specified anthropogenic aerosol optical properties, all forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "piClim-spAerO3-anthro": {
                               "experiment":                "effective radiative forcing at present day with specified anthropogenic aerosol optical properties, anthropogenic forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM",
                               "additional_source_type":    ""

                          },

        "hist-spAerO3": {
                               "experiment":                "historical simulations with specified anthropogenc aerosols, no other forcings",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    ""

                          },

        "hist-all-spAerO3": {
                               "experiment":                "historical simulations with specified anthropogenc aerosols ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    ""

                          },

        "rad-irf": {
                               "experiment":                "offline assessment of radiative transfer parmaeterizations in clear skies",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "RAD",
                               "additional_source_type":    ""

                          },

        "ssp126": {
                               "experiment":                "update of RCP2.6 based on SSP1",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp534-over": {
                               "experiment":                "overshoot of 3.4 W/m**2 branching from ssp585 in 2040",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp460": {
                               "experiment":                "update of RCP6.0 based on SSP4",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp245": {
                               "experiment":                "update of RCP4.5 based on SSP2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp370": {
                               "experiment":                "gap-filling scenario reaching 7.0 based on SSP3",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp434": {
                               "experiment":                "gap-filling scenario reaching 3.4 based on SSP4",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "ssp585": {
                               "experiment":                "update of RCP8.5 based on SSP5",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "sspxy": {
                               "experiment":                "low-end scenario informing 1.5C goal",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-cluster-ctrl": {
                               "experiment":                "19th century volcanic cluster initialized from PiControl",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-cluster-mill": {
                               "experiment":                "19th century volcanic cluster initialized from past1000",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-long-eq": {
                               "experiment":                "idealized equatorial volcanic eruption emitting 56.2 Tg SO2 ",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-long-hlN": {
                               "experiment":                "idealized Northern Hemisphere high-latitude eruption emitting 28.1 Tg of SO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-pinatubo-full": {
                               "experiment":                "Pinatubo experiment",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-pinatubo-ini": {
                               "experiment":                "Pinatubo experiment for decadal climate prediction",
                               "sub_experiment_id":         "initialized near end of year 2014",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "control-slab": {
                               "experiment":                "control with slab ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM SLAB",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-pinatubo-slab": {
                               "experiment":                "Pinatubo experiment with slab ocean",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AGCM SLAB",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-pinatubo-strat": {
                               "experiment":                "Pinatubo experiment with partial radiative forcing, includes only stratospheric warming",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-pinatubo-surf": {
                               "experiment":                "Pinatubo experiment with partial radiative forcing, solar radiation scattering only",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-cluster-21C": {
                               "experiment":                "volcanic cluster experiment under 21st century SSP2-4.5 scenario",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          },

        "volc-long-hlS": {
                               "experiment":                "Idealized Southern Hemisphere high-latitude eruption emitting 28.1 Tg of SO2",
                               "sub_experiment_id":         "none",
                               "activity_id":               "1",
                               "mip_era":                   "CMIP6",
                               "source_type":               "AOGCM",
                               "additional_source_type":    "AER CHEM BGM"

                          }
        }
```
 
