---
title: Example Python
tags: [examples,  python]
keywords: example, python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_python/
---
### CMOR Input Files


* [CMOR_input_example.json](https://github.com/PCMDI/cmor/blob/main/Test/CMOR_input_example.json)
* [CMIP6_coordinate.json](https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_coordinate.json)
* [CMIP6_formula_terms.json](https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_formula_terms.json)
* [CMIP6_CV.json](https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_CV.json)
* [CMIP6_Amon.json](https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_Amon.json)
* [CMIP6_Omon.json](https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_Omon.json)


### Example 1: Python source code

* [test_doc.py](https://github.com/PCMDI/cmor/blob/main/Test/test_doc.py)

<details><summary markdown="span"><b>Click to expand Python code</b>
</summary>

```python
import cmor

cmor.setup(
	# inpath has to point to the CMOR 
	# tables path (CMIP6, input4MIPs or otherwise)
	inpath='Tables',  
	netcdf_file_action=cmor.CMOR_REPLACE_4
)

cmor.dataset_json("Test/CMOR_input_example.json")    
  
# Loading this test table overwrites the normal CF checks on valid variable values.
# This is perfect for testing but shouldn't be done when writing real data.
table='CMIP6_Amon.json'
cmor.load_table(table)


# here is where you add your axes
itime = cmor.axis(table_entry= 'time',
                  units= 'days since 2000-01-01 00:00:00',
                  coord_vals= [15,],
                  cell_bounds= [0, 30])
ilat = cmor.axis(table_entry= 'latitude',
                 units= 'degrees_north',
                 coord_vals= [0],
                 cell_bounds= [-1, 1])
ilon = cmor.axis(table_entry= 'longitude',
                 units= 'degrees_east',
                 coord_vals= [90],
                 cell_bounds= [89, 91])

axis_ids = [itime,ilat,ilon]
              
# here we create a variable with appropriate name, units and axes
varid = cmor.variable('ts', 'K', axis_ids)

# then we can write the variable along with the data
cmor.write(varid, [273])

# finally we close the file and print where it was saved
outfile = cmor.close(varid, file_name=True)
print("File written to: {}".format(outfile))
cmor.close()


```
</details>

### Example 2: Usual Treatment of a 2-D Field

* [example2.py](/mydoc/examples/example2.py)

<details><summary markdown="span"><b>click to expand Python code</b></summary>

```python
import cmor
import numpy
import os

hfls = numpy.array([120, 116, 112, 108,
                    104, 100, 96, 92,
                    88, 84, 80, 76,
                    119, 115, 111, 107,
                    103, 99, 95, 91,
                    87, 83, 79, 75
                    ])
hfls.shape = (2, 3, 4)
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])
lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])
time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])
ipth = opth = 'test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.cmor_normal,
           netcdf_file_action=cmor.cmor_replace)
cmor.dataset_json("cmor_input_example.json")
cmor.load_table("cmip6_amon.json")
cmorlat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorlon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmortime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
axes = [cmortime, cmorlat, cmorlon]
cmorhfls = cmor.variable("hfls", "w/m2", axes, positive="up")
cmor.write(cmorhfls, hfls)
filename = cmor.close(cmorhfls, file_name=true)
print("stored in:", filename)
cmor.close()
```

</details>
<details><summary markdown="span"><b>click to expand netcdf dump</b></summary>

```
netcdf hfls_amon_pcmdi-test-1-0_picontrol-withism_r3i1p1f1_gn_201801-201802 {
dimensions:
	time = unlimited ; // (2 currently)
	lat = 3 ;
	lon = 4 ;
	bnds = 2 ;
variables:
	double time(time) ;
		time:bounds = "time_bnds" ;
		time:units = "days since 2018" ;
		time:calendar = "360_day" ;
		time:axis = "t" ;
		time:long_name = "time" ;
		time:standard_name = "time" ;
	double time_bnds(time, bnds) ;
	double lat(lat) ;
		lat:bounds = "lat_bnds" ;
		lat:units = "degrees_north" ;
		lat:axis = "y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
	double lat_bnds(lat, bnds) ;
	double lon(lon) ;
		lon:bounds = "lon_bnds" ;
		lon:units = "degrees_east" ;
		lon:axis = "x" ;
		lon:long_name = "longitude" ;
		lon:standard_name = "longitude" ;
	double lon_bnds(lon, bnds) ;
	float hfls(time, lat, lon) ;
		hfls:standard_name = "surface_upward_latent_heat_flux" ;
		hfls:long_name = "surface upward latent heat flux" ;
		hfls:comment = "the surface called \'surface\' means the lower boundary of the atmosphere. \'upward\' indicates a vector component which is positive when directed upward (negative downward). the surface latent heat flux is the exchange of heat between the surface and the air on account of evaporation (including sublimation). in accordance with common usage in geophysical disciplines, \'flux\' implies per unit area, called \'flux density\' in physics." ;
		hfls:units = "w m-2" ;
		hfls:original_units = "w/m2" ;
		hfls:history = "2019-01-08t23:32:26z altered by cmor: converted units from \'w/m2\' to \'w m-2\'. 2019-01-08t23:32:26z altered by cmor: converted type from \'l\' to \'f\'." ;
		hfls:cell_methods = "area: time: mean" ;
		hfls:cell_measures = "area: areacella" ;
		hfls:missing_value = 1.e+20f ;
		hfls:_fillvalue = 1.e+20f ;

// global attributes:
		:conventions = "cf-1.7 cmip-6.2" ;
		:activity_id = "ismip6" ;
		:branch_method = "no parent" ;
		:branch_time_in_child = 59400. ;
		:branch_time_in_parent = 0. ;
		:contact = "python coder (coder@a.b.c.com)" ;
		:creation_date = "2019-01-08t23:32:26z" ;
		:data_specs_version = "01.00.27" ;
		:experiment = "preindustrial control with interactive ice sheet" ;
		:experiment_id = "picontrol-withism" ;
		:external_variables = "areacella" ;
		:forcing_index = 1 ;
		:frequency = "mon" ;
		:further_info_url = "https://furtherinfo.es-doc.org/cmip6.pcmdi.pcmdi-test-1-0.picontrol-withism.none.r3i1p1f1" ;
		:grid = "native atmosphere regular grid (3x4 latxlon)" ;
		:grid_label = "gn" ;
		:history = "2019-01-08t23:32:26z ;rewrote data to be consistent with ismip6 for variable hfls found in table amon.;\n",
			"output from archivcl_a1.nce/giccm_03_std_2xco2_2256." ;
		:initialization_index = 1 ;
		:institution = "program for climate model diagnosis and intercomparison, lawrence livermore national laboratory, livermore, ca 94550, usa" ;
		:institution_id = "pcmdi" ;
		:mip_era = "cmip6" ;
		:nominal_resolution = "10000 km" ;
		:parent_activity_id = "no parent" ;
		:parent_experiment_id = "no parent" ;
		:parent_mip_era = "no parent" ;
		:parent_source_id = "no parent" ;
		:parent_time_units = "no parent" ;
		:parent_variant_label = "no parent" ;
		:physics_index = 1 ;
		:product = "model-output" ;
		:realization_index = 3 ;
		:realm = "atmos" ;
		:references = "model described by koder and tolkien (j. geophys. res., 2001, 576-591).  also see http://www.gicc.su/giccm/doc/index.html.  the ssp245 simulation is described in dorkey et al. \'(clim. dyn., 2003, 323-357.)\'" ;
		:run_variant = "3rd realization" ;
		:source = "pcmdi-test 1.0 (1989): \n",
			"aerosol: none\n",
			"atmos: earth1.0-gettinghotter (360 x 180 longitude/latitude; 50 levels; top level 0.1 mb)\n",
			"atmoschem: none\n",
			"land: earth1.0\n",
			"landice: none\n",
			"ocean: bluemarble1.0-warming (360 x 180 longitude/latitude; 50 levels; top grid cell 0-10 m)\n",
			"ocnbgchem: none\n",
			"seaice: declining1.0-warming (360 x 180 longitude/latitude)" ;
		:source_id = "pcmdi-test-1-0" ;
		:source_type = "aogcm ism aer" ;
		:sub_experiment = "none" ;
		:sub_experiment_id = "none" ;
		:table_id = "amon" ;
		:table_info = "creation date:(30 july 2018) md5:fa9bc503f57fb067bf398cab2c4ba77e" ;
		:title = "pcmdi-test-1-0 output prepared for cmip6" ;
		:tracking_id = "hdl:21.14100/ded65b61-6588-48f6-bd07-7e4281be9bee" ;
		:variable_id = "hfls" ;
		:variant_label = "r3i1p1f1" ;
		:license = "cmip6 model data produced by lawrence livermore pcmdi is licensed under a creative commons attribution sharealike 4.0 international license (https://creativecommons.org/licenses). consult https://pcmdi.llnl.gov/cmip6/termsofuse for terms of use governing cmip6 output, including citation requirements and proper acknowledgment. further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. the data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. all liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law." ;
		:cmor_version = "3.4.0" ;
data:

 time = 15.5, 45.5 ;

 time_bnds =
  0, 31,
  31, 60 ;

 lat = 10, 20, 30 ;

 lat_bnds =
  5, 15,
  15, 25,
  25, 35 ;

 lon = 0, 90, 180, 270 ;

 lon_bnds =
  -45, 45,
  45, 135,
  135, 225,
  225, 315 ;

 hfls =
  120, 116, 112, 108,
  104, 100, 96, 92,
  88, 84, 80, 76,
  119, 115, 111, 107,
  103, 99, 95, 91,
  87, 83, 79, 75 ;
}
```

</details>


### Example 3: Usual Treatment of a 3-D Field on Pressure Levels

* [example3.py](/mydoc/examples/example3.py)

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
import cmor
import numpy
import os

ta = 10. * numpy.random.random_sample((2, 19, 3, 4)) + 250.
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])
lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])
time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])
lev = numpy.array([100000, 92500, 85000, 70000, 60000, 50000, 40000, 30000,
                   25000, 20000, 15000, 10000, 7000, 5000, 3000, 2000, 1000, 500, 100])
ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)
cmor.dataset_json("CMOR_input_example.json")
cmor.load_table("CMIP6_Amon.json")
cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
cmorLev = cmor.axis("plev19", coord_vals=lev, units='Pa')
axes = [cmorTime, cmorLev, cmorLat, cmorLon]
cmorTa = cmor.variable("ta", "K", axes)
cmor.write(cmorTa, ta)
filename = cmor.close(cmorTa, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))


