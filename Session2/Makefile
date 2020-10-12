all: uv.nc clivi_cllvi_newtime.nc world.topo.200402.3x1920.png help

uv.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/uv.nc'

world.topo.200402.3x1920.png:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/world.topo.200402.3x1920.png'

clivi_cllvi_newtime.nc:
	wget 'https://swift.dkrz.de/v1/dkrz_8656c91ce0734327b6dc867fc5b6b068/ESiWACE2-Public/Paraview%20Sample%20Data/clivi_cllvi_newtime.nc'

help:
	firefox 'https://visualisation.gitlab-pages.dkrz.de/documentation/Paraview/Examples/2D_ocean_example/index.html'
