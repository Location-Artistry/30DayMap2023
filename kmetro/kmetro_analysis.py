import geopandas as gpd
import matplotlib.colors as colors
import webbrowser
# import folium
# import matplotlib as plt

# read in routes, stops and service area
routes = gpd.read_file('kmetro_routes.geojson')
stops = gpd.read_file('kmetro-stops.geojson')
service_area = gpd.read_file('kmetro_area.geojson')
# convert routes and stops to Albers Equal Area for spatial join
routes.to_crs(5070, inplace=True)
stops.to_crs(5070, inplace=True)

# Create unique colors for each route and route_color dict to specify color
color_dict = ['lightcoral', 'orangered', 'chocolate', 'orange', 'gold',
              'chartreuse', 'forestgreen', 'aquamarine', 'teal', 'deepskyblue',
              'cornflowerblue', 'navy', 'mediumslateblue', 'blueviolet', 'plum',
              'violet', 'magenta', 'deeppink', 'crimson', 'firebrick', 'sienna',
              'khaki', 'greenyellow', 'indigo']
route_dict = ['East Romence', 'West Center', 'Lovell', 'Paterson', 'West Main',
              'South Burdick', 'Duke', 'Stadium/Kvcc', 'Comstock', 'Gull Road',
              'Egleston', 'Alamo', 'Parchment', 'East Main', 'Oakland',
              'West Michigan', 'Portage', 'Westnedge', 'Solon/Kendall',
              'Ring Road', 'Parkview Campus']
route_color = {}
for i, route in enumerate(route_dict):
    route_color[route] = color_dict[i]

# add the color column from route_color
routes['color_line'] = routes.apply(lambda row: route_color[row.route_long_name], axis=1)
# view the dataframe in a web browser
# routes_no_geo = routes.drop('geometry', axis=1)
# with open('data.html', "w") as f: f.write(routes_no_geo.to_html())
# webbrowser.open('data.html')

# spatially join the routes to nearest stops
join_gdf = gpd.sjoin_nearest(stops, routes)

# create the map first with the service area polygon geojson
map = service_area.explore(
        tiles="CartoDB positron",
        style_kwds={"fill": False, "opacity": 0.3, "color": "darkslategrey"},
        legend=False,
        zoom_start=12)
# next add the routes using the colormap from the new route_color dict
routes.explore(
        m=map,
        column="route_long_name",
        style_kwds={"weight": 7, "opacity": 0.7},
        legend=True,
        cmap=colors.ListedColormap(list(route_color.values()))
        )
# then add the stops using the same colormap matched by route_long_name
join_gdf.explore(
        m=map,
        column="route_long_name",
        cmap=colors.ListedColormap(list(route_color.values())),
        marker_kwds={"radius": 6, "fill": False, "opacity": 0.7},
        legend=False,
        )
# Lastly open map in browser since we are not in a Jupyter Notebook
map.show_in_browser()