```
</details>
<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```
netcdf ta_Amon_PCMDI-test-1-0_piControl-withism_r3i1p1f1_gn_201801-201802 {
dimensions:
	time = UNLIMITED ; // (2 currently)
	plev = 19 ;
	lat = 3 ;
	lon = 4 ;
	bnds = 2 ;
variables:
	double time(time) ;
		time:bounds = "time_bnds" ;
		time:units = "days since 2018" ;
		time:calendar = "360_day" ;
		time:axis = "T" ;
		time:long_name = "time" ;
		time:standard_name = "time" ;
	double time_bnds(time, bnds) ;
	double plev(plev) ;
		plev:units = "Pa" ;
		plev:axis = "Z" ;
		plev:positive = "down" ;
		plev:long_name = "pressure" ;
		plev:standard_name = "air_pressure" ;
	double lat(lat) ;
		lat:bounds = "lat_bnds" ;
		lat:units = "degrees_north" ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
	double lat_bnds(lat, bnds) ;
	double lon(lon) ;
		lon:bounds = "lon_bnds" ;
		lon:units = "degrees_east" ;
		lon:axis = "X" ;
		lon:long_name = "Longitude" ;
		lon:standard_name = "longitude" ;
	double lon_bnds(lon, bnds) ;
	float ta(time, plev, lat, lon) ;
		ta:standard_name = "air_temperature" ;
		ta:long_name = "Air Temperature" ;
		ta:comment = "Air Temperature" ;
		ta:units = "K" ;
		ta:cell_methods = "time: mean" ;
		ta:cell_measures = "area: areacella" ;
		ta:missing_value = 1.e+20f ;
		ta:_FillValue = 1.e+20f ;
		ta:history = "2019-01-08T23:35:44Z altered by CMOR: Converted type from \'d\' to \'f\'." ;

// global attributes:
		:Conventions = "CF-1.7 CMIP-6.2" ;
		:activity_id = "ISMIP6" ;
		:branch_method = "no parent" ;
		:branch_time_in_child = 59400. ;
		:branch_time_in_parent = 0. ;
		:contact = "Python Coder (coder@a.b.c.com)" ;
		:creation_date = "2019-01-08T23:35:44Z" ;
		:data_specs_version = "01.00.27" ;
		:experiment = "preindustrial control with interactive ice sheet" ;
		:experiment_id = "piControl-withism" ;
		:external_variables = "areacella" ;
		:forcing_index = 1 ;
		:frequency = "mon" ;
		:further_info_url = "https://furtherinfo.es-doc.org/CMIP6.PCMDI.PCMDI-test-1-0.piControl-withism.none.r3i1p1f1" ;
		:grid = "native atmosphere regular grid (3x4 latxlon)" ;
		:grid_label = "gn" ;
		:history = "2019-01-08T23:35:44Z ;rewrote data to be consistent with ISMIP6 for variable ta found in table Amon.;\n",
			"Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256." ;
		:initialization_index = 1 ;
		:institution = "Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA" ;
		:institution_id = "PCMDI" ;
		:mip_era = "CMIP6" ;
		:nominal_resolution = "10000 km" ;
		:parent_activity_id = "no parent" ;
		:parent_experiment_id = "no parent" ;
		:parent_mip_era = "no parent" ;
		:parent_source_id = "no parent" ;
		:parent_time_units = "no parent" ;
		:parent_variant_label = "no parent" ;
		:physics_index = 1 ;
		:product = "model-output" ;
		:realization_index = 3 ;
		:realm = "atmos" ;
		:references = "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html.  The ssp245 simulation is described in Dorkey et al. \'(Clim. Dyn., 2003, 323-357.)\'" ;
		:run_variant = "3rd realization" ;
		:source = "PCMDI-test 1.0 (1989): \n",
			"aerosol: none\n",
			"atmos: Earth1.0-gettingHotter (360 x 180 longitude/latitude; 50 levels; top level 0.1 mb)\n",
			"atmosChem: none\n",
			"land: Earth1.0\n",
			"landIce: none\n",
			"ocean: BlueMarble1.0-warming (360 x 180 longitude/latitude; 50 levels; top grid cell 0-10 m)\n",
			"ocnBgchem: none\n",
			"seaIce: Declining1.0-warming (360 x 180 longitude/latitude)" ;
		:source_id = "PCMDI-test-1-0" ;
		:source_type = "AOGCM ISM AER" ;
		:sub_experiment = "none" ;
		:sub_experiment_id = "none" ;
		:table_id = "Amon" ;
		:table_info = "Creation Date:(30 July 2018) MD5:fa9bc503f57fb067bf398cab2c4ba77e" ;
		:title = "PCMDI-test-1-0 output prepared for CMIP6" ;
		:tracking_id = "hdl:21.14100/11fd8d79-f1d9-453d-8293-7603dc5dfe1e" ;
		:variable_id = "ta" ;
		:variant_label = "r3i1p1f1" ;
		:license = "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law." ;
		:cmor_version = "3.4.0" ;
data:

 time = 15.5, 45.5 ;

 time_bnds =
  0, 31,
  31, 60 ;

 plev = 100000, 92500, 85000, 70000, 60000, 50000, 40000, 30000, 25000, 
    20000, 15000, 10000, 7000, 5000, 3000, 2000, 1000, 500, 100 ;

 lat = 10, 20, 30 ;

 lat_bnds =
  5, 15,
  15, 25,
  25, 35 ;

 lon = 0, 90, 180, 270 ;

 lon_bnds =
  -45, 45,
  45, 135,
  135, 225,
  225, 315 ;

 ta =
  259.8408, 258.941, 252.4908, 251.0074,
  256.835, 258.2486, 250.7763, 256.6857,
  255.0459, 250.3535, 255.2871, 259.8668,
  253.4483, 256.5141, 259.7679, 252.1754,
  253.76, 250.867, 251.4578, 254.0015,
  252.3708, 258.2815, 255.3655, 257.9578,
  250.4145, 256.8469, 252.7675, 255.7654,
  258.5681, 259.7048, 254.8929, 252.6632,
  253.612, 258.3735, 256.299, 256.6488,
  253.1254, 254.9136, 255.2808, 253.8569,
  257.0341, 251.0754, 254.2664, 252.9441,
  255.2702, 255.9075, 253.3035, 257.6259,
  255.9043, 252.595, 253.9338, 258.0882,
  256.6787, 253.8391, 258.4736, 256.7391,
  252.671, 258.3957, 252.4797, 253.4284,
  258.6154, 258.6605, 255.7659, 252.4936,
  256.9681, 254.4894, 252.7608, 254.783,
  250.0667, 255.6354, 258.6563, 259.6775,
  254.3134, 250.8413, 250.2444, 254.6606,
  255.1599, 257.21, 252.6211, 256.2644,
  254.1385, 257.6524, 252.9917, 251.8146,
  259.5888, 256.2946, 255.9592, 254.3341,
  258.4659, 259.7941, 258.0905, 258.1966,
  257.4232, 259.0263, 251.2242, 259.6272,
  257.456, 259.999, 258.7972, 256.6927,
  256.5442, 250.3652, 254.9976, 254.2698,
  256.8535, 252.3693, 259.0882, 258.8849,
  253.6198, 259.3818, 251.4028, 254.9819,
  250.2339, 251.6083, 256.1446, 258.8874,
  259.977, 252.5453, 253.6287, 252.0314,
  257.0711, 254.6262, 253.957, 258.0355,
  250.333, 255.8116, 252.4928, 250.0648,
  256.737, 251.6935, 251.2943, 250.1732,
  256.9901, 256.2216, 259.1346, 258.9967,
  258.4938, 257.6587, 252.6762, 256.5123,
  254.6203, 257.5838, 259.8249, 257.2421,
  251.5132, 250.6997, 255.1321, 255.9642,
  250.5069, 251.3887, 252.1133, 253.0272,
  257.2178, 251.7756, 256.3568, 255.6339,
  250.4361, 258.3318, 259.5203, 258.9857,
  254.0756, 251.2124, 252.6628, 259.1253,
  252.2022, 254.2113, 259.4847, 252.9702,
  251.1179, 259.7756, 253.7968, 257.081,
  254.7999, 253.5379, 259.9748, 257.6128,
  257.1583, 258.5191, 252.2605, 251.6866,
  251.9091, 255.4374, 259.1645, 255.4471,
  251.6325, 252.1992, 256.1027, 252.4458,
  251.5014, 252.293, 250.0457, 251.2812,
  252.3479, 253.4959, 250.742, 254.3526,
  254.2659, 258.3052, 259.6293, 253.8284,
  255.0674, 250.3642, 252.008, 258.3384,
  258.2568, 257.897, 253.424, 254.922,
  254.939, 253.0223, 257.8987, 256.4419,
  254.1967, 257.1554, 253.706, 256.5611,
  259.3974, 254.3611, 251.2371, 257.0125,
  255.4547, 255.4249, 252.8776, 257.173,
  258.8824, 252.4057, 250.6023, 253.0139,
  255.5045, 257.2598, 257.7797, 253.2221,
  253.2658, 252.578, 255.4973, 252.6226,
  259.9648, 251.6002, 254.1322, 251.8064,
  254.0982, 252.5025, 251.4612, 251.3052,
  254.25, 251.7179, 251.4255, 256.1079,
  257.282, 255.7924, 252.2107, 255.8521,
  252.7759, 253.0962, 252.638, 255.9666,
  259.5663, 253.6493, 256.8842, 255.4041,
  254.6592, 255.4181, 258.7055, 254.7371,
  257.1625, 255.0113, 253.0983, 252.3584,
  257.2872, 253.2124, 256.9593, 250.7623,
  257.287, 257.2986, 252.6907, 251.519,
  254.1635, 250.1762, 256.4446, 259.7633,
  259.0938, 253.0846, 250.5819, 258.3493,
  258.6836, 257.3046, 255.8258, 257.9142,
  257.3879, 252.5779, 255.3217, 254.2868,
  255.9011, 252.4209, 253.7516, 255.2315,
  257.6159, 257.8478, 253.0855, 254.9258,
  255.5278, 257.5585, 258.8186, 250.2102,
  250.1217, 256.8153, 255.6852, 255.1126,
  257.7202, 256.3726, 252.1865, 253.0071,
  251.8633, 255.1148, 254.0191, 253.4735,
  257.7912, 253.4579, 255.0269, 250.1707,
  253.9734, 254.2229, 257.9263, 250.1125,
  258.5282, 250.8859, 257.5581, 255.8632,
  252.3537, 253.3955, 252.4796, 251.3484,
  259.0306, 250.2142, 253.429, 251.3313,
  257.0627, 253.5232, 254.0599, 253.5528,
  254.7048, 257.3163, 258.5922, 259.0777,
  253.2622, 258.1998, 254.3777, 259.3747,
  252.3826, 251.1805, 253.8417, 251.8928,
  256.3958, 256.0284, 253.0213, 256.2551,
  258.8141, 258.835, 259.7631, 254.7228,
  254.3701, 251.3905, 250.6818, 258.296,
  258.9814, 258.1483, 256.1503, 252.6487,
  252.123, 256.3247, 252.2733, 259.7609,
  259.3987, 252.3202, 250.5132, 252.3688,
  257.4306, 256.0952, 253.014, 251.8331,
  253.5333, 259.0857, 257.7149, 259.9082,
  259.6393, 258.5578, 256.9663, 252.2192,
  254.2118, 251.6638, 255.6581, 255.7678,
  253.8299, 251.3065, 255.6969, 259.1021,
  256.2309, 257.8936, 251.7329, 253.7878,
  256.5732, 254.0137, 253.6299, 250.413,
  258.7727, 251.4784, 253.509, 255.0283,
  254.1883, 255.0535, 250.6044, 257.4061,
  252.835, 255.2766, 257.4215, 259.0279,
  255.3313, 254.1923, 254.1777, 258.1096,
  250.3586, 255.7441, 258.2351, 257.1729,
  258.3901, 256.7424, 259.8389, 254.8441,
  252.9138, 256.6953, 255.918, 253.6417,
  252.3907, 255.4751, 258.3704, 255.8665,
  250.0418, 251.8351, 258.5436, 256.8799,
  252.2263, 255.383, 253.3702, 253.7597,
  251.112, 254.6407, 251.4067, 252.6422,
  258.1817, 252.3663, 253.5502, 252.4341,
  257.1426, 254.4529, 254.8314, 254.7638 ;
}
```
</details>

### Example 4: Treatment of a Scalar Dimension (near-surface air temperature)

* [example4.py](/mydoc/examples/example4.py)

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
import cmor
import numpy
import os

tas = 10. * numpy.random.random_sample((2, 3, 4)) + 250.
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])
lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])
time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])
ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)
cmor.dataset_json("CMOR_input_example.json")
cmor.load_table("CMIP6_Amon.json")
cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
axes = [cmorTime, cmorLat, cmorLon]
cmorTas = cmor.variable("tas", "K", axes)
cmor.write(cmorTas, tas)
filename = cmor.close(cmorTas, file_name=True)
print("Stored in:", filename)
cmor.close()
```
</details>
<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```
netcdf tas_Amon_PCMDI-test-1-0_piControl-withism_r3i1p1f1_gn_201801-201802 {
dimensions:
	time = UNLIMITED ; // (2 currently)
	lat = 3 ;
	lon = 4 ;
	bnds = 2 ;
variables:
	double time(time) ;
		time:bounds = "time_bnds" ;
		time:units = "days since 2018" ;
		time:calendar = "360_day" ;
		time:axis = "T" ;
		time:long_name = "time" ;
		time:standard_name = "time" ;
	double time_bnds(time, bnds) ;
	double lat(lat) ;
		lat:bounds = "lat_bnds" ;
		lat:units = "degrees_north" ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
	double lat_bnds(lat, bnds) ;
	double lon(lon) ;
		lon:bounds = "lon_bnds" ;
		lon:units = "degrees_east" ;
		lon:axis = "X" ;
		lon:long_name = "Longitude" ;
		lon:standard_name = "longitude" ;
	double lon_bnds(lon, bnds) ;
	double height ;
		height:units = "m" ;
		height:axis = "Z" ;
		height:positive = "up" ;
		height:long_name = "height" ;
		height:standard_name = "height" ;
	float tas(time, lat, lon) ;
		tas:standard_name = "air_temperature" ;
		tas:long_name = "Near-Surface Air Temperature" ;
		tas:comment = "near-surface (usually, 2 meter) air temperature" ;
		tas:units = "K" ;
		tas:cell_methods = "area: time: mean" ;
		tas:cell_measures = "area: areacella" ;
		tas:history = "2019-01-08T23:41:05Z altered by CMOR: Treated scalar dimension: \'height\'. 2019-01-08T23:41:05Z altered by CMOR: Converted type from \'d\' to \'f\'." ;
		tas:coordinates = "height" ;
		tas:missing_value = 1.e+20f ;
		tas:_FillValue = 1.e+20f ;

// global attributes:
		:Conventions = "CF-1.7 CMIP-6.2" ;
		:activity_id = "ISMIP6" ;
		:branch_method = "no parent" ;
		:branch_time_in_child = 59400. ;
		:branch_time_in_parent = 0. ;
		:contact = "Python Coder (coder@a.b.c.com)" ;
		:creation_date = "2019-01-08T23:41:05Z" ;
		:data_specs_version = "01.00.27" ;
		:experiment = "preindustrial control with interactive ice sheet" ;
		:experiment_id = "piControl-withism" ;
		:external_variables = "areacella" ;
		:forcing_index = 1 ;
		:frequency = "mon" ;
		:further_info_url = "https://furtherinfo.es-doc.org/CMIP6.PCMDI.PCMDI-test-1-0.piControl-withism.none.r3i1p1f1" ;
		:grid = "native atmosphere regular grid (3x4 latxlon)" ;
		:grid_label = "gn" ;
		:history = "2019-01-08T23:41:05Z ;rewrote data to be consistent with ISMIP6 for variable tas found in table Amon.;\n",
			"Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256." ;
		:initialization_index = 1 ;
		:institution = "Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA" ;
		:institution_id = "PCMDI" ;
		:mip_era = "CMIP6" ;
		:nominal_resolution = "10000 km" ;
		:parent_activity_id = "no parent" ;
		:parent_experiment_id = "no parent" ;
		:parent_mip_era = "no parent" ;
		:parent_source_id = "no parent" ;
		:parent_time_units = "no parent" ;
		:parent_variant_label = "no parent" ;
		:physics_index = 1 ;
		:product = "model-output" ;
		:realization_index = 3 ;
		:realm = "atmos" ;
		:references = "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html.  The ssp245 simulation is described in Dorkey et al. \'(Clim. Dyn., 2003, 323-357.)\'" ;
		:run_variant = "3rd realization" ;
		:source = "PCMDI-test 1.0 (1989): \n",
			"aerosol: none\n",
			"atmos: Earth1.0-gettingHotter (360 x 180 longitude/latitude; 50 levels; top level 0.1 mb)\n",
			"atmosChem: none\n",
			"land: Earth1.0\n",
			"landIce: none\n",
			"ocean: BlueMarble1.0-warming (360 x 180 longitude/latitude; 50 levels; top grid cell 0-10 m)\n",
			"ocnBgchem: none\n",
			"seaIce: Declining1.0-warming (360 x 180 longitude/latitude)" ;
		:source_id = "PCMDI-test-1-0" ;
		:source_type = "AOGCM ISM AER" ;
		:sub_experiment = "none" ;
		:sub_experiment_id = "none" ;
		:table_id = "Amon" ;
		:table_info = "Creation Date:(30 July 2018) MD5:fa9bc503f57fb067bf398cab2c4ba77e" ;
		:title = "PCMDI-test-1-0 output prepared for CMIP6" ;
		:tracking_id = "hdl:21.14100/f93e4db7-d6e5-404d-983b-dbfebc932250" ;
		:variable_id = "tas" ;
		:variant_label = "r3i1p1f1" ;
		:license = "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law." ;
		:cmor_version = "3.4.0" ;
data:

 time = 15.5, 45.5 ;

 time_bnds =
  0, 31,
  31, 60 ;

 lat = 10, 20, 30 ;

 lat_bnds =
  5, 15,
  15, 25,
  25, 35 ;

 lon = 0, 90, 180, 270 ;

 lon_bnds =
  -45, 45,
  45, 135,
  135, 225,
  225, 315 ;

 height = 2 ;

 tas =
  254.0895, 258.4085, 250.5549, 258.7101,
  258.668, 258.299, 252.1237, 255.0432,
  253.7254, 251.246, 254.3168, 255.4808,
  259.7908, 252.2754, 257.1892, 253.3132,
  253.8823, 253.4698, 253.5381, 254.973,
  256.1002, 251.8168, 259.3698, 250.2994 ;
}
```

