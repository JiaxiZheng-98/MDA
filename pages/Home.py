import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
import json

# Nine locations of Naamsestraat
locations = '''{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {"tooltip": "Naamsestraat 35 Maxim"},
      "geometry": {
        "coordinates": [
          4.70072379357917,
          50.87714100050355
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Naamsestraat 57 Xior"},
      "geometry": {
        "coordinates": [
          4.70071477856722,
          50.876488580852254
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Naamsestraat 62 Taste"},
      "geometry": {
        "coordinates": [
          4.7002025710271775,
          50.87584242792479
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Calvariekapel KU Leuven"},
      "geometry": {
        "coordinates": [
          4.699912605199012,
          50.87450555964785
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Parkstraat 2 La Filosovia"},
      "geometry": {
        "coordinates": [
          4.700037432979235,
          50.87409594784916
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Naamsestraat 81"},
      "geometry": {
        "coordinates": [
          4.700120481982684,
          50.87381992056434
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Kiosk Stadspark"},
      "geometry": {
        "coordinates": [
          4.701509483236361,
          50.87527504898961
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "Vrijthof"},
      "geometry": {
        "coordinates": [
          4.701188515337842,
          50.878905306069015
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {"tooltip": "His-Hairs"},
      "geometry": {
        "coordinates": [
          4.700112614916,
          50.87525705896549
        ],
        "type": "Point"
      }
    }
  ]
}
'''

dash.register_page(__name__, external_stylesheets=[dbc.themes.FLATLY], path='/')

# add locations to the map
map_naamsestraat = dl.Map(center=[50.876238831922526, 4.700073430112385], zoom=16, children=[
    dl.TileLayer(),
    dl.GeoJSON(id='map_naamsestraat',
               data=dlx.geojson_to_geobuf(json.loads(locations)),
               format='geobuf',
               )], style={'width': '100%', 'height': '70vh'})

# add app description
app_description = dbc.Card([
    dbc.CardBody([dbc.Row(dcc.Markdown("APP Description",
                                       style={'fontSize': 30, 'textAlign': 'center', "font-weight": "bold"})),
                  dbc.Row(html.Div(
                      "This application provides the data visualization based on the information and the data from "
                      "the datasets: Export 40, Export 41, Export 42, Meteo and Traffic. The information contained is "
                      "mainly about noise, weather and traffic, the three core elements of our research question: How "
                      "do the weather and traffic affect noise in the center of Leuven? The aim of this application "
                      "is to provide a clear picture of how the data change over time in order to make the prediction "
                      "in the future.")),
                  html.Br(),
                  dbc.Row(html.Div(
                      "In the application, we provide three types of data visualization. Firstly, in the Percentile "
                      "Data tab, one can find information about the level of noise during a year. One can make a "
                      "choice using the variables to select the:")),
                  dbc.Row(html.Div(" • month")),
                  dbc.Row(html.Div(" • time period")),
                  dbc.Row(html.Div(" • location of the noise detector")),
                  dbc.Row(html.Div(" • total amount of measurement time that the noise level lasted")),
                  html.Br(),
                  dbc.Row(html.Div("Secondly, we have the Event Data tab. There one can find  the visualization of "
                                   "the distribution of each type of Noise Event. This tab provides the overview for "
                                   "three time periods: a General one (annual), a Monthly and a Weekday one. Through "
                                   "the visualization (Monthly and Weekday), users can also select certain noise "
                                   "types by clicking on the list on the right in order to check the distribution of "
                                   "different noise events during the desirable time period. ")),
                  html.Br(),
                  dbc.Row(html.Div("Thirdly, in a similar way like the Percentile tab, in the Level tab we can find "
                                   "information when choosing the:")),
                  dbc.Row(html.Div(" • month")),
                  dbc.Row(html.Div(" • time period")),
                  dbc.Row(html.Div(" • location of the noise detector")),
                  dbc.Row(html.Div(" • the four terms for sound level: ")),
                  dbc.Row(html.Div(" • ICpeak: Instantaneous C-Weighted Peak Sound Pressure Level")),
                  dbc.Row(html.Div(" • Lamax: Maximum A-weighted sound pressure level ")),
                  dbc.Row(html.Div(" • LAeq : A-weighted, equivalent continuous sound level")),
                  dbc.Row(html.Div(" • LCeq : C-weighted, equivalent continuous sound level")),
                  html.Br(),
                  dbc.Row(html.Div("Finally, the fourth tab is for the prediction. By selecting month, day, "
                                   "temperature, rain condition, wind direction and exact location, one can see the "
                                   "percentages of predictions of the six different noise type classifications.")),
                  ]),
])

# group member
group = dbc.Card(
    dbc.CardBody([html.Div("Group Ecuador:", style={'text-align': 'right', "font-weight": "bold"}),
                  html.Div("Georgia Soni", style={'text-align': 'right'}),
                  html.Div("Lotte Wouters", style={'text-align': 'right'}),
                  html.Div("Jiaxi Zheng", style={'text-align': 'right'}),
                  html.Div("Yu-Ting Ma", style={'text-align': 'right'}),
                  ])
)

# layout
layout = dbc.Row(
    [
        dbc.Col(map_naamsestraat),
        dbc.Col([app_description,
                 html.Br(),
                 group]),
    ], style={"margin-left": "10px", "margin-right": "10px"}
)
