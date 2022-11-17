####################################
# DATA VIZ - CREATE CHARTS
####################################
import plotly.express as px
import pandas as pd

color_cont = 'thermal'
col_seq = ['indianred']

def map_2d(df,color='d_avg'):
    '''
    Scatterplot GPS trace on 2D map.
    Custom feature as color
    '''
    fig = px.scatter_mapbox(df,
                            lat='latitude',
                            lon='longitude',
                            hover_name='d+',
                            mapbox_style="open-street-map",
                            zoom=11,
                            color=color,
                            color_continuous_scale=color_cont,
                            title='2D Map - Elevation Highlight',
                            #height=600
                            )
    fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'))
    fig.update_layout(margin=dict(l=20, r=20))
    return fig


def map_3d(df,color='d_avg'):
    '''
    3D scatterplot GPS trace.
    Custom feature as color
    '''
    fig = px.scatter_3d(df,
                        x='longitude',
                        y='latitude',
                        z='elevation',
                        color=color,
                        color_continuous_scale=color_cont,
                        hover_name='d+',
                        title='3D Profile - Elevation Highlight')

    fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
    fig.update_layout(scene = {"xaxis": {"nticks": 5},
                               "zaxis": {"nticks": 10},
                               "camera_eye": {"x": -0.5, "y": 0.5, "z": 0.5},
                               "aspectratio": {"x": 1, "y": 0.7, "z": 0.25}},
                      #height=600,
                      margin=dict(l=20, r=20),

                      )
    return fig


def elev_line(df,color='d_avg'):
    '''
    Line chart showing elevation profile
    Custom feature as color
    '''
    fig = px.scatter(df,
                     x='duration',
                     y='elev_cum',
                     color=color,
                     color_continuous_scale=color_cont,
                     hover_name='d+',
                     title='Elevation Profile in m'
                     )
    fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
    fig.update_layout(margin=dict(l=20, r=20))
    return fig

def line_d_avg(df):
    '''
    Plot the average deniv over 90sec
    '''
    fig = px.histogram(df,
                       x='duration',
                       y='d_avg',
                       hover_name='d+',
                       color_discrete_sequence=col_seq,
                       title='90sec Elevation gain/loss in m',
                       opacity=0.75
                       )
    fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
    fig.update_layout(margin=dict(l=20, r=20))
    return fig

def histo_d_avg(df):
    '''
    Plot the average deniv over 90sec
    '''
    fig = px.histogram(df,
                       x='d_avg',
                       hover_name='d+',
                       title='90sec Elevation Distribution',
                       nbins=50,
                       color_discrete_sequence=col_seq,
                       opacity=0.85
                       )
    fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
    fig.update_layout(margin=dict(l=20, r=20),
                      xaxis_title="90sec average elevation in m")
    return fig


def line_d_plus(df,color='d_avg'):
    '''
    Plot the cumul d+ profile
    '''
    fig = px.scatter(df,
                     x='duration',
                     y='d+',
                     color=color,
                     color_continuous_scale=color_cont,
                     hover_name='d+',
                     title='Cumul D+ m'
                     )
    fig.update_traces(marker=dict(size=3), selector=dict(mode='markers'))
    fig.update_layout(margin=dict(l=20, r=20))
    return fig
