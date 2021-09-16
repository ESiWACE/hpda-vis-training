#!/bin/bash

# Script to download some CMIP5 data used in the tutorial from ESGF

wget 'http://esgf-node.cmcc.it/thredds/fileServer/esg_dataroot/cmip5/output1/CMCC/CMCC-CESM/rcp85/day/atmos/day/r1i1p1/v20170725/tasmin/tasmin_day_CMCC-CESM_rcp85_r1i1p1_20960101-21001231.nc'

wget 'http://esgf-node.cmcc.it/thredds/fileServer/esg_dataroot/cmip5/output1/CMCC/CMCC-CESM/rcp85/day/atmos/day/r1i1p1/v20170725/tasmax/tasmax_day_CMCC-CESM_rcp85_r1i1p1_20960101-21001231.nc'

# Download same tasmax file but already split in the 5 years

wget 'https://ophidialab.cmcc.it/thredds/fileServer/public/hpda_training_2021/tasmax_day_CMCC-CESM_rcp85_r1i1p1_20960101-20961231.nc'

wget 'https://ophidialab.cmcc.it/thredds/fileServer/public/hpda_training_2021/tasmax_day_CMCC-CESM_rcp85_r1i1p1_20970101-20971231.nc'

wget 'https://ophidialab.cmcc.it/thredds/fileServer/public/hpda_training_2021/tasmax_day_CMCC-CESM_rcp85_r1i1p1_20980101-20981231.nc'

wget 'https://ophidialab.cmcc.it/thredds/fileServer/public/hpda_training_2021/tasmax_day_CMCC-CESM_rcp85_r1i1p1_20990101-20991231.nc'

wget 'https://ophidialab.cmcc.it/thredds/fileServer/public/hpda_training_2021/tasmax_day_CMCC-CESM_rcp85_r1i1p1_21000101-21001231.nc'
