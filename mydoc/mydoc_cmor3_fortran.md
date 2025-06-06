---
title: Fortran Example
tags: [examples, fortran]
keywords: example, Fortran
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_fortran/
---

### CMOR user input

* [CMOR_input_example.json](https://github.com/PCMDI/cmor/blob/main/Test/CMOR_input_example.json)

<details><summary markdown="span"><b>Click to expand json file</b></summary>

```json
{
  "#note":           "explanation of what source_type is goes here",
  "source_type":            "AOGCM ISM AER",

  "#note":                  "CMIP6 valid experiment_ids are found in CMIP6_CV.json",
  "experiment_id":          "piControl-withism",
  "activity_id":            "ISMIP6",
  "sub_experiment_id":      "none",

  "realization_index":      "3",
  "initialization_index":   "1",
  "physics_index":          "1",
  "forcing_index":          "1",

  "#note":                  "Text stored in attribute variant_info (recommended, not required description of run variant)",
  "run_variant":            "3rd realization",

  "parent_experiment_id":   "historical",
  "parent_activity_id":     "CMIP",
  "parent_source_id":       "PCMDI-test-1-0",
  "parent_variant_label":   "r3i1p1f1",

  "parent_time_units":      "days since 1850-01-01",
  "branch_method":          "standard",
  "branch_time_in_child":   59400.0,
  "branch_time_in_parent":  59400.0,

  "#note":                  "institution_id must be registered at https://github.com/WCRP-CMIP/CMIP6_CVs/issues/new ",
  "institution_id":         "PCMDI",

  "#note":                  "source_id (model name) must be registered at https://github.com/WCRP-CMIP/CMIP6_CVs/issues/new ",
  "source_id":              "PCMDI-test-1-0",

  "calendar":               "360_day",

  "grid":                   "native atmosphere regular grid (3x4 latxlon)",
  "grid_label":             "gn",
  "nominal_resolution":     "10000 km",

  "license":                 "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law.",

  "#output":                "Root directory for output (can be either a relative or full path)",
  "outpath":                "CMIP6",

  "#note":                  " **** The following descriptors are optional and may be set to an empty string ",  

  "contact ":               "Python Coder (coder@a.b.c.com)",
  "history":                "Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256.",
  "comment":                "",
  "references":             "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html.  The ssp245 simulation is described in Dorkey et al. '(Clim. Dyn., 2003, 323-357.)'",

  "#note":                  " **** The following will be obtained from the CV and do not need to be defined here", 

  "sub_experiment":         "none",
  "institution":            "",
  "source":                 "PCMDI-test 1.0 (1989)",

  "#note":                  " **** The following are set correctly for CMIP6 and should not normally need editing",  

  "_controlled_vocabulary_file": "CMIP6_CV.json",
  "_AXIS_ENTRY_FILE":         "CMIP6_coordinate.json",
  "_FORMULA_VAR_FILE":        "CMIP6_formula_terms.json",
  "_cmip6_option":           "CMIP6",

  "mip_era":                "CMIP6",
  "parent_mip_era":         "CMIP6",

  "tracking_prefix":        "hdl:21.14100",
  "_history_template":       "%s ;rewrote data to be consistent with <activity_id> for variable <variable_id> found in table <table_id>.",

  "#output_path_template":   "Template for output path directory using tables keys or global attributes, these should follow the relevant data reference syntax",
  "output_path_template":    "<mip_era><activity_id><institution_id><source_id><experiment_id><_member_id><table><variable_id><grid_label><version>",
  "output_file_template":    "<variable_id><table><source_id><experiment_id><_member_id><grid_label>",
}

```
</details>

### Fortran source code

* [ipcc_test_code.f90](https://github.com/PCMDI/cmor/blob/main/Test/ipcc_test_code.f90)
* [reader_2D_3D.f90](https://github.com/PCMDI/cmor/blob/main/Test/reader_2D_3D.f90)

<details><summary markdown="span"><b>Click to expand Fortran code</b></summary>

```fortran
!!$pgf90 -I/work/NetCDF/5.1/include -L/work/NetCDF/5.1/lib -l netcdf -L. -l cmor Test/test_dimensionless.f90 -IModules -o cmor_test
!!$pgf90 -g -I/pcmdi/charles_work/NetCDF/include -L/pcmdi/charles_work/NetCDF/lib -lnetcdf -module Modules -IModules -L. -lcmor -I/pcmdi/charles_work/Unidata/include -L/pcmdi/charles_work/Unidata/lib -ludunits Test/test_dimensionless.f90 -o cmor_test

MODULE local_subs

USE cmor_users_functions
PRIVATE
PUBLIC read_coords, read_time, read_3d_input_files, read_2d_input_files
CONTAINS

SUBROUTINE read_coords(alats, alons, plevs, bnds_lat, bnds_lon)

  IMPLICIT NONE
  
  DOUBLE PRECISION, INTENT(OUT), DIMENSION(:) :: alats
  DOUBLE PRECISION, INTENT(OUT), DIMENSION(:) :: alons
  DOUBLE PRECISION, INTENT(OUT), DIMENSION(:) :: plevs
  DOUBLE PRECISION, INTENT(OUT), DIMENSION(:,:) :: bnds_lat
  DOUBLE PRECISION, INTENT(OUT), DIMENSION(:,:) :: bnds_lon
  
  INTEGER :: i
  
  DO i = 1, SIZE(alons)
      alons(i) = (i-1)*360./SIZE(alons)
      bnds_lon(1,i) = (i - 1.5)*360./SIZE(alons)
      bnds_lon(2,i) = (i - 0.5)*360./SIZE(alons)
  END DO
  
  DO i = 1, SIZE(alats)
      alats(i) = (size(alats)+1-i)*10
      bnds_lat(1,i) = (size(alats)+1-i)*10 + 5.
      bnds_lat(2,i) = (size(alats)+1-i)*10 - 5.
  END DO

  DO i = 1, SIZE(plevs)
      plevs(i) = i*1.0e4
  END DO
    plevs = (/100000., 92500., 85000., 70000.,&
      60000., 50000., 40000., 30000., 25000., 20000.,&
      15000., 10000., 7000., 5000., 3000., 2000., 1000., 500., 100./)
  
  RETURN
END SUBROUTINE read_coords

SUBROUTINE read_time(it, time, time_bnds)
  
  IMPLICIT NONE
  
  INTEGER, INTENT(IN) :: it
  DOUBLE PRECISION, INTENT(OUT) :: time
  DOUBLE PRECISION, INTENT(OUT), DIMENSION(2,1) :: time_bnds
  
  time = (it-0.5)*30.
  time_bnds(1,1) = (it-1)*30.
  time_bnds(2,1) = it*30.
  
  RETURN
END SUBROUTINE read_time

INCLUDE "reader_2D_3D.f90"

END MODULE local_subs


PROGRAM ipcc_test_code
!
!   Purpose:   To serve as a generic example of an application that
!       uses the "Climate Model Output Rewriter" (CMOR)

!    CMOR writes CF-compliant netCDF files.
!    Its use is strongly encouraged by the IPCC and is intended for use 
!       by those participating in many community-coordinated standard 
!       climate model experiments (e.g., AMIP, CMIP, CFMIP, PMIP, APE,
!       etc.)
!
!   Background information for this sample code:
!
!      Atmospheric standard output requested by IPCC are listed in 
!   tables available on the web.  Monthly mean output is found in
!   tables A1a and A1c.  This sample code processes only two 3-d 
!   variables listed in table A1c ("monthly mean atmosphere 3-D data" 
!   and only four 2-d variables listed in table A1a ("monthly mean 
!   atmosphere + land surface 2-D (latitude, longitude) data").  The 
!   extension to many more fields is trivial.
!
!      For this example, the user must fill in the sections of code that 
!   extract the 3-d and 2-d fields from his monthly mean "history" 
!   files (which usually contain many variables but only a single time 
!   slice).  The CMOR code will write each field in a separate file, but 
!   many monthly mean time-samples will be stored together.  These 
!   constraints partially determine the structure of the code.
!
!
!   Record of revisions:

!       Date        Programmer(s)           Description of change
!       ====        ==========              =====================
!      10/22/03     Rusty Koder              Original code
!       1/28/04     Les R. Koder             Revised to be consistent
!                                            with evolving code design

! include module that contains the user-accessible cmor functions.
USE cmor_users_functions
USE local_subs

IMPLICIT NONE

!   dimension parameters:
! ---------------------------------
INTEGER, PARAMETER :: ntimes = 2    ! number of time samples to process
INTEGER, PARAMETER :: lon = 4       ! number of longitude grid cells  
INTEGER, PARAMETER :: lat = 3       ! number of latitude grid cells
INTEGER, PARAMETER :: lev = 5       ! number of standard pressure levels
INTEGER, PARAMETER :: lev2 = 19       ! number of standard pressure levels
INTEGER, PARAMETER :: n2d = 4       ! number of IPCC Table A1a fields to be
                                    !     output.
INTEGER, PARAMETER :: n3d = 3       ! number of IPCC Table A1c fields to 
                                    !     be output.  

!   Tables associating the user's variables with IPCC standard output 
!   variables.  The user may choose to make this association in a 
!   different way (e.g., by defining values of pointers that allow him 
!   to directly retrieve data from a data record containing many 
!   different variables), but in some way the user will need to map his 
!   model output onto the Tables specifying the MIP standard output.

! ----------------------------------

                              ! My variable names for IPCC Table A1c fields
CHARACTER (LEN=5), DIMENSION(n3d) :: &
                                varin3d=(/'CLOUD', 'U    ', 'T    '/)

                              ! Units appropriate to my data
CHARACTER (LEN=5), DIMENSION(n3d) :: &
                                units3d=(/ '%    ', 'm s-1',   'K    '  /)

                    ! Corresponding IPCC Table A1c entry (variable name) 
CHARACTER (LEN=2), DIMENSION(n3d) :: entry3d = (/ 'cl', 'ua', 'ta' /)

                              ! My variable names for IPCC Table A1a fields
CHARACTER (LEN=8), DIMENSION(n2d) :: &
                varin2d=(/ 'LATENT  ', 'TSURF   ', 'SOIL_WET', 'PSURF   ' /)

                              ! Units appropriate to my data
  CHARACTER (LEN=6), DIMENSION(n2d) :: &
                        units2d=(/ 'W m-2 ', 'K     ', 'kg m-2', 'Pa    ' /)

  CHARACTER (LEN=4), DIMENSION(n2d) :: &
                    positive2d= (/  'down',  '    ', '    ', '    '  /)

                    ! Corresponding IPCC Table A1a entry (variable name) 
CHARACTER (LEN=5), DIMENSION(n2d) :: &
                      entry2d = (/ 'hfls ', 'tas  ', 'mrsos', 'ps   ' /)

!  uninitialized variables used in communicating with CMOR:
!  ---------------------------------------------------------

INTEGER :: error_flag
INTEGER :: znondim_id, zfactor_id
INTEGER, DIMENSION(n2d) :: var2d_ids
INTEGER, DIMENSION(n3d) :: var3d_ids
REAL, DIMENSION(lon,lat) :: data2d
REAL, DIMENSION(lon,lat,lev2) :: data3d
DOUBLE PRECISION, DIMENSION(lat) :: alats
DOUBLE PRECISION, DIMENSION(lon) :: alons
DOUBLE PRECISION, DIMENSION(lev2) :: plevs
DOUBLE PRECISION, DIMENSION(1) :: time
DOUBLE PRECISION, DIMENSION(2,1):: bnds_time
DOUBLE PRECISION, DIMENSION(2,lat) :: bnds_lat
DOUBLE PRECISION, DIMENSION(2,lon) :: bnds_lon
DOUBLE PRECISION, DIMENSION(lev) :: zlevs
DOUBLE PRECISION, DIMENSION(lev+1) :: zlev_bnds
REAL, DIMENSION(lev) :: a_coeff
REAL, DIMENSION(lev) :: b_coeff
REAL :: p0
REAL, DIMENSION(lev+1) :: a_coeff_bnds
REAL, DIMENSION(lev+1) :: b_coeff_bnds
INTEGER :: ilon, ilat, ipres, ilev, itim, itim2, ilon2,ilat2
DOUBLE PRECISION bt

character(256)::  outpath,mycal

!  Other variables:
!  ---------------------

INTEGER :: it, m  
bt=0.
! ================================
!  Execution begins here:
! ================================

! Read coordinate information from model into arrays that will be passed 
!   to CMOR.
! Read latitude, longitude, and pressure coordinate values into 
!   alats, alons, and plevs, respectively.  Also generate latitude and 
!   longitude bounds, and store in bnds_lat and bnds_lon, respectively.
!   Note that all variable names in this code can be freely chosen by
!   the user.

!   The user must write the subroutine that fills the coordinate arrays 
!   and their bounds with actual data.  The following line is simply a
!   a place-holder for the user's code, which should replace it.

!  *** possible user-written call ***

call read_coords(alats, alons, plevs, bnds_lat, bnds_lon)

! Specify path where tables can be found and indicate that existing 
!    netCDF files should not be overwritten.

error_flag = cmor_setup(inpath='Test', netcdf_file_action='replace')

! Define dataset as output from the GICC model (first member of an
!   ensemble of simulations) run under IPCC 2xCO2 equilibrium
!   experiment conditions, and provide information to be included as 
!   attributes in all CF-netCDF files written as part of this dataset.

mycal = '360_day'

error_flag = cmor_dataset_json("Test/CMOR_input_example.json")


!  Define all axes that will be needed

ilat = cmor_axis(  &
      table='Tables/CMIP6_Amon.json',    &
      table_entry='latitude',       &
      units='degrees_north',        &  
      length=lat,                   &
      coord_vals=alats,             & 
      cell_bounds=bnds_lat)        
    
ilon2 = cmor_axis(  &
      table='Tables/CMIP6_Lmon.json',    &
      table_entry='longitude',      &
      length=lon,                   &
      units='degrees_east',         &
      coord_vals=alons,             &
      cell_bounds=bnds_lon)      
      
ilat2 = cmor_axis(  &
      table='Tables/CMIP6_Lmon.json',    &
      table_entry='latitude',       &
      units='degrees_north',        &  
      length=lat,                   &
      coord_vals=alats,             & 
      cell_bounds=bnds_lat)        
    
ilon = cmor_axis(  &
      table='Tables/CMIP6_Amon.json',    &
      table_entry='longitude',      &
      length=lon,                   &
      units='degrees_east',         &
      coord_vals=alons,             &
      cell_bounds=bnds_lon)      
      
ipres = cmor_axis(  &
      table='Tables/CMIP6_Amon.json',    &
      table_entry='plev19',       &
      units='Pa',                   &
      length=lev2,                   &
      coord_vals=plevs)

!   note that the time axis is defined next, but the time coordinate 
!   values and bounds will be passed to cmor through function 
!   cmor_write (later, below).

itim = cmor_axis(  &
      table='Tables/CMIP6_Amon.json',    &
      table_entry='time',           &
      units='days since 2030-1-1',  &
      length=ntimes,                &
      interval='20 minutes')
itim2 = cmor_axis(  &
      table='Tables/CMIP6_Lmon.json',    &
      table_entry='time',           &
      units='days since 2030-1-1',  &
      length=ntimes,                &
      interval='20 minutes')

!  define model eta levels (although these must be provided, they will
!    actually be replaced by a+b before writing the netCDF file)
zlevs = (/ 0.1, 0.3, 0.55, 0.7, 0.9 /)
zlev_bnds=(/ 0.,.2, .42, .62, .8, 1. /)

ilev = cmor_axis(  &
      table='Tables/CMIP6_Amon.json',    &
      table_entry='standard_hybrid_sigma',       &
      units='1', &
      length=lev,                   &
      coord_vals=zlevs,             &
      cell_bounds=zlev_bnds)

!   define z-factors needed to transform from model level to pressure
p0 = 1.e5
a_coeff = (/ 0.1, 0.2, 0.3, 0.22, 0.1 /)
b_coeff = (/ 0.0, 0.1, 0.2, 0.5, 0.8 /)

a_coeff_bnds=(/0.,.15, .25, .25, .16, 0./)
b_coeff_bnds=(/0.,.05, .15, .35, .65, 1./)

error_flag = cmor_zfactor(  &
      zaxis_id=ilev,                      &
      zfactor_name='p0',                  &
      units='Pa',                         &
      zfactor_values = p0)

error_flag = cmor_zfactor(  &
      zaxis_id=ilev,                       & 
      zfactor_name='b',                    &
      axis_ids= (/ ilev /),                &
      zfactor_values = b_coeff,            &
      zfactor_bounds = b_coeff_bnds  )

error_flag = cmor_zfactor(  &
      zaxis_id=ilev,                       &
      zfactor_name='a',                    &
      axis_ids= (/ ilev /),                &
      zfactor_values = a_coeff,            &
      zfactor_bounds = a_coeff_bnds )

zfactor_id = cmor_zfactor(  &
      zaxis_id=ilev,                         &
      zfactor_name='ps',                     &
      axis_ids=(/ ilon, ilat, itim /),       &
      units='Pa' )

!  Define the only field to be written that is a function of model level
!    (appearing in IPCC table A1c)

var3d_ids(1) = cmor_variable(    &
      table='Tables/CMIP6_Amon.json',  &
      table_entry=entry3d(1),     &
      units=units3d(1),           &
      axis_ids=(/ ilon, ilat, ilev, itim /),  &
      missing_value=1.0e28, &
      original_name=varin3d(1))

!  Define variables appearing in IPCC table A1c that are a function of pressure
!         (3-d variables)

DO m=2,n3d
    var3d_ids(m) = cmor_variable(    &
        table='Tables/CMIP6_Amon.json',  &
        table_entry=entry3d(m),     &
        units=units3d(m),           &
        axis_ids=(/ ilon, ilat, ipres, itim /), &
        missing_value=1.0e28,       &
        original_name=varin3d(m))
ENDDO


!  Define variables appearing in IPCC table A1a (2-d variables)

DO m=1,n2d
    if (m.ne.3) then
    var2d_ids(m) = cmor_variable(    &
        table='Tables/CMIP6_Amon.json',      &
        table_entry=entry2d(m),     & 
        units=units2d(m),           & 
        axis_ids=(/ ilon, ilat, itim /), &
        missing_value=1.0e28,       &
        positive=positive2d(m),     &
        original_name=varin2d(m))   
else
    var2d_ids(m) = cmor_variable(    &
        table='Tables/CMIP6_Lmon.json',      &
        table_entry=entry2d(m),     & 
        units=units2d(m),           & 
        axis_ids=(/ ilon2, ilat2, itim2 /), &
        missing_value=1.0e28,       &
        positive=positive2d(m),     &
        original_name=varin2d(m)) 
endif
ENDDO

PRINT*, ' '
PRINT*, 'completed everything up to writing output fields '
PRINT*, ' '

!  Loop through history files (each containing several different fields, 
!       but only a single month of data, averaged over the month).  Then 
!       extract fields of interest and write these to netCDF files (with 
!       one field per file, but all months included in the loop).

time_loop: DO it=1, ntimes
    
    ! In the following loops over the 3d and 2d fields, the user-written    
    ! subroutines (read_3d_input_files and read_2d_input_files) retrieve 
    ! the requested IPCC table A1c and table A1a fields and store them in 
    ! data3d and data2d, respectively.  In addition a user-written code 
    ! (read_time) retrieves the time and time-bounds associated with the 
    ! time sample (in units of 'days since 1970-1-1', consistent with the 
    ! axis definitions above).  The bounds are set to the beginning and 
    ! the end of the month retrieved, indicating the averaging period.
    
    ! The user must write a code to obtain the times and time-bounds for
    !   the time slice.  The following line is simply a place-holder for
    !   the user's code, which should replace it.
    
  call read_time(it, time(1), bnds_time)

  call read_3d_input_files(it, varin3d(1), data3d)

  error_flag = cmor_write(                                  &
        var_id        = var3d_ids(1),                        &
        data          = data3d,                              &
        ntimes_passed = 1,                                   &
        time_vals     = time,                                &
        time_bnds     = bnds_time   )

  call read_2d_input_files(it, varin2d(4), data2d)                  

  error_flag = cmor_write(                                  &
        var_id        = zfactor_id,                          &
        data          = data2d,                              &
        ntimes_passed = 1,                                   &
        time_vals     = time,                                &
        time_bnds     = bnds_time,                           &
        store_with    = var3d_ids(1) )

  ! Cycle through the 3-d fields (stored on pressure levels), 
  ! and retrieve the requested variable and append each to the 
  ! appropriate netCDF file.

  DO m=2,n3d
      
      ! The user must write the code that fills the arrays of data
      ! that will be passed to CMOR.  The following line is simply a
      ! a place-holder for the user's code, which should replace it.

      call read_3d_input_files(it, varin3d(m), data3d)
      
      ! append a single time sample of data for a single field to 
      ! the appropriate netCDF file.
      error_flag = cmor_write(                                  &
            var_id        = var3d_ids(m),                        &
            data          = data3d,                              &
            ntimes_passed = 1,                                   &
            time_vals     = time,                                &
            time_bnds     = bnds_time  )
      
      IF (error_flag < 0) THEN
          ! write diagnostic messages to standard output device
          write(*,*) ' Error encountered writing IPCC Table A1c ' &
              // 'field ', entry3d(m), ', which I call ', varin3d(m)
          write(*,*) ' Was processing time sample: ', time
                    
      END IF

    END DO
    
    ! Cycle through the 2-d fields, retrieve the requested variable and 
    ! append each to the appropriate netCDF file.
    
    DO m=1,n2d
      
      ! The user must write the code that fills the arrays of data
      ! that will be passed to CMOR.  The following line is simply a
      ! a place-holder for the user's code, which should replace it.
      
      call read_2d_input_files(it, varin2d(m), data2d)                  

      ! append a single time sample of data for a single field to 
      ! the appropriate netCDF file.

      error_flag = cmor_write(                                  &
            var_id        = var2d_ids(m),                        &
            data          = data2d,                              &
            ntimes_passed = 1,                                   &
            time_vals     = time,                                &
            time_bnds     = bnds_time  )
      
      IF (error_flag < 0) THEN
          ! write diagnostic messages to standard output device
          write(*,*) ' Error encountered writing IPCC Table A1a ' &
              // 'field ', entry2d(m), ', which I call ', varin2d(m)
          write(*,*) ' Was processing time sample: ', time 
                    
      END IF
      
    END DO
    
END DO time_loop

!   Close all files opened by CMOR.

error_flag = cmor_close()  

print*, ' '
print*, '******************************'
print*, ' '
print*, 'ipcc_test_code executed to completion '   
print*, ' '
print*, '******************************'

END PROGRAM ipcc_test_code

```

</details>