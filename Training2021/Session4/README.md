# ESiWACE2 Online Training on High Performance Data Analaytics and Visualisation

## Session 4 - Advanced Ophidia concepts

### Thursday, 16 September, 2021

## Data Analytics Workflows with Ophidia: outline

This README provides the outline for Session4 of the training course. The session is organized as:

1. Introduction to scientific workflows, workflows features in the Ophidia framework and real-world examples 
2. Practical demo tutorial of data analytics workflow with Ophidia
3. Hands-on with some data analytics workflow examples with Ophidia

### Setup the environment

The same environment from Session 3 will be used. If you did not downloaded the container image, follow the next steps.

Requirements for the demo and hands-on parts: Docker, git command line and a web browser 

To run this tutorial first retrieve the Ophidia training image from DockerHub:

```
$ docker pull ophidiabigdata/ophidia-training:latest
```

This image includes the full Ophidia software stack, a Jupyter Notebook server and a set of scientific Python modules. Additional information on the image: https://hub.docker.com/r/ophidiabigdata/ophidia-training

#### Get the training material

Download the tutorial material:

```
$ https://github.com/ESiWACE/hpda-vis-training
```

The tutorial requires some NetCDF files. To download the data run:

```
$ cd hpda-vis-training/Training2021/Session4
$ ./get_data.sh
```

You should now see two CMIP5 NetCDF files under the git repository folder.

#### Start the environment

From the same folder start the container, binding the tutorial material repo path ($PWD): 

```
$ sudo docker run --rm -it -v $PWD:/home/ophidia/notebooks ophidiabigdata/ophidia-training:latest
```

Now copy the URL showed in the log message (e.g., http://172.17.0.2:8888/) in your browser to open the Jupyter Notebook UI. Type ‘ophidia’ as password when prompted. The notebooks will be available under the ```notebooks``` folder in the Jupyter Notebook UI.

### Workflows

In this folder you can find the notebook that will be shown during the practical demo tutorial:

- [**Workflow_Overview.ipynb**](./Workflow_Overview.ipynb) which provides step-by-step instructions on how to define a workflow by a JSON objecto and run it with the PyOphidia module.

Two subfolders are also located under this folder. 

#### Hands-on Notebooks

In the ```Hands-on``` folder you can find the notebooks for the hands-on part:

1. [**Basic_workflow.ipynb**](./Hands-on/1-Basic_workflow.ipynb) which provides step-by-step instructions on how to compose and submit a simple workflow with the PyOphidia interface; 
2. [**Summer_days_workflow.ipynb**](./Hands-on/2-Summer_days_workflow.ipynb) providing an exercise for the implementation of an analysis workflow (a climate indicator) on multiple input NetCDF files
3. [**Selection_interface.ipynb**](./Hands-on/3-Selection_interface.ipynb.ipynb) showing a more complex example about the use of the selection (if/elseif/else) statement.

#### Example Notebooks

The ```Examples``` folder contains a set of ready-to-use noteboks that can be executed if you are interested in seeing additional ways of composing workflows in Ophidia.

- [**DTR.ipynb**](./Examples/DTR.ipynb) shows how to compute the Daily Temperature Range climate indicator as a workflow;
- [**Frost_Days_workflow.ipynb**](./Examples/Frost_Days_workflow.ipynb) shows how to compute the Frost Days indicator as a workflow;
- [**Mult-file_example.ipynb**](./Examples/Mult-file_example.ipynb) shows how to compute a climate analysis on multiple files and combine the results in for a statistical analyis;
- [**Summer_Days_workflow.ipynb**](./Examples/Summer_Days_workflow.ipynb) shows how to compute the Summer Days indicator as a workflow;
- [**Selection_interface_example.ipynb**](./Examples/Selection_interface_example.ipynb) shows how to use the selection interface provided by the Ophidia workflow manager;

### Useful links

1. [HPDA & Visualisation Training Website](https://www.esiwace.eu/events/training-on-high-performance-data-analytics-and-visualisation-in-september-2021)
2. [Ophidia website](http://ophidia.cmcc.it/)
3. [Ophidia on Github](https://github.com/OphidiaBigData)
4. [Ophidia Docs](http://ophidia.cmcc.it/documentation/)
5. [PyOphidia](https://github.com/OphidiaBigData/PyOphidia/)
6. [Tutorial material](https://github.com/ESiWACE/hpda-vis-training/tree/master/Training2021)
7. [ESiWACE project](https://www.esiwace.eu/)
