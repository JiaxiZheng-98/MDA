import dash
from dash import html, dcc
from data import event_data
import plotly.express as px

dash.register_page(__name__, path='/Event_general')

# group the  event data in order to plot
event = event_data()
events_dist = event.groupby(['noise_event_laeq_primary_detected_class', 'time_of_day']).size().reset_index(name='count')
events_dist = events_dist.reset_index()

# add the sunburst plot
fig = px.sunburst(events_dist,
                  path=["noise_event_laeq_primary_detected_class", "time_of_day"],
                  values='count',
                  title="Noise Event Count Distribution",
                  color_discrete_sequence=px.colors.sequential.Aggrnyl,
                  )
fig.update_traces(texttemplate="%{label}<br>%{percentParent} of this event <br>%{percentRoot} of all noise event<br>%{"
                               "value}")
fig.update_layout(margin=dict(t=45, l=25, r=25, b=25), title_x=0.5)

layout = html.Div([
    dcc.Graph(
        figure=fig,
        style={
            'height': "100%",
            'width': "100%",
            "display": "block",
            "margin-left": "auto",
            "margin-right": "auto", }
    )
]
)
