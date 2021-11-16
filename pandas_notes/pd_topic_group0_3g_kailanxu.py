# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#  

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [DataFrame.pct_change()](#DataFrame.pct_change()) 
# + [Working with missing data](#Working-with-missing-data)
#

# ## DataFrame.pct_change()
# *Dongming Yang*

# +
# This function always be used to calculate the percentage change between the current and a prior element, and always be used to a time series     
# The axis could choose the percentage change from row or columns
# Creating the time-series index 
ind = pd.date_range('01/01/2000', periods = 6, freq ='W') 
  
# Creating the dataframe  
df = pd.DataFrame({"A":[14, 4, 5, 4, 1, 55], 
                   "B":[5, 2, 54, 3, 2, 32],  
                   "C":[20, 20, 7, 21, 8, 5], 
                   "D":[14, 3, 6, 2, 6, 4]}, index = ind) 
  
# find the percentage change with the previous row 
df.pct_change()

# find the percentage change with precvious columns 
df.pct_change(axis=1)m

# +
# periods means start to calculate the percentage change between the periods column or row and the beginning

# find the specific percentage change with first row
df.pct_change(periods=3)

# +
# fill_method means the way to handle NAs before computing percentage change by assigning a value to that NAs
# importing pandas as pd 
import pandas as pd 
  
# Creating the time-series index 
ind = pd.date_range('01/01/2000', periods = 6, freq ='W') 
  
# Creating the dataframe  
df = pd.DataFrame({"A":[14, 4, 5, 4, 1, 55], 
                   "B":[5, 2, None, 3, 2, 32],  
                   "C":[20, 20, 7, 21, 8, None], 
                   "D":[14, None, 6, 2, 6, 4]}, index = ind) 
  
# apply the pct_change() method 
# we use the forward fill method to 
# fill the missing values in the dataframe 
df.pct_change(fill_method ='ffill')

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# -

# ## Working with missing data
# *Kailan Xu*

# - Detecting missing data
# - Inserting missing data
# - Calculations with missing data
# - Cleaning / filling missing data
# - Dropping axis labels with missing data

# ### 1. Detecting missing data

# As data comes in many shapes and forms, pandas aims to be flexible with regard to handling missing data. While NaN is the default missing value marker for reasons of computational speed and convenience, we need to be able to easily detect this value with data of different types: floating point, integer, boolean, and general object. In many cases, however, the Python None will arise and we wish to also consider that “missing” or “not available” or “NA”.

# +
import pandas as pd 
import numpy as np 

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=["a", "c", "e", "f", "h"],
    columns=["one", "two", "three"],
)
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
df2
# -

# To make detecting missing values easier (and across different array dtypes), pandas provides the `isna()` and `notna()` functions, which are also methods on Series and DataFrame objects:

df2.isna()

df2.notna()

# ###  2. Inserting missing data

# You can insert missing values by simply assigning to containers. The actual missing value used will be chosen based on the dtype.
# For example, numeric containers will always use NaN regardless of the missing value type chosen:

s = pd.Series([1, 2, 3])
s.loc[0] = None
s

# Likewise, datetime containers will always use NaT.
# For object containers, pandas will use the value given:

s = pd.Series(["a", "b", "c"])
s.loc[0] = None
s.loc[1] = np.nan
s

# ### 3. Calculations with missing data

# - When summing data, NA (missing) values will be treated as zero.
# - If the data are all NA, the result will be 0.
# - Cumulative methods like `cumsum()` and `cumprod()` ignore NA values by default, but preserve them in the resulting arrays. To override this behaviour and include NA values, use `skipna=False`.

df2

df2["one"].sum()

df2.mean(1)

df2.cumsum()

df2.cumsum(skipna=False)

# ### 4. Cleaning / filling missing data

# pandas objects are equipped with various data manipulation methods for dealing with missing data.
# - `fillna()` can “fill in” NA values with non-NA data in a couple of ways, which we illustrate:

df2.fillna(0)

df2["one"].fillna("missing")

# ### 5.Dropping axis labels with missing data

# You may wish to simply exclude labels from a data set which refer to missing data. To do this, use `dropna()`:

df2.dropna(axis=0)



