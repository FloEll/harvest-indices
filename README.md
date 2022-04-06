# harvest-indices

## What is it?

**harvest-indices** is a Python package to calculate harvest anomalies from historical harvest data. It works really well with 1D-time series of annual harvest data (e.g. productivity records in dt/ha) and can be easily applied in conjunction with the pandas or xarray packages. 

## Main features

The **harvest-indices** Python package allows the calculation of a set of traditional and scientific harvest indices to detect positive and negative harvest anomalies. The indices so far implemented are:
* traditional harvest indices **THI** (frequently used by central European farmers)
* Standardized Harvest Index **SHI** (that we developed to analyze the harvest data base [cropdata.de](https://cropdata.de/) )
* Relative Harvest Index **RHI** (similar as e.g. in Ben-Ari et al (2018) and Beillouin et al. (2020))

## Where to get it

The source code is currently hosted on GitHub at: https://github.com/FloEll/harvest-indices

It can be installed using pip:

`pip install harvest-indices`

## Dependencies

The [NumPy](https://pypi.org/project/numpy/), [pandas](https://pypi.org/project/pandas/) and [statsmodel](https://pypi.org/project/statsmodels/) packages are (if not already available) installed automatically when installing harvest-indices.

When working with netCDF data it is also useful to install the [netcdf4](https://pypi.org/project/netCDF4/) and [xarray](https://pypi.org/project/xarray/) packages. 

## Licence

[MIT Licence](https://choosealicense.com/licenses/mit/)

## Background

The work on **harvest-indices** started in the [CROP project](https://www.uni-giessen.de/fbz/zentren/zeu/activities/researchprojects/CROP) at Justus-Liebig-University of Gießen in 2022. The idea was to have a simple and standardized way of assessing harvest anomalies from historical harvest data.

## Discussion and Development

If you are missing a feature or an index, did you find a bug or an error in the code or do you just have a great idea of how to improve this package, please write an email at info@cropdata.de or open an issue at https://github.com/FloEll/harvest-indices/issues

## How to cite

We are currently working on a manuscript that will also cover this package. Until then you can use the following citation: Florian Ellsäßer, 2022, harvest-indices python package to analyze harvest anomalies, https://pypi.org/project/harvest-indices/ 
