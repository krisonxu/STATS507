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

# ### **Kailan Xu**  
# ### kailanxu@umich.edu
# ***

# ***
# ## Question 0 - Topics in Pandas [25 points]

# ### *Working with missing data*

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



