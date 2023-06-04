import dash
import pandas as pd
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import joblib

dash.register_page(__name__, path='/Prediction')

# import the dataset for model
meteo_export41 = pd.read_csv('meteo_export41.csv', sep=',')
forest_cyclic = joblib.load("random_forest_model.pkl")
acyclic_time = ["hour", "dayOfWeek", "month"]
meteo_export41 = meteo_export41.drop(acyclic_time, axis=1).drop('noise_event', axis=1)
feature_names = meteo_export41.columns.tolist()
x_new = meteo_export41.iloc[3].values.reshape(1, -1)
x_new = pd.DataFrame(x_new, columns=feature_names)
class_labels_forest = forest_cyclic.classes_

# labels for dropdown box
month_list = [{'label': 'January', 'value': 1},
              {'label': 'February', 'value': 2},
              {'label': 'March', 'value': 3},
              {'label': 'April', 'value': 4},
              {'label': 'May', 'value': 5},
              {'label': 'June', 'value': 6},
              {'label': 'July', 'value': 7},
              {'label': 'August', 'value': 8},
              {'label': 'September', 'value': 9},
              {'label': 'October', 'value': 10},
              {'label': 'November', 'value': 11},
              {'label': 'December', 'value': 12}]

day_list = [
    {'label': str(day), 'value': day}
    for day in range(1, 32)
]

hour_list = [
    {'label': str(hour), 'value': hour}
    for hour in range(1, 24)
]

# month dropdown
month_dropdown = dcc.Dropdown(
    id='month-dropdown',
    options=month_list,
    value=None,
    style={'width': '250px'},
    placeholder="Select a Month"
)

# day dropdown
day_dropdown = dcc.Dropdown(
    id='day-dropdown',
    options=day_list,
    value=None,
    style={'width': '250px'},
    placeholder="Select a Day",
)

# hour dropdown
hour_dropdown = dcc.Dropdown(
    id='hour-dropdown',
    options=hour_list,
    value=None,
    style={'width': '250px'},
    placeholder="Select a Hour",
)

# decoder for the rain condition
intensities = [0.0, 0.1, 0.2, 0.5, 4, 9]
labels = ["No rain (0mm/hour)", "Very slight rain ( < 0.2mm/hour)", "Slight rain (0.2 - 0.5mm/hour)",
          "Moderate rain (0.5 - 4mm/hour)", "Heavy rain (4 - 8mm/hour)", "Very heavy rain ( > 8mm/hour)"]


def decode_RAININ(label):
    intensity = intensities[labels.index(label)]
    return intensity


# rain condition dropdown
rain_dropdown = dcc.Dropdown(
    id='rain-dropdown',
    options=labels,
    value=None,
    style={'width': '250px'},
    placeholder="Select the rain condition",
)

# Temperature, humidity, wind speed inputs
temp = dcc.Input(id='temp', type='number', min=-10, max=30, step=1, placeholder="temperature (℃)",
                 style={'width': '250px'}, )
humidity = dcc.Input(id='humidity', type='number', min=0, max=100, step=1, placeholder="humidity",
                     style={'width': '250px'}, )
wind_speed = dcc.Input(id='ws', type='number', min=0, max=10, step=1, placeholder="wind_speed (m/s)",
                       style={'width': '250px'}, )

# decoder for wind direction
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
to_degrees = [0, 45, 90, 135, 180, 225, 270, 315, 0]


# Decoder for WINDDIR:
def decode_WINDDIR(direction):
    decoded_degree = to_degrees[directions.index(direction)]
    return decoded_degree


# wind direction dropdown
winddirection_dropdown = dcc.Dropdown(
    id='winddirection_dropdown',
    options=directions,
    value=None,
    placeholder="Select the wind direction",
    style={'width': '250px'},
)

# Number of Heavy Vehicles, car, bike, pedestrian inputs
heavy = dcc.Input(id='heavy', type='number', min=-0, max=1000, step=1, placeholder="Number of Heavy Vehicles",
                  style={'width': '250px'}, )
car = dcc.Input(id='car', type='number', min=0, max=1000, step=1, placeholder="Number of Cars",
                style={'width': '250px'}, )
bike = dcc.Input(id='bike', type='number', min=0, max=1000, step=1, placeholder="Number of Bikes",
                 style={'width': '250px'}, )
pedestrian = dcc.Input(id='pedestrian', type='number', min=0, max=1000, step=1, placeholder="Number of Pedestrians",
                       style={'width': '250px'}, )

# label for location dropdown
all_locations = [{'label': "Naamsestraat 35 Maxim", 'value': 255439},
                 {'label': "Naamsestraat 57 Xior", 'value': 255440},
                 {'label': "Naamsestraat 62 Taste", 'value': 255441},
                 {'label': "Calvariekapel KU Leuven", 'value': 255442},
                 {'label': "Parkstraat 2 La Filosovia", 'value': 255443},
                 {'label': "Naamsestraat 81", 'value': 255444},
                 {'label': "Kiosk Stadspark", 'value': 255445},
                 {'label': "Vrijthof", 'value': 280324},
                 {'label': "His-Hairs", 'value': 303910}]

