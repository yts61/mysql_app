
# Dash packages
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np


###############################################################################
########### GRAPH 1 ###########
###############################################################################


df = pd.read_csv('assets/nst-est2017-alldata.csv')
# Alternatively:
# df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')

# grab just the six New England states:
df = df[df['DIVISION']=='1']
# set the index to state name:
df.set_index('NAME', inplace=True)
# grab just the population columns:
df = df[[col for col in df.columns if col.startswith('POP')]]

traces=[go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df.index]

layout = go.Layout(
    title = 'Population Estimates of the Six New England States'
)

fig1 = go.Figure(data=traces,layout=layout)



###############################################################################
########### GRAPH 2 ###########
###############################################################################

# Create a pandas DataFrame from 2010YumaAZ.csv
df2 = pd.read_csv('assets/2010YumaAZ.csv')

# Define a data variable
data2 = [{
    'x': df2['LST_TIME'],
    'y': df2[df2['DAY']==day]['T_HR_AVG'],
    'name': day
} for day in df2['DAY'].unique()]

# Define the layout
layout2 = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig2 = go.Figure(data=data2, layout=layout2)




###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Scatter-Line Chart 1"], className="display-5"),
                                        html.P([
                                                "This line chart is illustrating the population estimates of the 6ix new England States in the US.",
                                                "The growth of each of them are steady, while Massachusett has the highest rate."
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='Line graph 1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Line Chart 2"], className="display-5"),
                                        html.P([
                                                "This line chart number 2 is showing the daily temperatures from June 1-7, 2010 in Yuma, Arizona",
                                                "Obviously it is the hottest from Friday to Sunday in that particular week."
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='Line graph 2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),

                        ])
                ])

