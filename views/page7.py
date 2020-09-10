
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


df1 = pd.read_csv('assets/mpg.csv')

data1 = [go.Histogram(
    x=df1['mpg']
)]

layout1 = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig1 = go.Figure(data=data1, layout=layout1)



###############################################################################
########### GRAPH 2 ###########
###############################################################################

df2 = pd.read_csv('assets/mpg.csv')

data2 = [go.Histogram(
    x=df2['mpg'],
    # size is the key:
    xbins=dict(start=8,end=50,size=6),
)]

layout2 = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig2 = go.Figure(data=data2, layout=layout2)


###############################################################################
########### GRAPH 3 ###########
###############################################################################

df3 = pd.read_csv('assets/mpg.csv')

data3 = [go.Histogram(
    x=df3['mpg'],
    # size is the key:
    xbins=dict(start=8,end=50,size=1),
)]

layout3 = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig3 = go.Figure(data=data3, layout=layout3)


###############################################################################
########### GRAPH 4 ###########
###############################################################################

df4 = pd.read_csv('assets/arrhythmia.csv')

data4 = [go.Histogram(
    x=df4[df4['Sex']==0]['Height'],
    opacity=0.75,
    name='Male'
),
go.Histogram(
    x=df4[df4['Sex']==1]['Height'],
    opacity=0.75,
    name='Female'
)]

layout4 = go.Layout(
    barmode='overlay',
    title="Height comparison by gender"
)
fig4 = go.Figure(data=data4, layout=layout4)



###############################################################################
########### GRAPH 5 ###########
###############################################################################

import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.rand(200) + 2
x4 = np.random.randn(200) + 4

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig5 = ff.create_distplot(hist_data, group_labels, bin_size=.2)



###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Histogram 1"], className="display-5"),
                                        html.P([
                                                "A histogram is representation of the distribution of numerical data, \
                                                where the data are binned and the count for each bin is represented.",
                                                ""
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("This histogram looks back at the mpg dataset."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 1}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='hist 1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":2}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Histogram 2"], className="display-5"),
                                        html.P([
                                                "This is a wider histogram.",
                                                ""
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='hist 2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),
                        
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Histogram 3"], className="display-5"),
                                        html.P([
                                                "This is a narrower histogram showing a little more rougher and detailed nature of the dataset.",
                                                ""
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("This histogram also looks back at the mpg dataset."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 1}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='hist 3',
                                                        figure=fig3
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":2}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Histogram 4"], className="display-5"),
                                        html.P([
                                                "This is the popular double histogram.",
                                                "This graph shows the height difference of a group of customers by gender. "
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("The dark red area in the middle is the overlapping area of the two."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='hist 4',
                                                        figure=fig4
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Multiple Displot"], className="display-5"),
                                        html.P([
                                                "This is combining several representations in the same plot.", html.Br(),
                                                "Fancy isn't it!"
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P(""),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='hist 5',
                                                        figure=fig5
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),


                        ])
                ])

