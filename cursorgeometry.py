import arcpy
import os
from my_time_utils import timing

@timing
def cursor_geometry_xy(table):
    with arcpy.da.SearchCursor(table, 'SHAPE@') as cursor:
        for row in cursor:
            centroid = row[0].trueCentroid
            xy = centroid.X, centroid.Y

@timing
def cursor_just_xy(table):
    with arcpy.da.SearchCursor(table, 'SHAPE@XY') as cursor:
        for row in cursor:
            xy = row[0]

if __name__ == "__main__":        
    fc = os.path.join(os.path.dirname(__file__), 
                      "world_airports.gdb\\Airports")


    cursor_geometry_xy(fc)  # ignore first
    
    # Access just two
    cursor_geometry_xy(fc)
    
    # Access all fields
    cursor_just_xy(fc)
