import pandas as pd
import streamlit as st
from finance_dashboard.enums.econdb import EconDBSeries

OPENDB_PUBLIC_API_TOKEN = '3072d2f702b16c95c3e1a1aeb95e3d21fefc0292'

st.cache_data(ttl=60*60)
def get_open_db_series(series : EconDBSeries):

    df = pd.read_csv(
        f'https://www.econdb.com/api/series/{series}/?token=%s&format=csv' % OPENDB_PUBLIC_API_TOKEN,
        index_col='Date', parse_dates=['Date'])
    
    return df 