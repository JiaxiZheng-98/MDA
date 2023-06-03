import dash
from dash import html, dcc
from data import event_data
import plotly.express as px

dash.register_page(__name__, path='/Event_monthly')

event = event_data()
events_dist = event.groupby(['noise_event_laeq_primary_detected_class', 'month']).size().reset_index(name='count')
events_dist = events_dist.reset_index()

month_total = events_dist.groupby('month')['count'].transform('sum')
events_dist['percentage'] = (events_dist['count'] / month_total) * 100
events_dist = events_dist.sort_values('month')


fig = px.bar(events_dist, x="percentage", y="month", color="noise_event_laeq_primary_detected_class", orientation='h',
             hover_data=["noise_event_laeq_primary_detected_class", "count"],
             height=550, labels={"noise_event_laeq_primary_detected_class": "Event"},
             color_discrete_sequence=px.colors.qualitative.Antique,
             barmode='stack'
             )

fig.update_layout(
    yaxis=dict(
        tickmode='array',
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    )
)

layout = html.Div([
    dcc.Graph(
        figure=fig,
    )
])
