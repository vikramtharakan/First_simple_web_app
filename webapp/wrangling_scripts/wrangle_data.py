import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    graph_one = []    
        
    df = pd.read_csv('data/global_results.csv')
    df.columns = ['year','averageTemp']
    graph_one.append(
      go.Scatter(
      x = df.year.tolist(),
      y = df.averageTemp.tolist(),
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'World Yearly Temperature Averages',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Temperature'),
                )
   
    # second chart plots ararble land for 2015 as a bar chart    
    graph_two = []
    df2 = pd.read_csv('data/sf_results.csv')
    df2.columns = ['year_sf','averageTemp_sf', 'decade_rolling_average']
    graph_two.append(
      go.Scatter(
      x = df2.year_sf.tolist(),
      y = df2.decade_rolling_average.tolist(),
      mode = 'lines',
      )
    )

    layout_two = dict(title = 'San Francisco Yearly Temperature Averages',
                xaxis = dict(title = 'Year',),
                yaxis = dict(title = 'Temperature'),
                )
    


    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))

    return figures