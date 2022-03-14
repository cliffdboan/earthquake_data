import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the data structure
filename = 'data/eq_data_30_day_m2.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
meta = all_eq_data['metadata']

# Generate a title for the graph from the metadata dictionary.
my_title = meta['title']

# Generate lists of earthquake properties to populate the map.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons, 
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Delta',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]
my_layout = Layout(title= my_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')