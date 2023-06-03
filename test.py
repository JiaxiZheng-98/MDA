import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import html, Dash
from dash_extensions.javascript import assign
import json

locations = '''{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Point",
        "coordinates": [
            4.700712432079855,        
            50.87648931687922
        ]
      }
    }
  ]
}'''

app = Dash()
app.layout = html.Div(children=[
    dl.Map(center=[50.87, 4.7], zoom=15, children=[
        dl.TileLayer(),
        dl.GeoJSON(data=dlx.geojson_to_geobuf(json.loads(locations)),
                   format='geobuf',)],
           style={'width': '50%', 'height': '100vh'})])

if __name__ == "__main__":
    app.run_server(debug=False)
