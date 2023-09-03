# -*- coding: utf-8 -*-
"""
UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
UNIDADE ACADÊMICA DO CABO DE SANTO AGOSTINHO - UACSA

@author(s):
    Rogério Soares (rogerio.soaress@ufrpe.br)
    
Created on Tue May 12 16:49:17 2020
"""

import h5py
import numpy as np


# project_name = "Projects/ferrita"
# filename = project_name + ".hdf5"

# # using join() + ord() + format() 
# # Converting String to binary 
# res = ''.join(format(i, 'b') for i in bytearray(filename, encoding ='utf-8')) 

# with h5py.File(filename, 'w') as f:
#     ds_param = f.create_dataset("parameters", (7,))
#     ds_param[0] = 1234.22
    
#     dt = h5py.string_dtype()
#     ds_path = f.create_dataset("path", (100,), dtype=dt)
#     ds_path = np.void(res)
    
    
# with h5py.File(filename, 'r') as f:
#     data = f["parameters"]
#     print("data: ", data[0])
    
#     dpath = f["path"]
#     print(dpath[0:9])
    
#!/usr/bin/env python
'''Writes a NeXus HDF5 file using h5py and numpy'''

import h5py    # HDF5 support
import numpy
import six

print("Write a NeXus HDF5 file")
fileName = "prj_test.hdf5"
timestamp = "2010-10-18T17:17:04-0500"


# create the HDF5 NeXus file
with h5py.File(fileName, "w") as f:
    # point to the default data to be plotted
    f.attrs['default']        = 'entry'
    # give the HDF5 root some more attributes
    f.attrs['file_name']        = fileName
    f.attrs['file_time']        = timestamp
    f.attrs['instrument']       = 'APS USAXS at 32ID-B'
    f.attrs['creator']          = 'BasicWriter.py'
    f.attrs['NeXus_version']    = '4.3.0'
    f.attrs['ha'] = 3.453e-4

print("wrote file:", fileName)


import h5py    # HDF5 support

fileName = "prj_test.hdf5"
with h5py.File(fileName,  "r") as f:

    for item in f.attrs.keys():
        print(item + ":", f.attrs[item])
    

