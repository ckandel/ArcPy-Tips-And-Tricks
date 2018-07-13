import arcpy
import os
from my_time_utils import timing


@timing
def cursor_fields(table, fields='*'):
    with arcpy.da.SearchCursor(table, fields) as cursor:
        for row in fields:
            pass

if __name__ == "__main__":        
    fc = os.path.join(os.path.dirname(__file__), 
                      "world_airports.gdb\\Airports")
    
    cursor_fields(fc)  # ignore first run
        
    # Access just two
    cursor_fields(fc, ['name', 'FLOODRISK'])
    
    # Access all fields (50+)
    cursor_fields(fc)
    