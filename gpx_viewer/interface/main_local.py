####################################
# MAIN PAGE
####################################
import plotly.express as px
import gpxpy
import pandas as pd
import get_data
import data_viz

df = get_data.get_gpx()
df = get_data.data_feat_eng(df)

fig = data_viz.map_2d(df)
fig.show()

if __name__ == '__main__':
    print('main')
