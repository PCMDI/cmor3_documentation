# Python examples

## Setup

Install CMOR to your Python environment.

```bash
pip install cmor --extra-index-url https://pcmdi.github.io/cmor
```

## CMIP7 tables

The examples also need the CMIP7 tables. Clone the tables into the directory
where you run the examples.

```bash
git clone https://github.com/WCRP-CMIP/cmip7-cmor-tables.git
```

## Run

Run one of the Python files in this directory from a working directory that
contains the `cmip7-cmor-tables` repository.

```bash
python example_01_usual_2d_field.py 
```

The examples expect tables under `./cmip7-cmor-tables/tables` and use the
shared CMIP7 user input JSON from `../CMIP7_input_example.json`.

Use `CMOR_TABLES_PATH` when the CMIP7 tables are not under
`./cmip7-cmor-tables/tables`.

```bash
CMOR_TABLES_PATH=/path/to/cmip7-cmor-tables/tables python example_01_usual_2d_field.py
```

Use `--output-dir` to write generated NetCDF files somewhere other than
`./output`.
