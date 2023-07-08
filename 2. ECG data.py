# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:18:15 2022

@author: user
"""

import pandas as pd
# Loading the the survival un-employment data
ECG = pd.read_excel("C:/Users/user/OneDrive/Desktop/py 2/Survival Analytics/Assign/ECG_Surv.xlsx")
ECG.head()
ECG.isna().sum()

ECG = ECG.dropna(how='all')
ECG.survival_time_hr.isnull().sum()

#EDA
ECG.describe()

ECG["survival_time_hr"].describe()

# survival_time_hr is referring to time 
T = ECG.survival_time_hr

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(T, event_observed=ECG.alive)

kmf.plot()

# Over Multiple groups 
# For each group, here group is group
ECG.group.value_counts()

# Applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[ECG.group==1], ECG.alive[ECG.group==1], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and Events for the group "0"
kmf.fit(T[ECG.group==2], ECG.alive[ECG.group==2], label='2')
ay=kmf.plot()

# Applying KaplanMeierFitter model on Time and Events for the group "0"
kmf.fit(T[ECG.group==3], ECG.alive[ECG.group==3], label='3')
az=kmf.plot()
