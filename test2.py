import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd


df = pd.read_csv("./data-sample/test1.csv",
                 usecols=["decimalLatitude", "decimalLongitude"],
                 )

# initialize an axis
fig, ax = plt.subplots(figsize=(8,6))

# plot map on axis
countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == "New Zealand"].plot(color="lightgrey", ax=ax)

# plot points
df.plot(x="decimalLongitude", y="decimalLatitude", kind="scatter", colormap="YlOrRd", 
        title=f"NZ ", ax=ax)

# add grid
ax.grid(b=True, alpha=0.5)

plt.show()