####################################
# IMPORTS
####################################

import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc

from gpx_viewer.interface import get_data
from gpx_viewer.interface import data_viz


###################################
# CONVERT GPX to Dataframe
####################################
test_path = 'gpx_viewer/data/Morvan_day1.gpx'
df = get_data.get_gpx(gpx_path=test_path)
df = get_data.data_feat_eng(df)

###################################
# IMPORT Charts
####################################
fig_1 = data_viz.map_2d(df)
fig_2 = data_viz.map_3d(df)
fig_3 = data_viz.elev_line(df)
fig_4 = data_viz.line_d_avg(df)
fig_5 = data_viz.histo_d_avg(df)

####################################
# DASH Template + Design
####################################
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
title = html.H1(children="Clem's Suffer Fest")

map_2d = dcc.Graph(figure=fig_1)
map_3d = dcc.Graph(figure=fig_2)
elev_line = dcc.Graph(figure=fig_3)
d_avg = dcc.Graph(figure=fig_4)
histo = dcc.Graph(figure=fig_5)

row_1 = map_2d
row_2 = map_3d
row_3 = elev_line
row_4 = d_avg
row_5 = histo

app.layout = html.Div(children=[
    title,
    row_1,
    row_2,
    row_3,
    row_4,
    row_5
])

####################################
# RUN the app
####################################
if __name__ == '__main__':
    server=app.server
    app.run_server(debug=True)
