import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import dash_leaflet.express as dlx
import json

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

map_naamsestraat = dl.Map(center=[50.876238831922526, 4.700073430112385], zoom=16, children=[
    dl.TileLayer(),
    dl.GeoJSON(id='map_naamsestraat',
               data=dlx.geojson_to_geobuf(json.loads(locations)),
               format='geobuf',
               )], style={'width': '100%', 'height': '70vh'})

app_description = dbc.Card(
    dbc.CardBody([dbc.Row(dcc.Markdown("APP Description", style={'fontSize': 30, 'textAlign': 'center'})),
                  dbc.Row(html.Div(
                      "The project involves a data analytics project related to the noise problem in the City of "
                      "Leuven, more in particular the neighborhood of the Naamse Straat1. The City of Leuven is "
                      "trying to strike the balance between a vibrant nightlife and people getting a good night’s "
                      "sleep. A trial project used sound monitors to map night-time noise levels, along with "
                      "behavioural ‘nudges’ to reduce noise."))]))

layout = dbc.Row(
    [
        dbc.Col(map_naamsestraat),
        dbc.Col([app_description]),
    ], style={"margin-left": "10px", "margin-right": "10px"}
)
