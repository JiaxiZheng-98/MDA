import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


# create the dashboard
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# create the navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink("Percentile Data", href="/Percentile")
        ),
        dbc.NavItem(dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("General", href="/Event_general"),
                dbc.DropdownMenuItem("Monthly", href="/Event_monthly"),
                dbc.DropdownMenuItem("Weekday", href="/Event_weekday"),
            ],
            nav=True,
            in_navbar=True,
            label="Event Data",
        )),
        dbc.NavItem(dbc.NavLink("Level", href="/Level")),
        dbc.NavItem(dbc.NavLink("Prediction", href="/Prediction")),
    ],
    brand="Home",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True,
    links_left=True,
    sticky='Top'
)

# dashboard layout
app.layout = html.Div(
    [
        html.Div("Noise in Leuven", style={'fontSize': 50, 'textAlign': 'center'}),
        navbar,
        html.Hr(),
        # content of each page
        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run_server()