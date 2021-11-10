# ESiWACE2 Online Training on High Performance Data Analaytics and Visualisation

## Session 3 - Intro to HPDA and Ophidia

### Wednesday, 15 September, 2021

## High-Performance Data Analytics with Ophidia: outline

This README provides the outline for Session3 of the training course. The session is organized as:

1. Introduction to HPDA, data challenges in eScience and the Ophidia HPDA framework
2. Practical demo tutorial of data analytics with PyOphidia
3. Hands-on with some data analytics example notebooks with PyOphidia

### Setup the environment

Requirements for the demo and hands-on parts: Docker, git command line and a web browser 

To run this tutorial first retrieve the Ophidia training image from DockerHub:

```
$ docker pull ophidiabigdata/ophidia-training:v1.6
```

This image includes the full Ophidia software stack, a Jupyter Notebook server and a set of scientific Python modules. Additional information on the image: https://hub.docker.com/r/ophidiabigdata/ophidia-training

Download the tutorial material:

```
$ https://github.com/ESiWACE/hpda-vis-training
```

The tutorial requires some NetCDF files from the CMIP5 archive. In particular a couple of files from the ouput of the CESM model provided by CMCC will be downloaded with the following script from ESGF CMIP5 data nodes. CMIP5 data can be accessed from the ESGF Data Portal CMIP5 project page: https://esgf-node.llnl.gov/search/cmip5/). Please note that CMIP5 data come with the following Terms of Use: https://pcmdi.llnl.gov/mips/cmip5/terms-of-use.html 

To download the data run:

```
$ cd hpda-vis-training/Training2021/Session3
$ ./get_data.sh
```

You should now see two CMIP5 NetCDF files under the git repository folder. 

#### Start the environment

From the same folder start the container, binding the tutorial material repo path ($PWD): 

```
$ sudo docker run --rm -it -v $PWD:/home/ophidia/notebooks ophidiabigdata/ophidia-training:v1.6
```

Now copy the URL showed in the log message (e.g., `http://172.17.0.2:8888/`) in your browser to open the Jupyter Notebook UI. Type ‘ophidia’ as password when prompted. In case the IP address in not reachable, try with `http://localhost:8888/`. The notebooks will be available under the ```notebooks``` folder in the Jupyter Notebook UI.

### Notebooks

In this folder you can find the notebook that will be shown during the practical demo tutorial:

- [**PyOphidia_Basics.ipynb**](./PyOphidia_Basics.ipynb) which provides step-by-step instructions on how to use the main Ophidia operators with the PyOphidia module.

Two subfolders are also located under this folder. 

#### Hands-on Notebooks

In the ```Hands-on/``` folder you can find the notebooks for the hands-on part:

1. [**Basics.ipynb**](./Hands-on/1-Basics.ipynb) which provides step-by-step instructions on how to use the Ophidia operators as well as the PyOphidia library to implement a climate indicator; 
2. [**Summer_Days.ipynb**](./Hands-on/2-Summer_Days.ipynb) providing a simple exercise for the implementation of a climate indicator with PyOphidia. The *2-Summer_Days-filled.ipynb* noteobook shows the same notebook after its execution.
3. [**Linear_Regression.ipynb**](./Hands-on/3-Linear_Regression.ipynb) representing a more challenging exercise, where you can implement a linear regression experiment to extract the trend from the data.  The *3-Linear_Regression-filled.ipynb* noteobook shows the same notebook after its execution.

#### Example Notebooks

The ```Examples/``` folder contains a set of ready-to-use noteboks that can be executed if you are interested in seeing additional ways of exploiting Ophidia.

- [**Daily Temperature Range**](./Examples/Daily_Temperature_Range.ipynb) shows how to compute the Daily Temperature Range climate indicator;
- [**Frost Days**](./Examples/Frost_Days.ipynb) shows how to compute the Frost Days indicator;
- [**Linear regression**](./Examples/Linear_regression.ipynb) shows how to perform a linear regression on a time series from an Ophidia datacube;
- [**Summer Days**](./Examples/Summer_Days.ipynb) shows how to compute the Summer Days indicator;
- [**Time series extraction**](./Examples/Time_series_extraction.ipynb) shows how to plot on a map a time series from an Ophidia datacube;

### Useful links

1. [HPDA & Visualisation Training Website](https://www.esiwace.eu/events/training-on-high-performance-data-analytics-and-visualisation-in-september-2021)
2. [Ophidia website](http://ophidia.cmcc.it/)
3. [Ophidia on Github](https://github.com/OphidiaBigData)
4. [Ophidia Docs](http://ophidia.cmcc.it/documentation/)
5. [PyOphidia](https://github.com/OphidiaBigData/PyOphidia/)
6. [Tutorial material](https://github.com/ESiWACE/hpda-vis-training/tree/master/Training2021)
7. [ESiWACE project](https://www.esiwace.eu/)
