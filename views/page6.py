
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


snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data1 = [
    go.Box(
        y=snodgrass,
        name='QCS'
    ),
    go.Box(
        y=twain,
        name='MT'
    )
]
layout1 = go.Layout(
    title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain'
)
fig1 = go.Figure(data=data1, layout=layout1)




###############################################################################
########### GRAPH 2 ###########
###############################################################################

# create a DataFrame from the .csv file:
df2 = pd.read_csv('assets/abalone.csv')

# take two random samples of different sizes:
a = np.random.choice(df2['rings'],30,replace=False)
b = np.random.choice(df2['rings'],100,replace=False)

# create a data variable with two Box plots:
data2 = [
    go.Box(
        y=a,
        name='A'
    ),
    go.Box(
        y=b,
        name='B'
    )
]

# add a layout
layout2 = go.Layout(
    title = 'Comparison of two samples taken from the same population'
)

# create a fig from data & layout, and plot the fig
fig2 = go.Figure(data=data2, layout=layout2)




###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Boxplot 1"], className="display-5"),
                                        html.P([
                                                "A box plot is a statistical representation of numerical data through their quartiles.\
                                                The ends of the box represent the lower and upper quartiles, \
                                                while the median (second quartile) is marked by a line inside the box.",
                                                ""
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Obviously the statistical data of MT is asymmetrical and to the left."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='boxplot graph 1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Boxplot 2"], className="display-5"),
                                        html.P([
                                                "This boxplot 2 is comparing two samples taken from the same population of an abalone dataset.",
                                                "Clearly outliners exist in both samples."
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("The Original owners of the database is Marine Resources Division of the Australia Government. The number of instances is 4177."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='boxplot graph 2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),

                        ])
                ])

