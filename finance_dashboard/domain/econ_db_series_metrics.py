
from typing import Tuple
import pandas as pd
import streamlit as st

@st.cache_data(ttl=24 * 60)
def get_series_headline_metric(df : pd.DataFrame, lag : int = 1, relative_change=True) -> Tuple[float, float]:
    latest_row = df.iloc[-1]

    latest_value = latest_row.values[0]

    penultimate_row = df.iloc[-lag - 1]

    penultimate_value = penultimate_row.values[0]

    if relative_change:
        change = latest_value / penultimate_value
    else:
        change = latest_value - penultimate_value

    return (latest_value, change)