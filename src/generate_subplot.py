import yfinance as yf
from output import *


def generate_subplot(yf_company_name, chosen_date):
    """
    Function returns the subplot scatter for preset date choose

    Parameters
    ----------
    :param yf_company_name : list
        Company name list
    :param chosen_date : str
        Selected time period

    Returns
    -------
    :return subplot_fig : scatter
        Created scatter to trace
    """
    company_data_list = []
    company_name = []
    for i in range(len(yf_company_name)):
        company_name.append(yf.Ticker(yf_company_name[i]).info.get('longName'))
        company_data_list.append(yf.download(yf_company_name[i], period=chosen_date))
    subplot_fig = table_subplot(company_data_list, company_name)
    return subplot_fig


def generate_subplot_manual(yf_company_name, st_date, ed_date):
    """
    Function returns the subplot scatter for manual date choose

    Parameters
    ----------
    :param yf_company_name: list
        Company name list
    :param st_date: datetime
        Period start date
    :param ed_date: datetime
        Period end date

    Returns
    -------
    :return subplot_fig: scatter
        Created scatter to trace
    """
    company_data_list = []
    company_name = []
    for i in range(len(yf_company_name)):
        company_name.append(yf.Ticker(yf_company_name[i]).info.get('longName'))
        company_data_list.append(yf.download(yf_company_name[i], start=st_date, end=ed_date))
    subplot_fig = table_subplot(company_data_list, company_name)
    return subplot_fig
