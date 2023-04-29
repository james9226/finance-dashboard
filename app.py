import streamlit as st

from finance_dashboard.pages.economics_dashboard import economics_dashboard


st.set_page_config(
    page_title="Finance Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={"About": "# This is a header. This is an *extremely* cool app!"},
)

economics_dashboard()