# location dropdown
location_dropdown = dcc.Dropdown(
    id='location_dropdown',
    options=all_locations,
    value=None,
    placeholder="Select the location",
    style={'width': '250px'},
)

# combine all the inputs
inputs = dbc.Card(
    dbc.CardBody([
        html.Div("To predict the noise event of 2023, please give the necessary inputs.",
                 style={"text-align": "center", 'font-size': "40px", 'color': 'rgb(0,51,112)'}),
        html.Br(),
        dbc.Row([
            dbc.Col(month_dropdown, width="auto"),
            dbc.Col(day_dropdown, width="auto"),
            dbc.Col(hour_dropdown, width="auto")
        ], justify="center"),
        html.Br(),
        dbc.Row([
            dbc.Col(rain_dropdown, width="auto"),
            dbc.Col(temp, width="auto"),
            dbc.Col(humidity, width="auto"),
        ], justify="center"),
        html.Br(),
        dbc.Row([
            dbc.Col(wind_speed, width="auto"),
            dbc.Col(winddirection_dropdown, width="auto"),
            dbc.Col(location_dropdown, width="auto"),
        ], justify="center"),
        html.Br(),
        dbc.Row([
            dbc.Col(heavy, width="auto"),
            dbc.Col(car, width="auto"),
            dbc.Col(bike, width="auto"),
            dbc.Col(pedestrian, width="auto"),
        ], justify="center")
    ])
)

