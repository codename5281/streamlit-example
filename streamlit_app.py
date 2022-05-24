from collections import namedtuple
from multiprocessing.sharedctypes import Value
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from pcse.db import NASAPowerWeatherDataProvider
import plotly.express as px
import datetime

"""
# NN-ET0
## récupération des données
"""

latitude = st.number_input("latitude", value=43.610769)
longitude = st.number_input("longitude", value=3.876716)

st.map(pd.DataFrame({"lat":latitude,"lon":longitude}))


st.write("latitude: %s, longitude: %s" % (np.round(latitude,2),np.round(longitude,2)))

if st.button('load data'):
    st.write('Loading data')
    weatherdata = NASAPowerWeatherDataProvider(longitude,latitude,force_update=True) 
    
    df = pd.DataFrame(weatherdata.export())
    # converting PCSE units : cm to mm
    df["ET0"]=df["ET0"]*10 
    df["year"] = df.apply(lambda x: x["DAY"].year, axis=1)
    
    df["julian_day"] = df.apply(lambda x: (x["DAY"] - datetime.date(x["year"],1,1)).days, axis=1)
    
    df_2 = df[df["year"]>2012]

    fig = px.line(df_2, x="julian_day", y="ET0", color='year')
    st.plotly_chart(fig, use_container_width=True)

else:
    pass

"""
## entraînement du modèle
"""

