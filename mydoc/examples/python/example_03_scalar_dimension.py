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
cmor.load_table("CMIP7_atmos.json")
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
    cell_bounds=np.array([-45.0, 45.0, 135.0, 225.0, 315.0], dtype="d"),
)
time_id = cmor.axis(
    "time",
    "days since 1979-01-01",
    coord_vals=np.array([15.5, 45.5], dtype="d"),
    cell_bounds=np.array([0.0, 31.0, 60.0], dtype="d"),
)
height_id = cmor.axis(
    "height2m",
    "m",
    coord_vals=np.array([2.0], dtype="d"),
)
variable_name = "tas_tavg-h2m-hxy-u"
var_id = cmor.variable(
    variable_name,
    "K",
    [time_id, lat_id, lon_id, height_id],
    missing_value=1.0e20,
)
compound_name = ".".join(["atmos"] + variable_name.split("_") + ["mon", "glb"])

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
        254.0895,
        258.4085,
        250.5549,
        258.7101,
        258.6680,
        258.2990,
        252.1237,
        255.0432,
        253.7254,
        251.2460,
        254.3168,
        255.4808,
        259.7908,
        252.2754,
        257.1892,
        253.3132,
        253.8823,
        253.4698,
        253.5381,
        254.9730,
        256.1002,
        251.8168,
        259.3698,
        250.2994,
    ],
    dtype="f4",
).reshape(2, 3, 4, 1)
cmor.write(var_id, data)
path = cmor.close(var_id, file_name=True)
cmor.close()
print(path)