</details>

### Example 5: Treatment of Auxiliary Coordinates (northward ocean heat transport; a function of latitude, ocean basin, month)

* [example5.py](/mydoc/examples/example5.py)

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
import cmor
import numpy
import os

data = 10. * numpy.random.random_sample((2, 3, 4)) + 250.
data = numpy.array([-80, -84, -88,
                    -100, -104, -76,
                    -120, -92, -96,
                    -79, -83, -87,
                    -99, -103, -75,
                    -107, -111, -115
                    ])
data.shape = (2, 3, 3)
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])
time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])
region = [
    "atlantic_arctic_ocean",
    "indian_pacific_ocean",
    "global_ocean"
]
ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)
cmor.dataset_json("CMOR_input_example.json")
cmor.load_table("CMIP6_Omon.json")
cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
cmorBasin = cmor.axis("basin", coord_vals=region, units="")
axes = [cmorTime, cmorBasin, cmorLat]
cmorVar = cmor.variable("htovgyre", "W", axes)
cmor.write(cmorVar, data)
filename = cmor.close(cmorVar, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))


```

</details>
<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```
netcdf htovgyre_Omon_PCMDI-test-1-0_piControl-withism_r3i1p1f1_gn_201801-201802 {
dimensions:
	time = UNLIMITED ; // (2 currently)
	basin = 3 ;
	lat = 3 ;
	bnds = 2 ;
	strlen = 21 ;
variables:
	double time(time) ;
		time:bounds = "time_bnds" ;
		time:units = "days since 2018" ;
		time:calendar = "360_day" ;
		time:axis = "T" ;
		time:long_name = "time" ;
		time:standard_name = "time" ;
	double time_bnds(time, bnds) ;
	char sector(basin, strlen) ;
		sector:long_name = "ocean basin" ;
		sector:standard_name = "region" ;
	double lat(lat) ;
		lat:bounds = "lat_bnds" ;
		lat:units = "degrees_north" ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
	double lat_bnds(lat, bnds) ;
	float htovgyre(time, basin, lat) ;
		htovgyre:standard_name = "northward_ocean_heat_transport_due_to_gyre" ;
		htovgyre:long_name = "Northward Ocean Heat Transport due to Gyre" ;
		htovgyre:comment = "From all advective mass transport processes, resolved and parameterized." ;
		htovgyre:units = "W" ;
		htovgyre:cell_methods = "longitude: mean time: mean" ;
		htovgyre:missing_value = 1.e+20f ;
		htovgyre:_FillValue = 1.e+20f ;
		htovgyre:history = "2019-01-08T23:45:26Z altered by CMOR: Converted type from \'l\' to \'f\'." ;
		htovgyre:coordinates = "sector" ;

// global attributes:
		:Conventions = "CF-1.7 CMIP-6.2" ;
		:activity_id = "ISMIP6" ;
		:branch_method = "no parent" ;
		:branch_time_in_child = 59400. ;
		:branch_time_in_parent = 0. ;
		:contact = "Python Coder (coder@a.b.c.com)" ;
		:creation_date = "2019-01-08T23:45:26Z" ;
		:data_specs_version = "01.00.27" ;
		:experiment = "preindustrial control with interactive ice sheet" ;
		:experiment_id = "piControl-withism" ;
		:forcing_index = 1 ;
		:frequency = "mon" ;
		:further_info_url = "https://furtherinfo.es-doc.org/CMIP6.PCMDI.PCMDI-test-1-0.piControl-withism.none.r3i1p1f1" ;
		:grid = "native atmosphere regular grid (3x4 latxlon)" ;
		:grid_label = "gn" ;
		:history = "2019-01-08T23:45:26Z ;rewrote data to be consistent with ISMIP6 for variable htovgyre found in table Omon.;\n",
			"Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256." ;
		:initialization_index = 1 ;
		:institution = "Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA" ;
		:institution_id = "PCMDI" ;
		:mip_era = "CMIP6" ;
		:nominal_resolution = "10000 km" ;
		:parent_activity_id = "no parent" ;
		:parent_experiment_id = "no parent" ;
		:parent_mip_era = "no parent" ;
		:parent_source_id = "no parent" ;
		:parent_time_units = "no parent" ;
		:parent_variant_label = "no parent" ;
		:physics_index = 1 ;
		:product = "model-output" ;
		:realization_index = 3 ;
		:realm = "ocean" ;
		:references = "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html.  The ssp245 simulation is described in Dorkey et al. \'(Clim. Dyn., 2003, 323-357.)\'" ;
		:run_variant = "3rd realization" ;
		:source = "PCMDI-test 1.0 (1989): \n",
			"aerosol: none\n",
			"atmos: Earth1.0-gettingHotter (360 x 180 longitude/latitude; 50 levels; top level 0.1 mb)\n",
			"atmosChem: none\n",
			"land: Earth1.0\n",
			"landIce: none\n",
			"ocean: BlueMarble1.0-warming (360 x 180 longitude/latitude; 50 levels; top grid cell 0-10 m)\n",
			"ocnBgchem: none\n",
			"seaIce: Declining1.0-warming (360 x 180 longitude/latitude)" ;
		:source_id = "PCMDI-test-1-0" ;
		:source_type = "AOGCM ISM AER" ;
		:sub_experiment = "none" ;
		:sub_experiment_id = "none" ;
		:table_id = "Omon" ;
		:table_info = "Creation Date:(30 July 2018) MD5:fa9bc503f57fb067bf398cab2c4ba77e" ;
		:title = "PCMDI-test-1-0 output prepared for CMIP6" ;
		:tracking_id = "hdl:21.14100/631e76b6-64a0-4f24-8c67-e3a9a03a2920" ;
		:variable_id = "htovgyre" ;
		:variant_label = "r3i1p1f1" ;
		:license = "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law." ;
		:cmor_version = "3.4.0" ;
data:

 time = 15.5, 45.5 ;

 time_bnds =
  0, 31,
  31, 60 ;

 sector =
  "atlantic_arctic_ocean",
  "indian_pacific_ocean",
  "global_ocean" ;

 lat = 10, 20, 30 ;

 lat_bnds =
  5, 15,
  15, 25,
  25, 35 ;

 htovgyre =
  -80, -84, -88,
  -100, -104, -76,
  -120, -92, -96,
  -79, -83, -87,
  -99, -103, -75,
  -107, -111, -115 ;
}
```

</details>

### Example 6: Treatment of a 3-D Field on Model Levels (cloud fraction; a function of longitude, latitude, model level, month)

* [example6.py](/mydoc/examples/example6.py)

<details><summary markdown="span"><b>Click to expand Python code</b></summary>

```python
import cmor
import numpy
import os

