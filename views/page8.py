
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


# Create a DataFrame from  "flights" data
df1 = pd.read_csv('assets/flights.csv')

# Define a data variable
data1 = [go.Heatmap(
    x=df1['year'],
    y=df1['month'],
    z=df1['passengers']
)]

# Define the layout
layout1 = go.Layout(
    title='Flights'
)
# Create a fig from data and layout, and plot the fig
fig1 = go.Figure(data=data1, layout=layout1)

#######
# Excellent! This shows two distinct trends - an increase in
# passengers flying over the years, and a greater number of
# passengers flying in the summer months.
######




###############################################################################
########### GRAPH 2 ###########
###############################################################################

#######
# Side-by-side heatmaps for Sitka, Alaska,
# Santa Barbara, California and Yuma, Arizona
# using a shared temperature scale.
######
from plotly import subplots


dfa = pd.read_csv('assets/2010SitkaAK.csv')
dfb = pd.read_csv('assets/2010SantaBarbaraCA.csv')
dfc = pd.read_csv('assets/2010YumaAZ.csv')

trace1 = go.Heatmap(
    x=dfa['DAY'],
    y=dfa['LST_TIME'],
    z=dfa['T_HR_AVG'],
    colorscale='Jet',
    zmin = 5, zmax = 40 # add max/min color values to make each plot consistent
)
trace2 = go.Heatmap(
    x=dfb['DAY'],
    y=dfb['LST_TIME'],
    z=dfb['T_HR_AVG'],
    colorscale='Jet',
    zmin = 5, zmax = 40
)
trace3 = go.Heatmap(
    x=dfc['DAY'],
    y=dfc['LST_TIME'],
    z=dfc['T_HR_AVG'],
    colorscale='Jet',
    zmin = 5, zmax = 40
)

fig2 = subplots.make_subplots(rows=1, cols=3,
    subplot_titles=('Sitka, AK','Santa Barbara, CA', 'Yuma, AZ'),
    shared_yaxes = True,  # this makes the hours appear only on the left
)
fig2.append_trace(trace1, 1, 1)
fig2.append_trace(trace2, 1, 2)
fig2.append_trace(trace3, 1, 3)

fig2['layout'].update(      # access the layout directly!
    title='Hourly Temperatures, June 1-7, 2010'
)




###############################################################################
########### PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

                dbc.Jumbotron([
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Heat Map 1"], className="display-5"),
                                        html.P([
                                                "A heatmap shows the correlations of each input clearly with colors.",
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("This map shows two distinct trends - an increase in passengers flying over the years, \
                                                and a greater number of passengers flying in the summer months."),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='heat 1',
                                                        figure=fig1
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mt-4"),
                        
                        dbc.Row([
                                dbc.Col([
                                        html.H4(["Heat Map 2"], className="display-5"),
                                        html.P([
                                                "This is a side-by-side heatmaps for Sitka, Alaska, Santa Barbara, California and Yuma, Arizona, using a shared temperature scale."
                                                ],
                                                className="lead",
                                        ),
                                        html.Hr(className="my-2"),
                                        html.P("Don't forget to hover around and play with the interactive graph!"),
                                        html.P(dbc.Button("", color="primary"), className="lead"),
                                        ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                                dbc.Col([
                                        html.Div([
                                                dcc.Graph(id='heat 2',
                                                        figure=fig2
                                                        ),
                                                html.P([]),
                                                ]),
                                        ], width={"size": 7, "order":1}, lg=7, md=7, xs=112)
                                
                                
                                ], className="mb-4"),

                        ])
                ])

