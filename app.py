####################################
# IMPORTS
####################################

import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

from gpx_viewer.interface import get_data
from gpx_viewer.interface import data_viz

###################################
# CONVERT GPX to Dataframe
####################################
test_path = 'gpx_viewer/data/Morvan_day1.gpx'
df = get_data.get_gpx(gpx_path=test_path)
df = get_data.data_feat_eng(df)

####################################
# INIT APP
####################################
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])

server=app.server

###################################
# SELECT TEMPLATE for the APP
####################################
# loads the template and sets it as the default
load_figure_template("darkly")


###################################
# IMPORT Charts
####################################
fig_1 = data_viz.map_2d(df)
fig_2 = data_viz.map_3d(df)
fig_3 = data_viz.elev_line(df)
fig_4 = data_viz.line_d_avg(df)
fig_5 = data_viz.histo_d_avg(df)
fig_6 = data_viz.line_d_plus(df)

####################################
# FILL Template layout
####################################

title = html.H1(children="GPS Data Visualization",
                className=('text-center mb-4'))

map_2d = dcc.Graph(figure=fig_1)
map_3d = dcc.Graph(figure=fig_2)
elev_line = dcc.Graph(figure=fig_3)
d_plus = dcc.Graph(figure=fig_6)
d_avg = dcc.Graph(figure=fig_4)
histo = dcc.Graph(figure=fig_5)


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(title,width=12,)
    ]),
    dbc.Row([
        dbc.Col(map_2d,width={'size':5,'offset':1}),
        dbc.Col(map_3d,width=5),
    ]),
    dbc.Row([
        dbc.Col(elev_line,width={'size':5,'offset':1}),
        dbc.Col(d_plus,width=5),
    ]),
    dbc.Row([
        dbc.Col(d_avg,width={'size':5,'offset':1}),
        dbc.Col(histo,width=5),
    ],justify=True),

],
                           fluid=True,
                           className="dbc")


####################################
# RUN the app
####################################
if __name__ == '__main__':
    server=app.server
    app.run_server(debug=True)