data = 10. * numpy.random.random_sample((2, 3, 4)) + 250.
data = numpy.array([
    72.8, 73.2, 73.6, 74,
    71.6, 72, 72.4, 72.4,
    70.4, 70.8, 70.8, 71.2,
    67.6, 69.2, 69.6, 70,
    66, 66.4, 66.8, 67.2,
    64.8, 65.2, 65.6, 66,
    63.6, 64, 64.4, 64.4,
    60.8, 61.2, 62.8, 63.2,
    59.6, 59.6, 60, 60.4,
    58, 58.4, 58.8, 59.2,
    56.8, 57.2, 57.6, 58,
    54, 54.4, 54.8, 56.4,
    52.8, 53.2, 53.2, 53.6,
    51.6, 51.6, 52, 52.4,
    50, 50.4, 50.8, 51.2,
    72.9, 73.3, 73.7, 74.1,
    71.7, 72.1, 72.5, 72.5,
    70.5, 70.9, 70.9, 71.3,
    67.7, 69.3, 69.7, 70.1,
    66.1, 66.5, 66.9, 67.3,
    64.9, 65.3, 65.7, 66.1,
    63.7, 64.1, 64.5, 64.5,
    60.9, 61.3, 62.9, 63.3,
    59.7, 59.7, 60.1, 60.5,
    58.1, 58.5, 58.9, 59.3,
    56.9, 57.3, 57.7, 58.1,
    54.1, 54.5, 54.9, 56.5,
    52.9, 53.3, 53.3, 53.7,
    51.7, 51.7, 52.1, 52.5,
    50.1, 50.5, 50.9, 51.3])
