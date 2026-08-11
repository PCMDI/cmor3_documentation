---
title: Fortran Examples
tags: [examples, fortran, cmip7]
keywords: example, Fortran, cmip7
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_fortran/
---

These examples are based on the CMOR repository's [examples/fortran](https://github.com/PCMDI/cmor/tree/main/examples/fortran){:target="_blank"} directory. They use the same shared CMIP7 user input file as the Python examples and load CMIP7 tables from a local clone of [WCRP-CMIP/cmip7-cmor-tables](https://github.com/WCRP-CMIP/cmip7-cmor-tables){:target="_blank"}.

Create and activate a Conda or Mamba environment with CMOR and a Fortran compiler:

```bash
mamba create -n cmor-fortran -c conda-forge cmor fortran-compiler udunits2
mamba activate cmor-fortran
```

If you use Conda instead of Mamba, use the same package list:

```bash
conda create -n cmor-fortran -c conda-forge cmor fortran-compiler udunits2
conda activate cmor-fortran
```

Install the CMIP7 tables in the working directory where you will run the examples:

```bash
git clone https://github.com/WCRP-CMIP/cmip7-cmor-tables.git
```

Run the examples from a working directory that contains the `cmip7-cmor-tables` repository using the [run_examples.sh]({{site.baseurl}}/mydoc/examples/fortran/run_examples.sh){:target="_blank"} script:

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

### Common Fortran Utilities

* [cmip7_fortran_common.f90]({{site.baseurl}}/mydoc/examples/fortran/cmip7_fortran_common.f90){:target="_blank"}
* [run_examples.sh]({{site.baseurl}}/mydoc/examples/fortran/run_examples.sh){:target="_blank"}

<details><summary markdown="span"><b>Click to expand common Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/cmip7_fortran_common.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand runner script</b></summary>

```bash
{% include_relative examples/fortran/run_examples.sh %}
```

</details>

### Example 1: Regular Grid Ocean Field

* [example_01_regular_grid_tos.f90]({{site.baseurl}}/mydoc/examples/fortran/example_01_regular_grid_tos.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_01_regular_grid_tos.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_01_regular_grid_tos.cdl %}
```

</details>

### Example 2: 3-D Field on Pressure Levels

* [example_02_pressure_levels.f90]({{site.baseurl}}/mydoc/examples/fortran/example_02_pressure_levels.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_02_pressure_levels.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_02_pressure_levels.cdl %}
```

</details>

### Example 3: Scalar Height Coordinate

* [example_03_scalar_height_tas.f90]({{site.baseurl}}/mydoc/examples/fortran/example_03_scalar_height_tas.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_03_scalar_height_tas.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_03_scalar_height_tas.cdl %}
```

</details>

### Example 4: Basin Axis

* [example_04_basin_axis.f90]({{site.baseurl}}/mydoc/examples/fortran/example_04_basin_axis.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_04_basin_axis.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_04_basin_axis.cdl %}
```

</details>

### Example 5: Hybrid Sigma Model Levels

* [example_05_hybrid_sigma_levels.f90]({{site.baseurl}}/mydoc/examples/fortran/example_05_hybrid_sigma_levels.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_05_hybrid_sigma_levels.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_05_hybrid_sigma_levels.cdl %}
```

</details>

### Example 6: Curvilinear Grid

* [example_06_curvilinear_grid.f90]({{site.baseurl}}/mydoc/examples/fortran/example_06_curvilinear_grid.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_06_curvilinear_grid.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_06_curvilinear_grid.cdl %}
```

</details>

### Example 7: Fixed Field

* [example_07_fixed_field_rootd.f90]({{site.baseurl}}/mydoc/examples/fortran/example_07_fixed_field_rootd.f90){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
{% include_relative examples/fortran/example_07_fixed_field_rootd.f90 %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/fortran/example_07_fixed_field_rootd.cdl %}
```

</details>
