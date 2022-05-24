from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from pcse.db import NASAPowerWeatherDataProvider

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
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
        df


 else:
     pass