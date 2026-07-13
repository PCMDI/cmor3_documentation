---
title: Python Examples
tags: [examples, python]
keywords: example, python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_python/
---

These examples are based on the CMOR repository's [examples/python](https://github.com/PCMDI/cmor/tree/main/examples/python) directory. They use one shared CMIP7 user input file and load CMIP7 tables from a local clone of [WCRP-CMIP/cmip7-cmor-tables](https://github.com/WCRP-CMIP/cmip7-cmor-tables).

Install CMOR with conda:

```bash
conda install -c conda-forge cmor
```

or with pip:

```bash
pip install cmor --extra-index-url https://pcmdi.github.io/cmor
```

Run the examples from a working directory that contains the `cmip7-cmor-tables` repository:

```bash
git clone https://github.com/WCRP-CMIP/cmip7-cmor-tables.git
python /path/to/example_01_usual_2d_field.py
```

The examples expect tables under `./cmip7-cmor-tables/tables`. To use a different location, set `CMOR_TABLES_PATH` to the directory containing the CMIP7 table JSON files.

Each example builds the CMIP7 compound variable name and uses it to read `CMIP7_cell_measures.json` and `CMIP7_long_name_overrides.json` before writing data.

### CMOR Input Files

* [CMIP7_input_example.json]({{site.baseurl}}/mydoc/examples/python/CMIP7_input_example.json){:target="_blank"}
* [CMIP7_coordinate.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_coordinate.json){:target="_blank"}
* [CMIP7_formula_terms.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_formula_terms.json){:target="_blank"}
* [CMIP7_cell_measures.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_cell_measures.json){:target="_blank"}
* [CMIP7_long_name_overrides.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_long_name_overrides.json){:target="_blank"}
* [cmor-cvs.json](https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables-cvs/cmor-cvs.json){:target="_blank"}

<details><summary markdown="span"><b>Click to expand shared JSON input</b></summary>

```json
{% include_relative examples/python/CMIP7_input_example.json %}
```

</details>

### Example 1: Usual Treatment of a 2-D Field

* [example_01_usual_2d_field.py]({{site.baseurl}}/mydoc/examples/python/example_01_usual_2d_field.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_01_usual_2d_field.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_01_usual_2d_field.cdl %}
```

</details>

### Example 2: Usual Treatment of a 3-D Field on Pressure Levels

* [example_02_pressure_levels.py]({{site.baseurl}}/mydoc/examples/python/example_02_pressure_levels.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_02_pressure_levels.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_02_pressure_levels.cdl %}
```

</details>

### Example 3: Treatment of a Scalar Dimension

* [example_03_scalar_dimension.py]({{site.baseurl}}/mydoc/examples/python/example_03_scalar_dimension.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_03_scalar_dimension.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_03_scalar_dimension.cdl %}
```

</details>

### Example 4: Treatment of Auxiliary Coordinates

* [example_04_auxiliary_coordinates.py]({{site.baseurl}}/mydoc/examples/python/example_04_auxiliary_coordinates.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_04_auxiliary_coordinates.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_04_auxiliary_coordinates.cdl %}
```

</details>

### Example 5: Treatment of a 3-D Field on Model Levels

* [example_05_model_levels.py]({{site.baseurl}}/mydoc/examples/python/example_05_model_levels.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_05_model_levels.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_05_model_levels.cdl %}
```

</details>

### Example 6: Treatment of Grid Coordinates

* [example_06_complex_grid.py]({{site.baseurl}}/mydoc/examples/python/example_06_complex_grid.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_06_complex_grid.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_06_complex_grid.cdl %}
```

</details>

### Example 7: Fixed Field

* [example_07_fixed_field.py]({{site.baseurl}}/mydoc/examples/python/example_07_fixed_field.py){:target="_blank"}

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
{% include_relative examples/python/example_07_fixed_field.py %}
```

</details>

<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```text
{% include_relative examples/python/example_07_fixed_field.cdl %}
```

</details>
