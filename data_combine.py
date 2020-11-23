# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:12:30 2020

@author: jayka
"""

import pandas as pd
import numpy as np

y = np.zeros([150,450])#Initialize dataset array
z=0#iterator for array
#Normal-Day-1 append
for i in range(1,51):
    str0 = 'E:\\3-1\\Formal Project\\Normal Breath data\\'
    str1 = 'NB'
    str2 = str(i)
    str3 = '.xlsx'
    str4 = str0 + str1 + str2 + str3
    
    x1 = pd.read_excel(str4,skiprows=1,header=None)
    y1 = x1.to_numpy()[:,2]    
    y[z,:] = y1
    z=z+1


#Normal-Day-2 append
for i in range(1,51):
    str0 = 'E:\\3-1\\Formal Project\\Normal Breath data\\06-11-20\\'
    str1 = 'NB'
    str2 = str(i)
    str3 = '.xlsx'
    str4 = str0 + str1 + str2 + str3
    
    x1 = pd.read_excel(str4,skiprows=1,header=None)
    y1 = x1.to_numpy()[:,2]    
    y[z,:] = y1
    z=z+1

##############End of Normal data###########
#############Start slow data##############
'''###Do not uncomment, will give valueerror and fileerror due to inconsistent file-naming
#Slow-Day-1-append
for i in range(1,51):
    str0 = 'E:\\3-1\\Formal Project\\Slow Breath data\\'
    str1 = 'NB'
    str2 = str(i)
    str3 = '.xlsx'
    str4 = str0 + str1 + str2 + str3
    
    x1 = pd.read_excel(str4,skiprows=1,header=None)
    y1 = x1.to_numpy()[:,2]    
    y[z,:] = y1
    z=z+1
'''
#Slow-Day-2-append
for i in range(1,51):
    str0 = 'E:\\3-1\\Formal Project\\Slow Breath data\\07-11-20\\'
    str1 = 'SB'
    str2 = str(i)
    str3 = '.xlsx'
    str4 = str0 + str1 + str2 + str3
    
    x1 = pd.read_excel(str4,skiprows=1,header=None)
    y1 = x1.to_numpy()[:,2]    
    y[z,:420] = y1[:420]
    z=z+1

########Slow over########

##Trim down the dataset
##Since slow breath data is 420 timesteps,have to trim data down

data = y[:,:420]
data_duplicate = data.copy()

#Add classification labels
labels = np.zeros((150,1))
labels[100:150,:] = labels[100:150,:]+1

##Append labels to dataset array
final_data_set = np.append(data_duplicate,labels,axis=1)

#Check result
print(final_data_set)
print(final_data_set.shape)

#Save as CSV file
DF = pd.DataFrame(final_data_set)
DF.to_csv("E:\\3-1\\Formal Project\\data1.csv")

