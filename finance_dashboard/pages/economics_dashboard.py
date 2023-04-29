import streamlit as st
from finance_dashboard.domain.econ_db_series_metrics import get_series_headline_metric
from finance_dashboard.domain.formatter import percent, percent_from_ratio, pounds, quarter
from finance_dashboard.services.econdb.series import get_open_db_series
from finance_dashboard.enums.econdb import EconDBSeries


def economics_dashboard():

    st.title('UK Economics Dashboard')
    col1, col2, col3 = st.columns(3)    
    with col2:
        base_rate_df = get_open_db_series(EconDBSeries.BOE_BASE_RATE)
        latest_value, change = get_series_headline_metric(base_rate_df, 1, False)
        st.metric('BoE Base Rate', percent(latest_value, 2), percent(change, 2), "inverse")


    col1, col2, col3 = st.columns(3)

    with col1:

        gdp_df = get_open_db_series(EconDBSeries.GDP)
        latest_value,change = get_series_headline_metric(gdp_df, 4)
        st.metric('UK GPD', pounds(latest_value, "m"), percent(change))

        st.write(f'Max Date : {quarter(gdp_df.index.max())}')
        st.line_chart(gdp_df)
        st.download_button('Download', gdp_df.to_csv().encode('utf-8'), file_name=f'gdp_data.csv')


    with col2:
        cpi_df = get_open_db_series(EconDBSeries.CPI)
        latest_value,change = get_series_headline_metric(cpi_df, 12)
        st.metric('UK CPI', latest_value, percent_from_ratio(change), "inverse")
        st.write(f'Max Date : {quarter(cpi_df.index.max())}')
        st.line_chart(cpi_df)
        st.download_button('Download', cpi_df.to_csv().encode('utf-8'), file_name=f'cpi_data.csv')

    with col3:
        unemployment_df = get_open_db_series(EconDBSeries.UNEMPLOYMENT)
        latest_value,change = get_series_headline_metric(unemployment_df, 12)
        st.metric('UK Unemployment', percent(latest_value), percent_from_ratio(change), "inverse")
        st.write(f'Max Date : {quarter(unemployment_df.index.max())}')
        st.line_chart(unemployment_df)
        st.download_button('Download', unemployment_df.to_csv().encode('utf-8'), file_name=f'unemployment_data.csv')






    metric = st.selectbox('Choose metric', [e.value for e in EconDBSeries]
    )
    df = get_open_db_series(metric)
    st.line_chart(df)
    st.download_button('Download', df.to_csv().encode('utf-8'), file_name=f'{metric}_data.csv')
