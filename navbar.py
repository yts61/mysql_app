import os
import pathlib
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
# https://dash-bootstrap-components.opensource.faculty.ai/l/components

# Dash DAQ comprises a robust set of fancy controls
import dash_daq as daq

from app import app, server

LOGO = "https://elartedm.com/wp-content/uploads/2019/06/El-Arte-Logo-Light-m.png"


# dropdown Items
# make a reuseable navitem for the different examples for the dbc container below
nav_item = dbc.NavItem(dbc.NavLink("El Arte Design and Marketing Homepage", href="https://elartedm.com/"))




# make a reuseable dropdown for the different examples for the dbc container below
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Free Consultation", href='https://elartedm.com/free-startup-consultation/'),
        dbc.DropdownMenuItem("Marketing Blog", href='https://elartedm.com/marketing-blog/'),
        dbc.DropdownMenuItem("About Us", href='https://elartedm.com/about-us-1/'),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Privacy Policy", href='https://elartedm.com/privacy-policy/'),
        dbc.DropdownMenuItem("Contact Us", href='https://elartedm.com/contact-us/'),
    ],
    nav=True,
    in_navbar=True,
    label="Links",
    direction="",
    group=False,
)






"""------------------------------------  Header  ------------------------------------"""
elarte_navbar = html.Div([
    dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=LOGO, height="80px")),
                                    #dbc.Col(dbc.NavbarBrand("你的市場策劃數據分析公司", className="ml-0")),
                                ],
                                align="center",
                                no_gutters=True,
                            ),
                            href="https://elartedm.com",
                        ),

                        dbc.NavbarToggler(id="navbar-toggler"),
                        dbc.Collapse(
                            dbc.Nav(
                                [nav_item,
                                 dropdown,
                                 ], className="ml-auto", navbar=True
                            ),
                            id="navbar-collapse",
                            navbar=True,
                        )
                    ],
                ),
                color="#a6d9d2",
                dark="",
                className="mt-0 pt-5",
                light=True,
                sticky="top",
                style={"width": "100%"}
            ),
])


"""------------------------------------  Paste to the index.py  ------------------------------------"""

# add callback for toggling the collapse on small screens

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
