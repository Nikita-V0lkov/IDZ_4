from graphics_show import *
import streamlit as st
import pandas as pd


graphs_choose = pd.DataFrame({'first column': ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']})
graph_option = st.sidebar.selectbox('Select graphs', graphs_choose['first column'], key=2)
line_choose = pd.DataFrame({'first column': ['lines', 'markers', 'lines+markers', 'bar']})
line_options = st.sidebar.selectbox('Select graph type', line_choose['first column'], key=3)
show_choose = pd.DataFrame({'first column': ['Last month', 'Last year', 'Manually']})
show_option = st.sidebar.selectbox('Select time period', show_choose['first column'], key=1)


def main_menu():
    yf_company_name = ['AMZN', 'GOOG', 'MSFT', 'TSLA']
    show_graphics(yf_company_name, show_option)


def graph_type_choose():
    """
    Function returns the graphic option selected in select box

    Returns
    -------
    :return graph_option : str
        Graphic option selected in select box
    """
    return graph_option


def graph_line_choose():
    """
    Function returns the line option selected in select box

    Returns
    -------
    :return line_options : str
        Line option selected in select box
    """
    return line_options
