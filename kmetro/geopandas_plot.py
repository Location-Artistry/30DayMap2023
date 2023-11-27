import geopandas as gpd
import folium

routes = gpd.read_file('kmetro_routes.geojson')
stops = gpd.read_file('kmetro-stops.geojson')
service_area = gpd.read_file('kmetro_area.geojson')

map = service_area.explore(
        tiles="CartoDB positron",
        style_kwds={"fill": False},
        legend=False
        )
map = routes.explore(
        m=map,
        column="route_long_name",
        style_kwds={"weight": 5, "fillOpacity": 0.1},
        legend=False
        )
stops.explore(
        m=map,
        column="stop_code",
        marker_kwds=dict(radius=5, fill=True),
        legend=False
        )

map.show_in_browser()
