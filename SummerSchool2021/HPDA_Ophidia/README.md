# ESiWACE2 Summer School on Effective HPC for Climate and Weather

### Wednesday, 25 August, 2021

## High-Performance Data Analytics with Ophidia: tutorial outline

Requirements for the tutorial: Docker, git command line and a web browser 

### Setup the environment

To run this tutorial first retrieve the Ophidia training image from DockerHub:

```
$ docker pull ophidiabigdata/ophidia-training:latest
```

This image includes the full Ophidia software stack, a Jupyter Notebook server and a set of scientific Python modules. Additional information on the image: https://hub.docker.com/r/ophidiabigdata/ophidia-training

Download the tutorial material:

```
$ https://github.com/ESiWACE/hpda-vis-training
```

The tutorial requires some NetCDF files. To download the data run:

```
$ cd hpda-vis-training/SummerSchool2021/HPDA_Ophidia
$ ./get_data.sh
```

You should now see two CMIP5 NetCDF files under the git repository folder.

### Start the environment


From the same folder start the container, binding the tutorial material repo path ($PWD): 

```
$ sudo docker run --rm -it -v $PWD:/home/ophidia/notebooks ophidiabigdata/ophidia-training:latest
```

Now copy the URL showed in the log message (e.g., http://172.17.0.2:8888/) in your browser to open the Jupyter Notebook UI. Type ‘ophidia’ as password when prompted. The notebooks will be available under the ```notebooks``` folder in the Jupyter Notebook UI.

### Tutorial Notebooks

In this folder you can find the tutorial notebook [**PyOphidia_Basics.ipynb**](./PyOphidia_Basics.ipynb), which provides step-by-step instructions on how to use the main Ophidia operators with the PyOphidia module.

The folder contains also a set of noteboks showing different examples of how the Ophidia features can be used.

- [**Daily Temperature Range**](./Daily_Temperature_Range.ipynb) shows how to compute the Daily Temperature Range climate indicator;
- [**Frost Days**](./Frost_Days.ipynb) shows how to compute the Frost Days indicator;
- [**Linear regression**](./Linear_regression.ipynb) shows how to perform a linear regression on a time series from an Ophidia datacube;
- [**Summer Days**](./Summer_Days.ipynb) shows how to compute the Summer Days indicator;
- [**Time series extraction**](./Time_series_extraction.ipynb) shows how to plot on a map a time series from an Ophidia datacube;

### Useful links

1. [Summer School Website](https://hps.vi4io.org/events/2021/esiwace-school)
2. [Ophidia website](http://ophidia.cmcc.it/)
3. [Ophidia on Github](https://github.com/OphidiaBigData)
4. [Ophidia Docs](http://ophidia.cmcc.it/documentation/)
5. [PyOphidia](https://github.com/OphidiaBigData/PyOphidia/)
6. [Tutorial material](https://github.com/ESiWACE/hpda-vis-training/tree/master/SummerSchool2021/HPDA_Ophidia)
7. [ESiWACE project](https://www.esiwace.eu/)
