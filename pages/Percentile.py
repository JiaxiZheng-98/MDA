import dash
import pandas as pd
from dash import dcc, html, callback
from data import percentile_data
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

percentile = percentile_data()

dash.register_page(__name__, path='/Percentile')

all_variables = percentile.columns.tolist()
all_variables = all_variables[2:]
all_locations = [{'label': "Naamsestraat 35 Maxim", 'value': 255439},
                 {'label': "Naamsestraat 57 Xior", 'value': 255440},
                 {'label': "Naamsestraat 62 Taste", 'value': 255441},
                 {'label': "Calvariekapel KU Leuven", 'value': 255442},
                 {'label': "Parkstraat 2 La Filosovia", 'value': 255443},
                 {'label': "Naamsestraat 81", 'value': 255444},
                 {'label': "Kiosk Stadspark", 'value': 255445},
                 {'label': "Vrijthof", 'value': 280324},
                 {'label': "His-Hairs", 'value': 303910}]

month_slider = dbc.Card(
    dbc.CardBody([
        html.P(
            id="slider-text",
            children="Drag the slider to change the month:",
        ),
        dcc.Slider(
            id="months-slider",
            min=1,
            max=12,
            value=3,
            step=1,
            marks={i: str(i) for i in range(1, 13)},
        )
    ])
)

day_slider = dbc.Card(
    dbc.CardBody([
        html.P(
            id="slider-text",
            children="Drag the slider to change the time period:",
        ),
        dcc.RangeSlider(
            id="days-slider",
            min=1,
            max=31,
            value=[5, 15],
            step=1,
            marks=None,
            allowCross=False,
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ])
)

var_dropdown = dbc.Card(
    dbc.CardBody([
        html.P(
            id="dropdown-text",
            children="Select Variables: ",
        ),
        dcc.Dropdown(
            id='variables-dropdown',
            options=[{'label': k, 'value': k} for k in all_variables],
            value=all_variables[10:],
            multi=True,
            searchable=False,
        )
    ])
)

loc_dropdown = dbc.Card(
    dbc.CardBody([
        html.P(
            id="dropdown-text",
            children="Select Location: ",
        ),
        dcc.Dropdown(
            id='locations-dropdown',
            options=all_locations,
            value=255439,
            multi=False,
            searchable=False
        )
    ])
)

layout = dbc.Row([
    dbc.Col([
        month_slider,
        html.Br(),
        day_slider,
        html.Br(),
        var_dropdown,
        html.Br(),
        loc_dropdown,
    ], width=3, align="center"),
    dbc.Col(dbc.Card(
        dbc.CardBody(dcc.Graph(id='monthPlot'))
    ))]
    , style={"margin-left": "10px", "margin-right": "10px"})


@callback(
    Output("monthPlot", "figure"),
    [Input("months-slider", "value"),
     Input("days-slider", "value"),
     Input("variables-dropdown", "value"),
     Input("locations-dropdown", "value")]
)
def MonthPlot(month, day, var, loc):
    filtered_percentile = percentile.loc[
        (percentile['result_timestamp'].dt.month == month) &
        (percentile['result_timestamp'].dt.day.between(day[0], day[1]))
        ]
    filtered_percentile = filtered_percentile[filtered_percentile['#object_id'] == loc]
    fig = px.line(filtered_percentile, x='result_timestamp', y=var,
                  labels={
                      "result_timestamp": "Date",
                      "y": "Noise (dbs)"
                  })
    fig.update_layout(yaxis_title='Noise in db(a)', xaxis_title='Time')
    return fig
