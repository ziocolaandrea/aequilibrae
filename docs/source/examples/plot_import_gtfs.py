"""
Import GTFS
===========

On this example, we import a GTFS feed to our model. We will also perform map matching. 

We use data from Coquimbo, a city in La Serena Metropolitan Area in Chile.

"""
# %%
## Imports
from uuid import uuid4
from os import remove
from os.path import join
from tempfile import gettempdir

import folium
import pandas as pd
from aequilibrae.project.database_connection import database_connection

from aequilibrae.transit import Transit
from aequilibrae.utils.create_example import create_example

"""Let's create an empty project on an arbitrary folder."""
# %%
fldr = join(gettempdir(), uuid4().hex)

project = create_example(fldr, "coquimbo")

"""
As Coquimbo example already has a complete GTFS model, we shall remove its public transport  
database for the sake of this example.
"""
# %%
remove(join(fldr, "public_transport.sqlite"))

"""Let's import the GTFS feed."""
# %%

dest_path = join(fldr, "gtfs_coquimbo.zip")

"""
Now we create our Transit object and import the GTFS feed into our model.
This will automatically create a new public transport database.
"""
# %%
data = Transit(project)

transit = data.new_gtfs_builder(agency="LISANCO", file_path=dest_path)

"""
To load the data, we must chose one date. We're going to continue with 2016-04-13, but feel free 
to experiment any other available dates. Transit class has a function which allows you to check
the available dates for the GTFS feed. 
It should take approximately 2 minutes to load the data.
"""
# %%
transit.load_date("2016-04-13")

"""
Now we execute the map matching to find the real paths.
Depending on the GTFS size, this process can be really time consuming.
"""
# %%
transit.set_allow_map_match(True)
transit.map_match()

"""Finally, we save our GTFS into our model."""
# %%
transit.save_to_disk()

"""
Now we will plot the route we just imported into our model!
"""
conn = database_connection("transit")

links = pd.read_sql("SELECT seq, ST_AsText(geometry) geom FROM pattern_mapping WHERE geom IS NOT NULL;", con=conn)

stops = pd.read_sql("""SELECT stop_id, ST_X(geometry) X, ST_Y(geometry) Y FROM stops""", con=conn)

# %%
gtfs_links = folium.FeatureGroup("links")
gtfs_stops = folium.FeatureGroup("stops")

layers = [gtfs_links, gtfs_stops]

for i, row in links.iterrows():
    points = row.geom.replace("LINESTRING", "").replace("(", "").replace(")", "").split(", ")
    points = "[[" + "],[".join([p.replace(" ", ", ") for p in points]) + "]]"
    points = [[x[1], x[0]] for x in eval(points)]

    _ = folium.vector_layers.PolyLine(points, popup=f"<b>link_id: {row.seq}</b>", color="red", weight=2).add_to(
        gtfs_links
    )

for i, row in stops.iterrows():
    point = (row.Y, row.X)

    _ = folium.vector_layers.CircleMarker(
        point,
        popup=f"<b>link_id: {row.stop_id}</b>",
        color="black",
        radius=5,
        fill=True,
        fillColor="black",
        fillOpacity=1.0,
    ).add_to(gtfs_stops)

# %%
# We create the map
map_osm = folium.Map(location=[-29.9633719, -71.3242825], zoom_start=13)

# add all layers
for layer in layers:
    layer.add_to(map_osm)

# And Add layer control before we display it
folium.LayerControl().add_to(map_osm)
map_osm

# %%
project.close()
