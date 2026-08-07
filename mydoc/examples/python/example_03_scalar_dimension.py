#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import cmor
import numpy as np

EXAMPLE_DIR = Path(__file__).resolve().parent
RUN_DIR = Path.cwd()
DEFAULT_TABLES_PATH = RUN_DIR / "cmip7-cmor-tables" / "tables"
TABLES_PATH = Path(os.environ.get("CMOR_TABLES_PATH", DEFAULT_TABLES_PATH))
INPUT_PATH = EXAMPLE_DIR.parent / "CMIP7_input_example.json"


def configure(
    output_dir: Path,
    frequency: str = "mon",
    realization_index: str = "r1",
    forcing_index: str = "f1",
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    user_input = json.loads(INPUT_PATH.read_text())
    user_input["outpath"] = str(output_dir)
    user_input["frequency"] = frequency
    user_input["realization_index"] = realization_index
    user_input["forcing_index"] = forcing_index
    input_path = output_dir / "CMIP7_input_example.json"
    input_path.write_text(json.dumps(user_input, indent=2, sort_keys=True))
    cmor.setup(inpath=str(TABLES_PATH), netcdf_file_action=cmor.CMOR_REPLACE)
    cmor.dataset_json(str(input_path))


def apply_cmip7_variable_metadata(
    var_id: int,
    realm: str,
    table_entry: str,
    frequency: str,
    region: str,
) -> str:
    compound_name = ".".join(
        [realm] + table_entry.split("_") + [frequency, region]
    )

    with (TABLES_PATH / "CMIP7_cell_measures.json").open() as handle:
        cell_measures = json.load(handle)["cell_measures"]
    cmor.set_variable_attribute(
        var_id,
        "cell_measures",
        "c",
        cell_measures.get(compound_name, ""),
    )

    with (TABLES_PATH / "CMIP7_long_name_overrides.json").open() as handle:
        long_name_overrides = json.load(handle)["long_name_overrides"]
    if compound_name in long_name_overrides:
        cmor.set_variable_attribute(
            var_id,
            "long_name",
            "c",
            long_name_overrides[compound_name],
        )

    return compound_name


def write_example(output_dir: Path) -> str:
    configure(output_dir, realization_index="r9", forcing_index="f2")
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
    var_id = cmor.variable(
        "tas_tavg-h2m-hxy-u",
        "K",
        [time_id, lat_id, lon_id, height_id],
        missing_value=1.0e20,
    )
    apply_cmip7_variable_metadata(
        var_id,
        "atmos",
        "tas_tavg-h2m-hxy-u",
        "mon",
        "glb",
    )
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
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write CMIP7 example 3 with CMOR."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "output",
    )
    args = parser.parse_args()
    print(write_example(args.output_dir))


if __name__ == "__main__":
    main()
