# 30DayMap2023
Repo for python code and projects related to the 2023 30DayMapChallenge.  
Working from terminal & neovim in arch linux, running interactive python
terminal testing ipython & pyqt5.    
Exploring how much prototyping and visualization is possible without using a 
full Jupyter Notebook, which lags on this 4GB RAM Chromebook :)  
### Projects
- kmetro Analysis
    - Kalamazoo Metro Transit GTFS feed from Transitland data 
    - Added geojson to recognized neovim formats
    - Created shortcut for jq library to pretty format geojson
    - Utilized geopandas explore and folium to generate map
    - Created a custom color map so routes and stops would match
    - map has a .show_in_browser() method to open folium in browser
