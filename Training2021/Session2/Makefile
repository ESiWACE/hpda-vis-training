all: uv.nc clivi_cllvi_newtime.nc world.topo.200402.3x1920.png  ncfiles ice_sheet_complete.pvsm  json_files help

uv.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/uv.nc'

world.topo.200402.3x1920.png:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/world.topo.200402.3x1920.png'

clivi_cllvi_newtime.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/clivi_cllvi_newtime.nc'

json_files: vrm-edited.json vrm-green-for-edit.json rignot-ish-with-white.json

ncfiles: friv_777.nc pism_ANT_777.nc pism_NH_777.nc surf_fw_out_pv_777.nc  veg_ratio_max_nn_777.nc vilma_ss_777.nc

%.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@

%.json:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@


ice_sheet_complete.pvsm:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@

help:
	echo for more instructions open 'https://visualisation.gitlab-pages.dkrz.de/documentation/Paraview/Examples/2D_ocean_example/index.html'
	echo Please also have a look at https://visualisation.gitlab-pages.dkrz.de/documentation/Paraview/Examples/PalMod_combined/index.html
