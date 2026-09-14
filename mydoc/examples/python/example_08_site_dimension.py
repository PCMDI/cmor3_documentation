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
    configure(output_dir)
    cmor.load_table("CMIP7_atmos.json")

    time_id = cmor.axis(
        "time1",
        "days since 1979-01-01",
        coord_vals=np.array([15.5, 45.5], dtype="d"),
        cell_bounds=np.array([0.0, 31.0, 60.0], dtype="d"),
    )
    site_values = np.arange(1, 127, dtype="i")
    site_id = cmor.axis("site", "1", coord_vals=site_values)
    height_id = cmor.axis(
        "height2m",
        "m",
        coord_vals=np.array([2.0], dtype="d"),
    )

    cmor.load_table("CMIP7_grids.json")
    site_latitudes = np.linspace(-60.0, 60.0, site_values.size, dtype="f")
    site_longitudes = np.linspace(0.5, 359.5, site_values.size, dtype="f")
    site_grid_id = cmor.grid(
        [site_id],
        latitude=site_latitudes,
        longitude=site_longitudes,
        latitude_vertices=np.column_stack(
            (site_latitudes - 0.25, site_latitudes + 0.25)
        ),
        longitude_vertices=np.column_stack(
            (site_longitudes - 0.25, site_longitudes + 0.25)
        ),
    )

    cmor.load_table("CMIP7_atmos.json")
    var_id = cmor.variable(
        "tas_tpt-h2m-hs-u",
        "K",
        [height_id, time_id, site_grid_id],
        missing_value=1.0e20,
    )
    apply_cmip7_variable_metadata(
        var_id,
        "atmos",
        "tas_tpt-h2m-hs-u",
        "mon",
        "glb",
    )

    data = np.linspace(
        275.0,
        290.0,
        2 * site_values.size,
        dtype="f4",
    ).reshape(1, 2, site_values.size)
    cmor.write(var_id, data)
    path = cmor.close(var_id, file_name=True)
    cmor.close()
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write CMIP7 example 8 with CMOR."
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
