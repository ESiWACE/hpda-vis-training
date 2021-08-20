#!/bin/python3


def main():
	import os,sys
	from netCDF4 import Dataset
	import cartopy.crs as ccrs
	import matplotlib.pyplot as plt
	from cartopy.mpl.geoaxes import GeoAxes
	from cartopy.util import add_cyclic_point
	import numpy as np
	import imageio

	images = []
	img='/data/output/summer_days_'

	for i in range(2011,2014):

		filename = "/data/output/summer_days_"+str(i)+".nc"
		from netCDF4 import Dataset
		dataset = Dataset(filename,"r")	
		lat = dataset.variables['lat'][:]
		lon = dataset.variables['lon'][:]
		var =  dataset.variables['tasmax'][:]
		var = np.reshape(var, (len(lat), len(lon)))
		
		import cartopy.crs as ccrs
		import matplotlib.pyplot as plt
		from cartopy.mpl.geoaxes import GeoAxes
		from cartopy.util import add_cyclic_point
		import numpy as np
		import warnings
		warnings.filterwarnings("ignore")

		fig = plt.figure(figsize=(15, 6), dpi=100)

		#Add Geo axes to the figure with the specified projection (PlateCarree)
		projection = ccrs.PlateCarree()
		ax = plt.axes(projection=projection)

		#Draw coastline and gridlines
		ax.coastlines()

		gl = ax.gridlines(crs=projection, draw_labels=True, linewidth=1, color='black', alpha=0.9, linestyle=':')
		gl.xlabels_top = False
		gl.ylabels_right = False

		#Wraparound points in longitude
		var_cyclic, lon_cyclic = add_cyclic_point(var, coord=np.asarray(lon))
		x, y = np.meshgrid(lon_cyclic,lat)

		#Define color levels for color bar
		levStep = (np.nanmax(var)-np.nanmin(var))/20
		clevs = np.arange(np.nanmin(var),np.nanmax(var)+levStep,levStep)

		#Set filled contour plot
		cnplot = ax.contourf(x, y, var_cyclic, clevs, transform=projection,cmap=plt.cm.Oranges)
		plt.colorbar(cnplot,ax=ax)

		ax.set_aspect('auto', adjustable=None)

		plt.title('Summer Days (year '+str(i)+')')
		plt.savefig(img+str(i)+'.png', dpi=fig.dpi, bbox_inches='tight')
		plt.close()
		
		images.append(imageio.imread(img+str(i)+'.png')) 
		try:
			os.remove(img+str(i)+'.png')
		except:
			pass

		
	args = { 'duration': 1 }
	imageio.mimsave('/data/output/summer_days_2011_2013.gif', images, 'gif', **args)




if __name__ == "__main__":
	main()

