import cmor
import numpy
import os


var_data = numpy.random.random((3, 4, 2)) + 34.

x = numpy.arange(4, dtype=float)
x_bnds = numpy.array([[x_ - 0.5, x_ + 0.5] for x_ in x])
y = numpy.arange(3, dtype=float)
y_bnds = numpy.array([[y_ - 0.5, y_ + 0.5] for y_ in y])

lat = numpy.array([10, 20, 30]).reshape((3, 1))
lat = numpy.tile(lat, (1, 4))
lon = numpy.array([0, 90, 180, 270])
lon = numpy.tile(lon, (3, 1))
lon_bnds = numpy.zeros((3, 4, 4))
lat_bnds = numpy.zeros((3, 4, 4))

for j in range(3):
    for i in range(4):
        lon_bnds[j, i, 0] = (lon[j, i] - 45) % 360
        lon_bnds[j, i, 1] = lon[j, i]
        lon_bnds[j, i, 2] = (lon[j, i] + 45) % 360
        lon_bnds[j, i, 3] = lon[j, i]
        lat_bnds[j, i, 0] = lat[j, i]
        lat_bnds[j, i, 1] = lat[j, i] - 5
        lat_bnds[j, i, 2] = lat[j, i]
        lat_bnds[j, i, 3] = lat[j, i] + 5

time = numpy.array([0, 1])
time_bnds = numpy.array([0, 1, 2])

ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE,
           exit_control=cmor.CMOR_EXIT_ON_MAJOR)
cmor.dataset_json('CMOR_input_example.json')

# First, load the grids table to set up x and y axes and the lat-long grid
grid_table_id = cmor.load_table('CMIP6_grids.json')
cmor.set_table(grid_table_id)

y_axis_id = cmor.axis(table_entry='y_deg',
                      units='degrees',
                      coord_vals=y,
                      cell_bounds=y_bnds)
x_axis_id = cmor.axis(table_entry='x_deg',
                      units='degrees',
                      coord_vals=x,
                      cell_bounds=x_bnds)

grid_id = cmor.grid(axis_ids=[y_axis_id, x_axis_id],
                    latitude=lat,
                    longitude=lon,
                    latitude_vertices=lat_bnds,
                    longitude_vertices=lon_bnds)

# Now, load the Omon table to set up the time axis and variable
omon_table_id = cmor.load_table('CMIP6_Omon.json')
cmor.set_table(omon_table_id)

time_axis_id = cmor.axis(table_entry='time',
                         units='months since 1980',
                         coord_vals=time,
                         cell_bounds=time_bnds)

var_id = cmor.variable(table_entry='sos',
                       units='0.001',
                       axis_ids=[grid_id, time_axis_id])

cmor.write(var_id, var_data, 2)

filename = cmor.close(var_id, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))
