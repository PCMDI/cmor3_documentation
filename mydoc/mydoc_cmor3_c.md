---
title: C Examples
tags: [examples, c, cmip7]
keywords: example, C, cmip7
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_c/
---

These examples are based on the CMOR repository's [examples/c](https://github.com/PCMDI/cmor/tree/c_examples/examples/c){:target="_blank"} directory. They use the same shared CMIP7 user input file as the Python and Fortran examples and load CMIP7 tables from a local clone of [WCRP-CMIP/cmip7-cmor-tables](https://github.com/WCRP-CMIP/cmip7-cmor-tables){:target="_blank"}.

Create and activate a Conda or Mamba environment with CMOR and a C compiler:

```bash
mamba create -n cmor-c -c conda-forge cmor c-compiler libnetcdf udunits2 json-c libuuid
mamba activate cmor-c
```

If you use Conda instead of Mamba, use the same package list:

```bash
conda create -n cmor-c -c conda-forge cmor c-compiler libnetcdf udunits2 json-c libuuid
conda activate cmor-c
```

Install the CMIP7 tables in the working directory where you will run the examples:

```bash
git clone https://github.com/WCRP-CMIP/cmip7-cmor-tables.git
```

Run the examples from a working directory that contains the `cmip7-cmor-tables` repository using the [run_examples.sh]({{site.baseurl}}/mydoc/examples/c/run_examples.sh){:target="_blank"} script:

```bash
chmod a+x run_examples.sh
./run_examples.sh
```

The examples expect tables under `./cmip7-cmor-tables/tables` in the directory where you run the script. To use a different table location, set `CMOR_TABLES_PATH` to the directory containing the CMIP7 table JSON files. To use a different user input file, set `CMOR_INPUT_PATH`.

Each example builds the CMIP7 compound variable name and uses it to read `CMIP7_cell_measures.json` and `CMIP7_long_name_overrides.json` before writing data. The fixed-field example overrides `frequency` from the shared user input file to `fx`.

### CMOR Input Files

* [CMIP7_input_example.json]({{site.baseurl}}/mydoc/examples/CMIP7_input_example.json){:target="_blank"}
* [CMIP7_coordinate.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_coordinate.json){:target="_blank"}
* [CMIP7_formula_terms.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_formula_terms.json){:target="_blank"}
* [CMIP7_cell_measures.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_cell_measures.json){:target="_blank"}
* [CMIP7_long_name_overrides.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_long_name_overrides.json){:target="_blank"}
* [cmor-cvs.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables-cvs/cmor-cvs.json){:target="_blank"}

<details><summary markdown="span"><b>Click to expand shared JSON input</b></summary>

```json
{% include_relative examples/CMIP7_input_example.json %}
```

</details>

### Common C Utilities

* [cmip7_c_common.h]({{site.baseurl}}/mydoc/examples/c/cmip7_c_common.h){:target="_blank"}
* [cmip7_c_common.c]({{site.baseurl}}/mydoc/examples/c/cmip7_c_common.c){:target="_blank"}
* [run_examples.sh]({{site.baseurl}}/mydoc/examples/c/run_examples.sh){:target="_blank"}

<details><summary markdown="span"><b>Click to expand common C header</b></summary>

```c
{% include_relative examples/c/cmip7_c_common.h %}
```

</details>

<details><summary markdown="span"><b>Click to expand common C code</b></summary>

```c
{% include_relative examples/c/cmip7_c_common.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand runner script</b></summary>

```bash
{% include_relative examples/c/run_examples.sh %}
```

</details>

### Example 1: Regular Grid Ocean Field

* [example_01_regular_grid_tos.c]({{site.baseurl}}/mydoc/examples/c/example_01_regular_grid_tos.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_01_regular_grid_tos.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_01_regular_grid_tos.cdl %}
```

</details>

### Example 2: 3-D Field on Pressure Levels

* [example_02_pressure_levels.c]({{site.baseurl}}/mydoc/examples/c/example_02_pressure_levels.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_02_pressure_levels.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_02_pressure_levels.cdl %}
```

</details>

### Example 3: Scalar Height Coordinate

* [example_03_scalar_height_tas.c]({{site.baseurl}}/mydoc/examples/c/example_03_scalar_height_tas.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_03_scalar_height_tas.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_03_scalar_height_tas.cdl %}
```

</details>

### Example 4: Basin Axis

* [example_04_basin_axis.c]({{site.baseurl}}/mydoc/examples/c/example_04_basin_axis.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_04_basin_axis.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_04_basin_axis.cdl %}
```

</details>

### Example 5: Hybrid Sigma Model Levels

* [example_05_hybrid_sigma_levels.c]({{site.baseurl}}/mydoc/examples/c/example_05_hybrid_sigma_levels.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_05_hybrid_sigma_levels.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_05_hybrid_sigma_levels.cdl %}
```

</details>

### Example 6: Curvilinear Grid

* [example_06_curvilinear_grid.c]({{site.baseurl}}/mydoc/examples/c/example_06_curvilinear_grid.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_06_curvilinear_grid.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_06_curvilinear_grid.cdl %}
```

</details>

### Example 7: Fixed Field

* [example_07_fixed_field_rootd.c]({{site.baseurl}}/mydoc/examples/c/example_07_fixed_field_rootd.c){:target="_blank"}

<details><summary markdown="span"><b>Click to expand C code</b></summary>

```c
{% include_relative examples/c/example_07_fixed_field_rootd.c %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/c/example_07_fixed_field_rootd.cdl %}
```

</details>
