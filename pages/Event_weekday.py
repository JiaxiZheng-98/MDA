import dash
from dash import html, dcc
from data import event_data
import plotly.express as px

dash.register_page(__name__, path='/Event_weekday')

event = event_data()
events_dist = event.groupby(['noise_event_laeq_primary_detected_class', 'weekday']).size().reset_index(name='count')
events_dist = events_dist.reset_index()

fig = px.bar(events_dist, x="count", y="weekday", color="noise_event_laeq_primary_detected_class", orientation='h',
             hover_data=["noise_event_laeq_primary_detected_class", "count"],
             height=550, labels={"noise_event_laeq_primary_detected_class": "Event"},
             color_discrete_sequence=px.colors.qualitative.Antique
             )

fig.update_layout(
    yaxis=dict(
        tickmode='array',
        tickvals=[0, 1, 2, 3, 4, 5, 6],
        ticktext=['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    )
)

layout = html.Div([
    dcc.Graph(
        figure=fig,
    )
])
