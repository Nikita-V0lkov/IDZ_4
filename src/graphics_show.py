import streamlit as st
from generate_subplot import *
from datetime import *


def show_graphics(yf_company_name, show_opt):
    """
    Function writes graphs depending on the specified time period

    Parameters
    ----------
    :param yf_company_name: list
        Company name list
    :param show_opt: str
        Period presets
    """
    if show_opt == 'Last month':
        st.write(generate_subplot(yf_company_name, '1mo'))

    if show_opt == 'Last year':
        st.write(generate_subplot(yf_company_name, '1y'))

    if show_opt == 'Manually':
        start_date = st.sidebar.date_input('Pick a date from', date.today() - timedelta(days=30))
        end_date = st.sidebar.date_input('Pick a date to')
        st.write(generate_subplot_manual(yf_company_name, start_date, end_date))
