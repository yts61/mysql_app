
# Dash packages
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from urllib.request import urlopen
import plotly.express as px
import json
import pandas as pd
from app import app

# A Choropleth Map is a map composed of colored polygons.

import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("assets/final_texas_cases.csv")
cities_for_map = pd.read_csv("assets/cities_for_geo_map.csv")

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig = px.choropleth(df, geojson=counties, locations='FIPS #',
                           hover_name = "County",
                           scope = "usa",
                           title = "Total Cases"
                          )

colors = ['#FFA07A','#CD5C5C','#B22222','#800000']
months = {5: 'May', 6:'June',7:'July',8:'Aug'}


#plot the bubble cases for each month and each county
for i in range(5,9)[::-1]: # Negative values to make a list in reverse order, in this case, it is from aug to may
    mask = df["month"] == i
    df_month = df[mask]
    #print(df_month)
    fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_month['X (Lat)'],
            lat = df_month['Y (Long)'],
            text = df_month[['County','Case Count']],
            name = months[i], # "i" only will only render the index, not the value.
            mode = 'markers',
            marker = dict(
                size = df_month['Case Count'],
                color = colors[i-5], # to make it within the colors list, in this case, it is 5-6=-1, rgb(239,243,255)
                line_width = 0,
                sizeref = 9,
                sizemode = "area",
                reversescale = True
            )))
# to show texas cities on map
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = cities_for_map['lng'],
    lat = cities_for_map['lat'],
    hoverinfo = 'text',
    text = cities_for_map['city'],
    name = "Major Cities",
    mode = 'markers',
    marker = dict(
        size = 4,
        color = 'rgb(102,102,102)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))
fig.update_geos(fitbounds="locations")
fig.update_layout(title_text='Total Cases per month for last 4 months', title_x=0.5)





###############################################################################
########### LANDING PAGE LAYOUT ###########
###############################################################################




layout = dbc.Container([
        html.Div([
            html.H2(["Wuhan Virus Cases During Summertime", html.Br(), "in Texas this Summer 2020"])
            ], style={'width':'100%','display':'flex','align-items':'center','justify-content':'center'}),
        
        
        dbc.Jumbotron([
            dbc.Row(
            [
                dbc.Col([
                    html.H4([], className="display-4"),
                    html.P(
                        "This page is showing a county-level geographic bubble map of COVID-19 cases in Texas using Python, Plotly, MySQL, PostgreSQL, cPanel.",
                        className="lead",
                    ),
                    html.Hr(className="my-2"),
                    html.P(
                        "With various merged data types e.g. CSV, XLSX, JSON, from multiple trustable sources such as US Census, US government, simplemaps.com, etc."
                    ),
                    html.P(dbc.Button("", color="primary"), className="lead"),
                ], width={"size": 5, "order": 2}, lg=5, md=5, xs=12),



                dbc.Col([
                    html.Div(
                        html.Img(src="/assets/virus.jpg",
                                style={'height': '',
                                        'width': '100%', }, id="the_id")),
                    dbc.Tooltip(
                                "The state is still clearing a backlog of coronavirus cases. DSHS added 550 backlogged cases to Wednesday's state total on August 19, 2020."
                                "",
                                target="the_id",
                ),
                ], width={"size": 7, "order": 1}, lg=7, md=7, xs=12,)

            ]
        )]
        ),
        
        
        html.Hr(),
        dbc.Row(
                [dbc.Col([
                    html.Div([
                        dcc.Graph(id='map',
                                  figure=fig
                                  ),
                        html.P([
                        "Click on the map and play around with the bubbles.",
                        html.Br(),
                        html.Br(),
                        "A tooltip will show up to tell you useful infomation like the name \
                        of the county and the confirmed cases when you hover over the bubble or localtion point. \
                        You can also enable or disable the month filter in the legend to see how the number of cases grew over the 4 months. ", 
                        html.Br(),
                        html.Br(),
                        "Try turning on only August and May, and you will find out how drastic an increase in confirmed cases is over the 4 months period. "]
                    ),
                        ]),
                 ], width={"size": 12, "order":1}, lg=12, md=12, xs=112)
        ], className="mt-4", style={"height": "100vh"})
        
        
])