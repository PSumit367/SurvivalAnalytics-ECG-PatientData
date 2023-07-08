# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:59:55 2022

@author: user
"""

# pip install lifelines
# import lifelines

import pandas as pd

patient = pd.read_csv("C:/Users/user/OneDrive/Desktop/py 2/Survival Analytics/Assign/Patient.csv")
patient.head()
patient.describe()

patient["Followup"].describe()

# Spell is referring to time 
T = patient.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(T, event_observed=patient.Eventtype)

# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is Scenario
patient.Scenario.value_counts()

# Applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[patient.Scenario=="A"], patient.Eventtype[patient.Scenario=="A"], label="A")
ax = kmf.plot()


