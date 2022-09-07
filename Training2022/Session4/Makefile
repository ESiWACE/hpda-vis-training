all:   ncfiles ice_sheet_complete.pvsm  json_files help

json_files: vrm-edited.json vrm-green-for-edit.json rignot-ish-with-white.json

ncfiles: friv_777.nc pism_ANT_777.nc pism_NH_777.nc surf_fw_out_pv_777.nc  veg_ratio_max_nn_777.nc vilma_ss_777.nc

%.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@

%.json:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@


ice_sheet_complete.pvsm:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@

help:
	echo Please also have a look at 'https://docs.dkrz.de/doc/visualization/sw/paraview/Examples/PalMod_combined/index.html'
