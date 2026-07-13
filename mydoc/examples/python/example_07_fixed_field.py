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

# Override 'frequency' from the user input
cmor.set_cur_dataset_attribute("frequency", "fx")
cmor.load_table("CMIP7_land.json")
lat_id = cmor.axis(
    "latitude",
    "degrees_north",
    coord_vals=np.array([10.0, 20.0, 30.0], dtype="d"),
    cell_bounds=np.array([5.0, 15.0, 25.0, 35.0], dtype="d"),
)
lon_id = cmor.axis(
    "longitude",
    "degrees_east",
    coord_vals=np.array([0.0, 90.0, 180.0, 270.0], dtype="d"),
    cell_bounds=np.array(
        [-45.0, 45.0, 135.0, 225.0, 315.0],
        dtype="d",
    ),
)
variable_name = "rootd_ti-u-hxy-lnd"
var_id = cmor.variable(
    variable_name,
    "m",
    [lat_id, lon_id],
    missing_value=1.0e20,
)
compound_name = ".".join(["land"] + variable_name.split("_") + ["fx", "glb"])

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
        [0.50, 0.45, 1.0e20, 0.55],
        [0.60, 0.60, 1.0e20, 0.55],
        [1.0e20, 0.45, 0.50, 0.50],
    ],
    dtype="f4",
)
cmor.write(var_id, data)
path = cmor.close(var_id, file_name=True)
cmor.close()
print(path)
