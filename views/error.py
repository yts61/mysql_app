
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from app import app

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='err404', refresh=True),
        dbc.Container(
            html.Img(
                src='/assets/datascience.jpg',
                className='center',
                style={'height': '',
                        'width': '50%', },
            ),
        ),
        dbc.Container([

            html.H5(id='outputState', children='Error 404 - Page not found'),
            html.A("Go back to the front page.", href="/"),

        ], className='form-group'),
    ], className='jumbotron')
])
