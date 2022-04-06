# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:42:23 2022

@author: Florian Ellsäßer
"""

import setuptools

setuptools.setup(name='harvest-indices',
      version='0.0.2',
      description='Calculate harvest anomalies from historical harvest data.',
      author='Florian Ellsäßer',
      author_email='info@cropdata.de',
      url='cropdata.de',
      project_urls={
        'Documentation': 'https://readthedocs.org/projects/harvest-indices/',
        'Source': 'https://github.com/FloEll/harvest-indices',
        'Tracker': 'https://github.com/FloEll/harvest-indices/issues',
      },
      license='MIT',
      packages=['harvest_indices'],
      install_requires=[
          'numpy','pandas','statsmodels'
      ]
      )
