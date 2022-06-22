import plotly.graph_objects as go
import main_menu as mm


def fig_scatter(table, graph_opt, t_name, line_opt):
    """
    Function returns generated scatter using values

    Parameters
    ----------
    :param table : dataframe
        Company data to describe x axes
    :param graph_opt : str
        Graphics type
    :param t_name : str
        Name of data table
    :param line_opt : str
        Option to choose line type

    Returns
    -------
    :return fig : scatter
        Created scatter
    """

    if line_opt == 'bar':
        index_table = table.reset_index()
        fig = go.Bar(x=index_table['Date'],
                     y=table[graph_opt],
                     name=t_name)
        return fig
    else:
        index_table = table.reset_index()
        fig = go.Scatter(x=index_table['Date'],
                         y=table[graph_opt],
                         mode=line_opt,
                         name=t_name)
        return fig


def table_subplot(company_list, company_name):
    """
    Creates graphs using companies data tables

    Parameters
    ----------
    :param company_list : list
        Companies data list
    :param company_name : list
        Company name list

    Returns
    -------
    :return fig : figure
        Created graphic
    """

    fig = go.Figure()
    for i in range(len(company_list)):
        fig.add_trace(fig_scatter(company_list[i], mm.graph_type_choose(), company_name[i], mm.graph_line_choose()))
    fig.update_layout(height=700, width=800, title=mm.graph_type_choose(), xaxis_title='Date', yaxis_title='USD')
    return fig
