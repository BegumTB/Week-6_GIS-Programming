
# In[1]:


import arcpy
import numpy
import os


# In[6]:


# Get input Raster properties
inRas = arcpy.Raster (r"C:\Users\begum.tanriverdi\Documents\00_CPS-GIS Courses\GIS6345 GIS Programming\Week 6\Banning.tif")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth


# In[7]:


# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)


# In[17]:


# Calculate percentage of the row for each cell value
arrSum = arr.sum(1)
arrSum.shape = (arr.shape[0],4)
arrPerc = (arr)/arrSum


# In[16]:


# Convert Array to raster (keep the origin and cellsize the same as the input)
newRaster = arcpy.NumPyArrayToRaster(arrPerc,lowerLeft,cellSize,
                                     value_to_nodata=0)
newRaster.save("C:\\Users\begum.tanriverdi\Documents\00_CPS-GIS Courses\GIS6345 GIS Programming\Week 6\Raster to NumPy\Raster to NumPy.gdb")


# In[ ]:




