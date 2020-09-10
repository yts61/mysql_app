
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





###############################################################################
########### GRAPH 2 ###########
###############################################################################





###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Line Chart 1"], className="display-5"),
                                        html.P([
                                                "This line chart is illustrating the population estimates of the 6ix new England States in the US.",
                                                html.Br(),
                                                "The growth of each of them are steady, while Massachusett has the highest rate."
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P([
                                               "Don't forget to hover around and play with the interactive graph!",
                                               html.Br(),
                                               "A"
                                        ]),
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
                                                "Don't forget to hover around and play with the interactive graph!",
                                                html.Br(),
                                                "A"
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P([
                                                "Don't forget to hover around and play with the interactive graph!",
                                               html.Br(),
                                               "A"
                                               ]),
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

