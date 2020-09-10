
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

df1 = pd.read_csv('assets/2018WinterOlympics.csv')

trace11 = go.Bar(
    x=df1['NOC'],  # NOC stands for National Olympic Committee
    y=df1['Gold'],
    name = 'Gold',
    marker=dict(color='#FFD700') # set the marker color to gold
)
trace12 = go.Bar(
    x=df1['NOC'],
    y=df1['Silver'],
    name='Silver',
    marker=dict(color='#9EA0A1') # set the marker color to silver
)
trace13 = go.Bar(
    x=df1['NOC'],
    y=df1['Bronze'],
    name='Bronze',
    marker=dict(color='#CD7F32') # set the marker color to bronze
)
data1 = [trace11, trace12, trace13]
layout1 = go.Layout(
    title='2018 Winter Olympic Medals by Country',
    barmode='stack'
)
fig1 = go.Figure(data=data1, layout=layout1)



###############################################################################
########### GRAPH 2 ###########
###############################################################################

# create a DataFrame from the .csv file:
df2 = pd.read_csv('assets/mocksurvey.csv',index_col=0)

# create traces using a list comprehension:
data2 = [go.Bar(
    y = df2.index,     # reverse your x- and y-axis assignments
    x = df2[response],
    orientation='h',  # this line makes it horizontal!
    name=response
) for response in df2.columns]

# create a layout, remember to set the barmode here
layout2 = go.Layout(
    title='Mock Survey Results',
    barmode='stack'
)

# create a fig from data & layout, and plot the fig.
fig2 = go.Figure(data=data2, layout=layout2)




###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Bar Chart 1"], className="display-5"),
                                        html.P([
                                                "This bar chart is describing the amount of medals won by country in 2018 Winter Olympic.",
                                                "Clearly, Norway is the biggest winner, while Germany and Canada are the first runner up and 2nd runner up respectively."
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P(["Don't forget to hover around and play with the interactive graph!",
                                                "You won't mess up the chart, there is a little house icon on the top right hand corner to reset!"]),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='bar graph 1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Bar Chart 2"], className="display-5"),
                                        html.P([
                                                "Wanna check out how is it when comes to survey? Here it is.",
                                                "This is a survey result of 3 mock questions. Apparently quiestion 1 is dominated by Strongly Agree, while more than 50% disagreeing Question 3 "
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='bar graph 2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),

                        ])
                ])

