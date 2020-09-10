
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

# Add columns to the DataFrame to convert model year to a string and
# then combine it with name so that hover text shows both:
df1['text1']=pd.Series(df1['model_year'],dtype=str)
df1['text2']="'"+df1['text1']+" "+df1['name']

data1 = [go.Scatter(
            x=df1['horsepower'],
            y=df1['mpg'],
            text=df1['text2'],  # use the new column for the hover text
            mode='markers',
            marker=dict(size=1.5*df1['cylinders'])
    )]
layout1 = go.Layout(
    title='Vehicle mpg vs. horsepower',
    hovermode='closest'
)
fig1 = go.Figure(data=data1, layout=layout1)



###############################################################################
########### GRAPH 2 ###########
###############################################################################

# create a DataFrame from the .csv file:
df2 = pd.read_csv('assets/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data2 = [go.Scatter(
    x=df2['displacement'],
    y=df2['acceleration'],
    text=df2['name'],
    mode='markers',
    marker=dict(size=df2['weight']/500)
)]

# create a layout with a title and axis labels
layout2 = go.Layout(
    title='Vehicle acceleration vs. displacement',
    xaxis = dict(title = 'displacement'),
    yaxis = dict(title = 'acceleration = seconds to reach 60mph'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig2 = go.Figure(data=data2, layout=layout2)
#######
# So what happened?? Why is the trend sloping downward?
# Remember that acceleration is the number of seconds to go from 0 to 60mph,
# so fewer seconds means faster acceleration!
######





###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Bubble Chart 1"], className="display-5"),
                                        html.P([
                                                "A bubble chart is a scatter plot in which a third dimension of the data is shown through the size of markers.",
                                                "Which car is your favourite?"
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("This bubble chart is showing the relationship of MPG and horsepower. MPG stands for miles per gallon."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='bubble graph 1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Bubble Chart 2"], className="display-5"),
                                        html.P([
                                                "This 2nd bubble chart is describing the vehicle acceleration and the displacement relationship from the same dataset.",
                                                ""
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Why is the trend sloping downward? Remember that acceleration is the number of seconds to go from 0 to 60mph, \
                                                so fewer seconds means faster acceleration!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='bubble graph 2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),

                        ])
                ])

