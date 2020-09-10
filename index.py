# index page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app, server
from flask_login import logout_user, current_user
from views import login, error, page1, page2, page3, page4, page5, page6, page7, page8, profile, user_admin
from navbar import *

navBar = dbc.Navbar(id='navBar',
    children=[],
    color='#a6d9d2',
    style={'width':'100%','display':'flex','align-items':'center','justify-content':'center'}
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        elarte_navbar,
        navBar,
        html.Div(id='pageContent')
    ])
], id='table-wrapper')


################################################################################
# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
################################################################################
@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/':
        if current_user.is_authenticated:
            return page1.layout
        else:
            return login.layout

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return login.layout
        else:
            return login.layout

    if pathname == '/page1':
        if current_user.is_authenticated:
            return page1.layout
        else:
            return login.layout

    if pathname == '/page2':
        if current_user.is_authenticated:
            return page2.layout
        else:
            return login.layout
        
    if pathname == '/page3':
        if current_user.is_authenticated:
            return page3.layout
        else:
            return login.layout

    if pathname == '/page4':
        if current_user.is_authenticated:
            return page4.layout
        else:
            return login.layout

    if pathname == '/page5':
        if current_user.is_authenticated:
            return page5.layout
        else:
            return login.layout

    if pathname == '/page6':
        if current_user.is_authenticated:
            return page6.layout
        else:
            return login.layout

    if pathname == '/page7':
        if current_user.is_authenticated:
            return page7.layout
        else:
            return login.layout

    if pathname == '/page8':
        if current_user.is_authenticated:
            return page8.layout
        else:
            return login.layout

    if pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout

    if pathname == '/admin':
        if current_user.is_authenticated:
            if current_user.admin == 1:
                return user_admin.layout
            else:
                return error.layout
        else:
            return login.layout


    else:
        return error.layout


################################################################################
# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
################################################################################
@app.callback(
    Output('navBar', 'children'),
    [Input('pageContent', 'children')])
def navBar(input1):
    if current_user.is_authenticated:
        if current_user.admin == 1:
            navBarContents = html.Div([
                dbc.NavItem(dbc.NavLink('Page 1', href='/page1')),
                dbc.NavItem(dbc.NavLink('Page 2', href='/page2')),
                dbc.NavItem(dbc.NavLink('Page 3', href='/page3')),
                dbc.NavItem(dbc.NavLink('Page 4', href='/page4')),
                dbc.NavItem(dbc.NavLink('Page 5', href='/page5')),
                dbc.NavItem(dbc.NavLink('Page 6', href='/page6')),
                dbc.NavItem(dbc.NavLink('Page 7', href='/page7')),
                dbc.NavItem(dbc.NavLink('Page 8', href='/page8')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem('Admin', href='/admin'),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem('Logout', href='/logout'),
                    ],
                ),
            ], horizontal="center", pills=True
)
            return navBarContents

        else:
            navBarContents = [
                dbc.NavItem(dbc.NavLink('Page 1', href='/page1')),
                dbc.NavItem(dbc.NavLink('Page 2', href='/page2')),
                dbc.NavItem(dbc.NavLink('Page 3', href='/page3')),
                dbc.NavItem(dbc.NavLink('Page 4', href='/page4')),
                dbc.NavItem(dbc.NavLink('Page 5', href='/page5')),
                dbc.NavItem(dbc.NavLink('Page 6', href='/page6')),
                dbc.NavItem(dbc.NavLink('Page 7', href='/page7')),
                dbc.NavItem(dbc.NavLink('Page 8', href='/page8')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem('Logout', href='/logout'),
                    ],
                ),
            ]
            return navBarContents

    else:
        return ''



if __name__ == '__main__':
    app.run_server(debug=True, port=8072)