data.shape = (2, 5, 3, 4)
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])
lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])
time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])
lev = [0.92, 0.72, 0.5, 0.3, 0.1]
lev_bnds = [1, 0.83,
            0.61,
            0.4,
            0.2,
            0
            ]
p0 = 100000
a = [0.12, 0.22, 0.3, 0.2, 0.1]
b = [0.8, 0.5, 0.2, 0.1, 0]
ps = numpy.array([
    97000, 97400, 97800, 98200,
    98600, 99000, 99400, 99800,
    100200, 100600, 101000, 101400,
    97100, 97500, 97900, 98300,
    98700, 99100, 99500, 99900,
    100300, 100700, 101100, 101500])
ps.shape = (2, 3, 4)
a_bnds = [
    0.06, 0.18,
    0.26,
    0.25,
    0.15,
    0]
b_bnds = [
    0.94, 0.65,
    0.35,
    0.15,
    0.05,
    0]
ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)
cmor.dataset_json("CMOR_input_example.json")
cmor.load_table("CMIP6_Amon.json")
cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
cmorLev = cmor.axis("standard_hybrid_sigma",
                    units='1',
                    coord_vals=lev,
                    cell_bounds=lev_bnds)
axes = [cmorTime, cmorLev, cmorLat, cmorLon]
ierr = cmor.zfactor(zaxis_id=cmorLev,
                    zfactor_name='a',
                    axis_ids=[cmorLev, ],
                    zfactor_values=a,
                    zfactor_bounds=a_bnds)
