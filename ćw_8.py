import geopandas
import numpy as np
from matplotlib import pyplot as plt


gdf = geopandas.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf = gdf.to_crs("EPSG:4326")
gdf.plot("TOT", legend = True)
gdf['centroid'] = gdf.centroid

import shapely
#
xmin, ymin, xmax, ymax = [13, 48, 25, 56]
#
n_cells = 30
cell_size = (xmax-xmin)/n_cells
#
grid_cells = []
for x0 in np.arange(xmin, xmax + cell_size, cell_size):
    for y0 in np.arange(ymin, ymax + cell_size, cell_size):
        # bounds
        x1 = x0 - cell_size
        y1 = y0 + cell_size
        grid_cells.append(shapely.geometry.box(x0,y0,x1,y1))
cell = geopandas.GeoDataFrame(grid_cells, columns = ['geometry'])

ax = gdf.plot(markersize =.1, figsize=(12,8), column = 'TOT', cmap = 'jet')
plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor = 'grey')
ax.axis("off")

merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by = "index_right", aggfunc = "sum")

cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values

ax = cell.plot(column ='TOT', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnosci w siatce')


# Przedział wiekowy 0-14:
a = gdf.TOT_0_14
suma_a = sum(a)

cell.loc[dissolve.index, 'TOT_0_14'] = dissolve.TOT_0_14.values
axa = cell.plot(column ='TOT_0_14', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axa.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnosci w siatce dla przedziału wiekowego 0-14')

# Przedział wiekowy 15-64:
b = gdf.TOT_15_64
suma_b = sum(b)

cell.loc[dissolve.index, 'TOT_15_64'] = dissolve.TOT_15_64.values
axb = cell.plot(column ='TOT_15_64', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axb.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnosci w siatce dla przedziału wiekowego 15-64')

# Przedział wiekowy >65:
c = gdf.TOT_65__
suma_c = sum(c)

cell.loc[dissolve.index, 'TOT_65__'] = dissolve.TOT_65__.values
axc = cell.plot(column ='TOT_65__', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axc.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnosci w siatce dla przedziału wiekowego >65')

# Ludnoć męska w przedziale wiekowym 0-14:
d1 = gdf.MALE_0_14
suma_d1 = sum(d1)

cell.loc[dissolve.index, 'MALE_0_14'] = dissolve.MALE_0_14.values
axd1 = cell.plot(column ='MALE_0_14', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axd1.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnoci męsiej w przedziale wiekowym 0-14')

# Ludnoć męska w przedziale wiekowym 15-64:
d2 = gdf.MALE_15_64
suma_d2 = sum(d2)

cell.loc[dissolve.index, 'MALE_15_64'] = dissolve.MALE_15_64.values
axd2 = cell.plot(column ='MALE_15_64', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axd2.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnoci męsiej w przedziale wiekowym 15-64')

# Ludnoć męska w przedziale wiekowym >65:
d3 = gdf.MALE_65__
suma_d3 = sum(d3)

cell.loc[dissolve.index, 'MALE_65__'] = dissolve.MALE_65__.values
axd3 = cell.plot(column ='MALE_65__', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axd3.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnoci męsiej w przedziale wiekowym >64')


# Ludnoć damska w przedziale wiekowym 0-14:
e1 = gdf.FEM_0_14
suma_e1 = sum(e1)

cell.loc[dissolve.index, 'FEM_0_14'] = dissolve.FEM_0_14.values
axe1 = cell.plot(column ='FEM_0_14', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axe1.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnoci damskiej w przedziale wiekowym 0-14')

# Ludnoć damska w przedziale wiekowym 15-64:
e2 = gdf.FEM_15_64
suma_e2 = sum(e2)

cell.loc[dissolve.index, 'FEM_15_64'] = dissolve.FEM_15_64.values
axe2 = cell.plot(column ='FEM_15_64', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axe2.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnoci damskiej w przedziale wiekowym 15-64')

# Ludnoć damska w przedziale wiekowym >65:
e3 = gdf.FEM_65__
suma_e3 = sum(e3)

cell.loc[dissolve.index, 'FEM_65__'] = dissolve.FEM_65__.values
axe3 = cell.plot(column ='FEM_65__', figsize=(12,8), cmap ='viridis', vmax = 700000, edgecolor = "grey", legend = True)
plt.autoscale(False)
axe3.set_axis_off()
plt.axis('equal');
plt.title('Liczba ludnoci damskiej w przedziale wiekowym >65')