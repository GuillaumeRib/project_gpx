####################################
# GET DATA
####################################
import gpxpy
import pandas as pd
test_path = 'project_gpx_viewer/data/Morvan_day2.gpx'
def get_gpx(gpx_path):
    '''
    Convert a gpx file as INPUT to a pd DataFrame as OUTPUT
    '''
    # Parse gpx file.
    with open(gpx_path) as f:
        gpx = gpxpy.parse(f)

    # Convert to a dataframe one point at a time.
    points = []
    for segment in gpx.tracks[0].segments:
        for p in segment.points:
            points.append({
                'time': p.time,
                'latitude': p.latitude,
                'longitude': p.longitude,
                'elevation': p.elevation,
            })
    df = pd.DataFrame.from_records(points)
    return df

def data_feat_eng(df):
    '''
    pd DataFrame from gpx file as INPUT.
    Create new features, enriching df
    OUTPUT pd DataFrame with added features
    '''

    # Duration
    df[['duration']] = df[['time']] - df[['time']].iloc[0]
    df['duration'] = df['duration'].apply(str)

    # D+
    df[['elev_diff']] = df[['elevation']].diff()
    df['d+'] = df[df['elev_diff']>0]['elev_diff'].cumsum().round(2)
    df = df.fillna(method='ffill')

    # Cumul Elevation
    df['elev_cum'] = df.elev_diff.cumsum().round(2)

    # Avg deniv for color
    n=90
    df['d_avg'] = df['elev_diff'].rolling(n).sum().round(2)
    return df
