from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from pcse.db import NASAPowerWeatherDataProvider

"""
# NN-ET0
"""

latitude = st.number_input("latitude")
longitude = st.number_input("longitude")


st.write("latitude: %s, longitude: %s" % (np.round(latitude,2),np.round(longitude,2)))

if st.button('load data'):
    st.write('Loading data')
    weatherdata = NASAPowerWeatherDataProvider(longitude,latitude,force_update=True) 
    
    df = pd.DataFrame(weatherdata.export())
    # converting PCSE units : cm to mm
    df["ET0"]=df["ET0"]*10 
    df["year"] = df.apply(lambda x: x["DAY"].year, axis=1)
    
    df_2 = df[df["year"]==2021]
    df_2

else:
    pass