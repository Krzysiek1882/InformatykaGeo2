import geopandas
import numpy as np
from matplotlib import pyplot as plt



gdf = geopandas.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf.to_crs("EPSG:4326")
gdf.plot("TOT", legend = True)
gdf['centroid'] = gdf.centroid

import math as m
a = 5
b = 10
a*b

