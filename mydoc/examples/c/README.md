# C examples

These examples mirror the CMIP7 Python and Fortran examples with the CMOR C
API. They write small synthetic fields for regular grids, pressure levels,
scalar coordinates, basin coordinates, hybrid-sigma model levels,
curvilinear grids, and fixed fields.

## Setup

Create a Conda or Mamba environment with CMOR, a C compiler, and the CMOR link
dependencies.

```bash
mamba create -n cmor-c -c conda-forge cmor c-compiler libnetcdf udunits2 json-c libuuid
mamba activate cmor-c
```

The equivalent Conda command is:

```bash
conda create -n cmor-c -c conda-forge cmor c-compiler libnetcdf udunits2 json-c libuuid
conda activate cmor-c
```

## CMIP7 tables

The examples also need the CMIP7 tables. Clone the tables into the directory
where you run `run_examples.sh`.

```bash
git clone https://github.com/WCRP-CMIP/cmip7-cmor-tables.git
```

## Run

To compile and run all examples, run:

```bash
./run_examples.sh
```

You can also run the examples without activating the environment first.

```bash
conda run -n cmor-c ./run_examples.sh
```

Generated NetCDF files are written under `./output`.

## Environment variables

The script uses the active Conda environment by default. It expects CMOR under
`$CONDA_PREFIX`, reads `cmor.h` from `$CONDA_PREFIX/include`, reads CMOR's
cdTime headers from `$CONDA_PREFIX/include/cdTime`, links against libraries in
`$CONDA_PREFIX/lib`, and prefers a C compiler installed in the environment.

Use `CMOR_TABLES_PATH` when the CMIP7 tables are not under
`./cmip7-cmor-tables/tables`.

```bash
CMOR_TABLES_PATH=/path/to/cmip7-cmor-tables/tables ./run_examples.sh
```

Use `CMOR_INPUT_PATH` to use a different CMIP7 user input JSON file.

```bash
CMOR_INPUT_PATH=/path/to/CMIP7_input_example.json ./run_examples.sh
```

Use `CMOR_PREFIX` when CMOR is installed under a different prefix.

```bash
CMOR_PREFIX=/path/to/cmor ./run_examples.sh
```

Use `CMOR_INCLUDE_DIR`, `CMOR_CDTIME_INCLUDE_DIR`, or `CMOR_LIB` when the
headers or library are not under the standard `include` and `lib` directories
for the prefix.

```bash
CMOR_INCLUDE_DIR=/path/to/include \
CMOR_CDTIME_INCLUDE_DIR=/path/to/include/cdTime \
CMOR_LIB=/path/to/libcmor.a \
./run_examples.sh
```

Use `CC`, `CFLAGS`, and `EXTRA_LDFLAGS` to override the compiler, compiler
flags, or linker flags.

```bash
CC=/path/to/cc \
CFLAGS="-g -O0 -Wall -Wextra" \
EXTRA_LDFLAGS="-L/path/to/lib -Wl,-rpath,/path/to/lib" \
./run_examples.sh
```

Use `BUILD_DIR` to override where executables are written.
