#!/usr/bin/env python3

from __future__ import annotations

import json
import os
from pathlib import Path

import cmor
import numpy as np

EXAMPLE_DIR = Path(__file__).resolve().parent
RUN_DIR = Path.cwd()
DEFAULT_TABLES_PATH = RUN_DIR / "cmip7-cmor-tables" / "tables"
TABLES_PATH = Path(os.environ.get("CMOR_TABLES_PATH", DEFAULT_TABLES_PATH))
INPUT_PATH = EXAMPLE_DIR / "CMIP7_input_example.json"

os.chdir(EXAMPLE_DIR)
(EXAMPLE_DIR / "output").mkdir(exist_ok=True)
cmor.setup(inpath=str(TABLES_PATH), netcdf_file_action=cmor.CMOR_REPLACE)
cmor.dataset_json(str(INPUT_PATH))
cmor.load_table("CMIP7_ocean.json")
time_id = cmor.axis(
    "time",
    "days since 1979-01-01",
    coord_vals=np.array([15.5, 45.5], dtype="d"),
    cell_bounds=np.array([0.0, 31.0, 60.0], dtype="d"),
)
lat_id = cmor.axis(
    "latitude",
    "degrees_north",
    coord_vals=np.array([10.0, 20.0, 30.0], dtype="d"),
    cell_bounds=np.array([5.0, 15.0, 25.0, 35.0], dtype="d"),
)
basin_id = cmor.axis(
    "basin",
    "",
    coord_vals=np.array(
        [
            "atlantic_arctic_ocean",
            "indian_pacific_ocean",
            "global_ocean",
        ],
        dtype="U21",
    ),
)
variable_name = "htovgyre_tavg-u-hyb-sea"
var_id = cmor.variable(
    variable_name,
    "W",
    [time_id, basin_id, lat_id],
    missing_value=1.0e20,
)
compound_name = ".".join(["ocean"] + variable_name.split("_") + ["mon", "glb"])

with open(TABLES_PATH / "CMIP7_cell_measures.json") as handle:
    cell_measure = json.load(handle)["cell_measures"].get(compound_name)
if cell_measure:
    cmor.set_variable_attribute(var_id, "cell_measures", "c", cell_measure)

with open(TABLES_PATH / "CMIP7_long_name_overrides.json") as handle:
    long_name = json.load(handle)["long_name_overrides"].get(compound_name)
if long_name:
    cmor.set_variable_attribute(var_id, "long_name", "c", long_name)
data = np.array(
    [
        -80.0,
        -84.0,
        -88.0,
        -100.0,
        -104.0,
        -76.0,
        -120.0,
        -92.0,
        -96.0,
        -79.0,
        -83.0,
        -87.0,
        -99.0,
        -103.0,
        -75.0,
        -107.0,
        -111.0,
        -115.0,
    ],
    dtype="f4",
).reshape(2, 3, 3)
cmor.write(var_id, data)
path = cmor.close(var_id, file_name=True)
cmor.close()
print(path)
