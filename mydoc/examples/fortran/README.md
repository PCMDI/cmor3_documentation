# Fortran examples

## Setup

To run the examples, you need a Conda or Mamba environment with CMOR and a
Fortran compiler installed.

```bash
mamba create -n cmor-fortran -c conda-forge cmor fortran-compiler udunits2
mamba activate cmor-fortran
```

The examples also need the CMIP7 tables. Clone the tables into the directory
where you run `run_examples.sh`.

```bash
git clone https://github.com/WCRP-CMIP/cmip7-cmor-tables.git
```

The runner expects tables under `./cmip7-cmor-tables/tables` and uses the
shared CMIP7 user input JSON from `../CMIP7_input_example.json`.

## Run

To compile and run all of the examples from this directory, run the following.

```bash
./run_examples.sh
```

Generated NetCDF files are written under `./output`.

You can also run the examples without activating the environment first.

```bash
conda run -n cmor-fortran ./run_examples.sh
```

## Environment variables

The script uses the active Conda environment by default. It expects CMOR under
`$CONDA_PREFIX`, reads the Fortran module from `$CONDA_PREFIX/include`, links
against libraries in `$CONDA_PREFIX/lib`, and prefers a `gfortran` executable
installed in the environment.

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

Use `CMOR_MOD_DIR` or `CMOR_LIB` when the module file or library is not under
the standard `include` and `lib` directories for the prefix.

```bash
CMOR_MOD_DIR=/path/to/include CMOR_LIB=/path/to/libcmor.a ./run_examples.sh
```

Use `FC`, `FFLAGS`, and `EXTRA_LDFLAGS` to override the compiler, compiler
flags, or linker flags.

```bash
FC=/path/to/gfortran \
FFLAGS="-g -O0 -ffree-line-length-none" \
EXTRA_LDFLAGS="-L/path/to/lib -Wl,-rpath,/path/to/lib" \
./run_examples.sh ./output
```

Use `BUILD_DIR` to override where executables and Fortran module outputs are
written.
