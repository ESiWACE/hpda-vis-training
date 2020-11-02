all: ncfiles ice_sheet_complete.pvsm # help

ncfiles: friv_777.nc pism_ANT_777.nc pism_NH_777.nc surf_fw_out_pv_777.nc veg_ratio_max_777.nc veg_ratio_max_nn_777.nc vilma_ss_777.nc

%.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@
ice_sheet_complete.pvsm:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/PalMod_example/'$@

help:
	firefox 'https://visualisation.gitlab-pages.dkrz.de/documentation/Paraview/Examples/2D_ocean_example/index.html' &
