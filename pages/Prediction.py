import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/Prediction')

month_list = [{'label': 'January', 'value': 'Jan'},
              {'label': 'February', 'value': 'Feb'},
              {'label': 'March', 'value': 'Mar'},
              {'label': 'April', 'value': 'Apr'},
              {'label': 'May', 'value': 'May'},
              {'label': 'June', 'value': 'Jun'},
              {'label': 'July', 'value': 'Jul'},
              {'label': 'August', 'value': 'Aug'},
              {'label': 'September', 'value': 'Sep'},
              {'label': 'October', 'value': 'Oct'},
              {'label': 'November', 'value': 'Nov'},
              {'label': 'December', 'value': 'Dec'}]

day_list = [
    {'label': str(day), 'value': day}
    for day in range(1, 32)
]

rain_dropdown = dcc.Dropdown(
    id='rain-dropdown',
    options=[],
    value=None,
    placeholder="Select the rain condition",
)

temp = dcc.Input(id='temp', type='number', min=-10, max=30, step=1, placeholder="temperature",)

winddirection_dropdown = dcc.Dropdown(
    id='winddirection_dropdown',
    options=[],
    value=None,
    placeholder="Select the wind direction",
)

location_dropdown = dcc.Dropdown(
    id='location_dropdown',
    options=[],
    value=None,
    placeholder="Select the location",
)

layout = html.Div([html.Div([
    html.Label('Select Month:'),
    dcc.Dropdown(
        id='month-dropdown',
        options=month_list,
        value=None,
        style={'width': '200px'},
        placeholder="Select a Month",
    )
], style={'margin-bottom': '10px'}),
    html.Div([
        html.Label('Select Day:'),
        dcc.Dropdown(
            id='day-dropdown',
            options=day_list,
            value=None,
            style={'width': '200px'},
            placeholder="Select a Day",
        )
    ]),
    html.Div(rain_dropdown),
    html.Div(temp),
    html.Div(winddirection_dropdown),
    html.Div(location_dropdown),
    html.Div(id='Prediction')
])


@callback(
    Output('Prediction', 'children'),
    Input('month-dropdown', 'value'),
    Input('day-dropdown', 'value')
)
def update_output(month, day):
    if month is not None and day is not None:
        return html.H3(f'Selected date: {month} {day}')
    else:
        return ''
