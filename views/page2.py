
# Dash packages
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker = dict(      # change the marker style
        size = 12,
        color = 'rgb(51,204,153)',
        symbol = 'pentagon',
        line = dict(
            width = 2,
        )
    )
)]
layout = go.Layout(
    title = 'Random Data Scatterplot', # Graph title
    xaxis = dict(title = 'Some random x-values'), # x-axis label
    yaxis = dict(title = 'Some random y-values'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig1 = go.Figure(data=data, layout=layout)


# obtain x and y values:
random_x2 = np.random.randn(1000) # normal distribution
random_y2 = np.random.rand(1000)  # uniform distribution

# define a data variable
data2 = [go.Scatter(
    x = random_x2,
    y = random_y2,
    mode = 'markers',
)]

# define the layout, and include a title and axis labels
layout2 = go.Layout(
    title = 'Random Data Scatterplot', # Graph title
    xaxis = dict(title = 'Normal distribution'), # x-axis label
    yaxis = dict(title = 'Uniform distribution'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)

# Create a fig from data and layout, and plot the fig
fig2 = go.Figure(data=data2, layout=layout2)

###############################################################################
########### PAGE 2 LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Scatterplot Type 1"], className="display-5"),
                                        html.P(
                                                "This scatterplot aims to show the distribution of some random numbers.",
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='scatter1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Scatterplot Type 2"], className="display-5"),
                                        html.P(
                                                "This scatterplot aims to show different type of distributions - \
                                                the Gaussian distribution (or the bell curve) on the x-axis, and the uniform distribution on the y-axis.",
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='scatter2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),

                        ])
                ])