ierr = cmor.zfactor(zaxis_id=cmorLev,
                    zfactor_name='b',
                    axis_ids=[cmorLev, ],
                    zfactor_values=b,
                    zfactor_bounds=b_bnds)
ierr = cmor.zfactor(zaxis_id=cmorLev,
                    zfactor_name='p0',
                    units='Pa',
                    zfactor_values=p0)
ips = cmor.zfactor(zaxis_id=cmorLev,
                   zfactor_name='ps',
                   axis_ids=[cmorTime, cmorLat, cmorLon],
                   units='Pa')
cmorVar = cmor.variable("cl", "%", axes)
cmor.write(cmorVar, data)
cmor.write(ips, ps, store_with=cmorVar)
filename = cmor.close(cmorVar, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))
```

</details>
<details><summary markdown="span"><b>Click to expand NetCDF dump</b></summary>

```
netcdf cl_Amon_PCMDI-test-1-0_piControl-withism_r3i1p1f1_gn_201801-201802 {
dimensions:
	time = UNLIMITED ; // (2 currently)
	lev = 5 ;
	lat = 3 ;
	lon = 4 ;
	bnds = 2 ;
variables:
	double time(time) ;
		time:bounds = "time_bnds" ;
		time:units = "days since 2018" ;
		time:calendar = "360_day" ;
		time:axis = "T" ;
		time:long_name = "time" ;
		time:standard_name = "time" ;
	double time_bnds(time, bnds) ;
	double lev(lev) ;
		lev:bounds = "lev_bnds" ;
		lev:units = "1" ;
		lev:axis = "Z" ;
		lev:positive = "down" ;
		lev:long_name = "hybrid sigma pressure coordinate" ;
		lev:standard_name = "atmosphere_hybrid_sigma_pressure_coordinate" ;
		lev:formula = "p = a*p0 + b*ps" ;
		lev:formula_terms = "p0: p0 a: a b: b ps: ps" ;
	double lev_bnds(lev, bnds) ;
		lev_bnds:formula = "p = a*p0 + b*ps" ;
		lev_bnds:standard_name = "atmosphere_hybrid_sigma_pressure_coordinate" ;
		lev_bnds:units = "1" ;
		lev_bnds:formula_terms = "p0: p0 a: a_bnds b: b_bnds ps: ps" ;
	double p0 ;
		p0:long_name = "vertical coordinate formula term: reference pressure" ;
		p0:units = "Pa" ;
	double a(lev) ;
		a:long_name = "vertical coordinate formula term: a(k)" ;
	double b(lev) ;
		b:long_name = "vertical coordinate formula term: b(k)" ;
	float ps(time, lat, lon) ;
		ps:long_name = "Surface Air Pressure" ;
		ps:units = "Pa" ;
	double a_bnds(lev, bnds) ;
		a_bnds:long_name = "vertical coordinate formula term: a(k+1/2)" ;
	double b_bnds(lev, bnds) ;
		b_bnds:long_name = "vertical coordinate formula term: b(k+1/2)" ;
	double lat(lat) ;
		lat:bounds = "lat_bnds" ;
		lat:units = "degrees_north" ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
	double lat_bnds(lat, bnds) ;
	double lon(lon) ;
		lon:bounds = "lon_bnds" ;
		lon:units = "degrees_east" ;
		lon:axis = "X" ;
		lon:long_name = "Longitude" ;
		lon:standard_name = "longitude" ;
	double lon_bnds(lon, bnds) ;
	float cl(time, lev, lat, lon) ;
		cl:standard_name = "cloud_area_fraction_in_atmosphere_layer" ;
		cl:long_name = "Cloud Area Fraction" ;
		cl:comment = "Percentage cloud cover, including both large-scale and convective cloud." ;
		cl:units = "%" ;
		cl:cell_methods = "area: time: mean" ;
		cl:cell_measures = "area: areacella" ;
		cl:missing_value = 1.e+20f ;
		cl:_FillValue = 1.e+20f ;
		cl:history = "2019-01-08T23:49:05Z altered by CMOR: Converted type from \'d\' to \'f\'." ;

// global attributes:
		:Conventions = "CF-1.7 CMIP-6.2" ;
		:activity_id = "ISMIP6" ;
		:branch_method = "no parent" ;
		:branch_time_in_child = 59400. ;
		:branch_time_in_parent = 0. ;
		:contact = "Python Coder (coder@a.b.c.com)" ;
		:creation_date = "2019-01-08T23:49:05Z" ;
		:data_specs_version = "01.00.27" ;
		:experiment = "preindustrial control with interactive ice sheet" ;
		:experiment_id = "piControl-withism" ;
		:external_variables = "areacella" ;
		:forcing_index = 1 ;
		:frequency = "mon" ;
		:further_info_url = "https://furtherinfo.es-doc.org/CMIP6.PCMDI.PCMDI-test-1-0.piControl-withism.none.r3i1p1f1" ;
		:grid = "native atmosphere regular grid (3x4 latxlon)" ;
		:grid_label = "gn" ;
		:history = "2019-01-08T23:49:05Z ;rewrote data to be consistent with ISMIP6 for variable cl found in table Amon.;\n",
			"Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256." ;
		:initialization_index = 1 ;
		:institution = "Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA" ;
		:institution_id = "PCMDI" ;
		:mip_era = "CMIP6" ;
		:nominal_resolution = "10000 km" ;
		:parent_activity_id = "no parent" ;
		:parent_experiment_id = "no parent" ;
		:parent_mip_era = "no parent" ;
		:parent_source_id = "no parent" ;
		:parent_time_units = "no parent" ;
		:parent_variant_label = "no parent" ;
		:physics_index = 1 ;
		:product = "model-output" ;
		:realization_index = 3 ;
		:realm = "atmos" ;
		:references = "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html.  The ssp245 simulation is described in Dorkey et al. \'(Clim. Dyn., 2003, 323-357.)\'" ;
		:run_variant = "3rd realization" ;
		:source = "PCMDI-test 1.0 (1989): \n",
			"aerosol: none\n",
			"atmos: Earth1.0-gettingHotter (360 x 180 longitude/latitude; 50 levels; top level 0.1 mb)\n",
			"atmosChem: none\n",
			"land: Earth1.0\n",
			"landIce: none\n",
			"ocean: BlueMarble1.0-warming (360 x 180 longitude/latitude; 50 levels; top grid cell 0-10 m)\n",
			"ocnBgchem: none\n",
			"seaIce: Declining1.0-warming (360 x 180 longitude/latitude)" ;
		:source_id = "PCMDI-test-1-0" ;
		:source_type = "AOGCM ISM AER" ;
		:sub_experiment = "none" ;
		:sub_experiment_id = "none" ;
		:table_id = "Amon" ;
		:table_info = "Creation Date:(30 July 2018) MD5:fa9bc503f57fb067bf398cab2c4ba77e" ;
		:title = "PCMDI-test-1-0 output prepared for CMIP6" ;
		:variable_id = "cl" ;
		:variant_label = "r3i1p1f1" ;
		:license = "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law." ;
		:cmor_version = "3.4.0" ;
		:tracking_id = "hdl:21.14100/68486bc9-5ee7-4a03-ba74-ec9cf9c86e3c" ;
data:

 time = 15.5, 45.5 ;

 time_bnds =
  0, 31,
  31, 60 ;

 lev = 0.92, 0.72, 0.5, 0.3, 0.1 ;

 lev_bnds =
  1, 0.83,
  0.83, 0.61,
  0.61, 0.4,
  0.4, 0.2,
  0.2, 0 ;

 p0 = 100000 ;

 a = 0.12, 0.22, 0.3, 0.2, 0.1 ;

 b = 0.8, 0.5, 0.2, 0.1, 0 ;

 ps =
  97000, 97400, 97800, 98200,
  98600, 99000, 99400, 99800,
  100200, 100600, 101000, 101400,
  97100, 97500, 97900, 98300,
  98700, 99100, 99500, 99900,
  100300, 100700, 101100, 101500 ;

 a_bnds =
  0.06, 0.18,
  0.18, 0.26,
  0.26, 0.25,
  0.25, 0.15,
  0.15, 0 ;

 b_bnds =
  0.94, 0.65,
  0.65, 0.35,
  0.35, 0.15,
  0.15, 0.05,
  0.05, 0 ;

 lat = 10, 20, 30 ;

 lat_bnds =
  5, 15,
  15, 25,
  25, 35 ;

 lon = 0, 90, 180, 270 ;

 lon_bnds =
  -45, 45,
  45, 135,
  135, 225,
  225, 315 ;

 cl =
  72.8, 73.2, 73.6, 74,
  71.6, 72, 72.4, 72.4,
  70.4, 70.8, 70.8, 71.2,
  67.6, 69.2, 69.6, 70,
  66, 66.4, 66.8, 67.2,
  64.8, 65.2, 65.6, 66,
  63.6, 64, 64.4, 64.4,
  60.8, 61.2, 62.8, 63.2,
  59.6, 59.6, 60, 60.4,
  58, 58.4, 58.8, 59.2,
  56.8, 57.2, 57.6, 58,
  54, 54.4, 54.8, 56.4,
  52.8, 53.2, 53.2, 53.6,
  51.6, 51.6, 52, 52.4,
  50, 50.4, 50.8, 51.2,
  72.9, 73.3, 73.7, 74.1,
  71.7, 72.1, 72.5, 72.5,
  70.5, 70.9, 70.9, 71.3,
  67.7, 69.3, 69.7, 70.1,
  66.1, 66.5, 66.9, 67.3,
  64.9, 65.3, 65.7, 66.1,
  63.7, 64.1, 64.5, 64.5,
  60.9, 61.3, 62.9, 63.3,
  59.7, 59.7, 60.1, 60.5,
  58.1, 58.5, 58.9, 59.3,
  56.9, 57.3, 57.7, 58.1,
  54.1, 54.5, 54.9, 56.5,
  52.9, 53.3, 53.3, 53.7,
  51.7, 51.7, 52.1, 52.5,
  50.1, 50.5, 50.9, 51.3 ;
}

```
</details>