# combine all the predictions
pred = dbc.Row([
    dbc.Col([html.Img(src=r'assets/icons8-shouting-48.png', alt='image',
                      style={'height': 100, 'width': 100, 'display': 'block', 'margin-left': "auto",
                             'margin-right': "auto"}),
             html.Div("Human voice - Shouting",
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'}),
             html.Div(id='prediction1',
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'})
             ]),
    dbc.Col([html.Img(src=r'assets/icons8-laid-back-64.png', alt='image',
                      style={'height': 100, 'width': 100, 'display': 'block', 'margin-left': "auto",
                             'margin-right': "auto"}),
             html.Div("Human voice - Singing",
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'}),
             html.Div(id='prediction2',
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'})
             ]),
    dbc.Col([html.Img(src=r'assets/icons8-musical-notes-100.png', alt='image',
                      style={'height': 100, 'width': 100, 'display': 'block', 'margin-left': "auto",
                             'margin-right': "auto"}),
             html.Div("Music non-amplified",
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'}),
             html.Div(id='prediction3',
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'})
             ]),
    dbc.Col([html.Img(src=r'assets/icons8-wind-100.png', alt='image',
                      style={'height': 100, 'width': 100, 'display': 'block', 'margin-left': "auto",
                             'margin-right': "auto"}),
             html.Div("Nature elements - Wind",
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'}),
             html.Div(id='prediction4',
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'})
             ]),
    dbc.Col([html.Img(src=r'assets/icons8-car-64.png', alt='image',
                      style={'height': 100, 'width': 100, 'display': 'block', 'margin-left': "auto",
                             'margin-right': "auto"}),
             html.Div("Transport road - Passenger car",
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'}),
             html.Div(id='prediction5',
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'})
             ]),
    dbc.Col([html.Img(src=r'assets/icons8-siren-64.png', alt='image',
                      style={'height': 100, 'width': 100, 'display': 'block', 'margin-left': "auto",
                             'margin-right': "auto"}),
             html.Div("Transport road - Siren",
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'}),
             html.Div(id='prediction6',
                      style={"text-align": "center", 'font-size': "30px", 'color': 'rgb(0,51,112)',
                             'font-family': 'Comic Sans MS'})
             ]),
], justify="end")

# layout
layout = html.Div([
    inputs,
    html.Br(),
    dbc.Card(
        dbc.CardBody(pred)
    )
])


# callback to update the prediction
@callback(
    [Output('prediction1', 'children'),
     Output('prediction2', 'children'),
     Output('prediction3', 'children'),
     Output('prediction4', 'children'),
     Output('prediction5', 'children'),
     Output('prediction6', 'children')],
    [Input('month-dropdown', 'value'),
     Input('day-dropdown', 'value'),
     Input('hour-dropdown', 'value'),
     Input('rain-dropdown', 'value'),
     Input('temp', 'value'),
     Input('humidity', 'value'),
     Input('ws', 'value'),
     Input("winddirection_dropdown", "value"),
     Input('location_dropdown', 'value'),
     Input('heavy', 'value'),
     Input('car', 'value'),
     Input('bike', 'value'),
     Input('pedestrian', 'value'),
     ]
)
def update_output(month, day, hour, rain, temperature, h, ws, wd, loc, num_heavy, num_car, num_bike, num_pedestrian):
    if month is not None and day is not None and rain is not None and temperature is not None and h is not None and \
            ws is not None and wd is not None and loc is not None and num_heavy is not None and num_car is not None and \
            num_bike is not None and num_pedestrian is not None:
        date = datetime(2023, month, day)
        academic = 0
        if month in [1, 6, 7, 8, 9]:
            academic = 1

        if month == 9 and day in range(24, 31):
            academic = 0

        if month == 12 and day in range(25, 32):
            academic = 1

        if month == 2 and day in range(1, 14):
            academic = 1

        if month == 4 and day in range(1, 17):
            academic = 1

        scaler = MinMaxScaler(feature_range=(0, 2 * np.pi))
        hour_array = np.array([hour])
        scaled_hour = scaler.fit_transform(hour_array.reshape(-1, 1))
        weekday_array = np.array([date.weekday()])
        scaled_weekday = scaler.fit_transform(weekday_array.reshape(-1, 1))
        month_array = np.array([month])
        scaled_month = scaler.fit_transform(month_array.reshape(-1, 1))

        x_new['LC_HUMIDITY'] = h
        x_new['LC_DWPTEMP'] = 260.2809 - 0.4438 * month - 3.0222 * h + 3.4770 * temperature - 19.5174 * np.sin(
            2 * np.pi * hour / 24) - 69.9803 * np.cos(2 * np.pi * hour / 24)
        x_new['LC_RAININ'] = decode_RAININ(rain)
        x_new['LC_RAD60'] = 0.4 + 0.5888 * temperature
        x_new['AV_TEMP'] = temperature
        x_new['LC_WINDDIR'] = decode_WINDDIR(wd)
        x_new['heavy'] = num_heavy
        x_new['car'] = num_car
        x_new['bike'] = num_bike
        x_new['pedestrian'] = num_pedestrian
        x_new['weekend'] = int(date.weekday() >= 5)
        x_new['academic_calender'] = academic
        x_new['cos_hour'] = np.cos(scaled_hour)
        x_new['sin_hour'] = np.sin(scaled_hour)
        x_new['cos_dayOfWeek'] = np.cos(scaled_weekday)
        x_new['sin_dayOfWeek'] = np.sin(scaled_weekday)
        x_new['cos_month'] = np.cos(scaled_month)
        x_new['sin_month'] = np.sin(scaled_month)

        x_new['location_MP 01: Naamsestraat 35  Maxim'] = int(loc == 255439)
        x_new['location_MP 01: Naamsestraat 35  Maxim.1'] = int(loc == 255439)
        x_new['location_MP 02: Naamsestraat 57 Xior'] = int(loc == 255440)
        x_new['location_MP 02: Naamsestraat 57 Xior.1'] = int(loc == 255440)
        x_new['location_MP 03: Naamsestraat 62 Taste'] = int(loc == 255441)
        x_new['location_MP 03: Naamsestraat 62 Taste.1'] = int(loc == 255441)
        x_new['location_MP 05: Calvariekapel KU Leuven'] = int(loc == 255442)
        x_new['location_MP 05: Calvariekapel KU Leuven.1'] = int(loc == 255442)
        x_new['location_MP 06: Parkstraat 2 La Filosovia'] = int(loc == 255443)
        x_new['location_MP 06: Parkstraat 2 La Filosovia.1'] = int(loc == 255443)
        x_new['location_MP 07: Naamsestraat 81'] = int(loc == 255444)
        x_new['location_MP 07: Naamsestraat 81.1'] = int(loc == 255444)
        x_new['location_MP08bis - Vrijthof'] = int(loc == 280324)
        x_new['location_MP08bis - Vrijthof.1'] = int(loc == 280324)

        dropvar = ["location_MP 01: Naamsestraat 35  Maxim.1", "location_MP 02: Naamsestraat 57 Xior.1",
                   "location_MP 03: Naamsestraat 62 Taste.1", "location_MP 05: Calvariekapel KU Leuven.1",
                   "location_MP 06: Parkstraat 2 La Filosovia.1", "location_MP 07: Naamsestraat 81.1",
                   "location_MP08bis - Vrijthof.1"]

        pre = x_new.drop(dropvar, axis=1)
        probas = forest_cyclic.predict_proba(pre)

        return (
            f"{round(probas[0][0] * 100, 1)}%",
            f"{round(probas[0][1] * 100, 1)}%",
            f"{round(probas[0][2] * 100, 1)}%",
            f"{round(probas[0][3] * 100, 1)}%",
            f"{round(probas[0][4] * 100, 1)}%",
            f"{round(probas[0][5] * 100, 1)}%"
        )
    else:
        return ''
