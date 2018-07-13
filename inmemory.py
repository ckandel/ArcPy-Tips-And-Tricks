"""
This particular case showed modest gains. Other cases show multiple factor
gains.
"""


import arcpy
import os
from my_time_utils import timing

arcpy.env.overwriteOutput = True

@timing
def process_gdb(fc):  # 319 seconds
    for i in range(4):
        fc = arcpy.Buffer_analysis(
            fc, '{}\\fc_{}'.format(arcpy.env.scratchGDB, i), '100 meters')

@timing
def process_inmemory(fc):  # 280 seconds
    for i in range(4):
        fc = arcpy.Buffer_analysis(
            fc, 'in_memory\\fc_{}'.format(i), '100 meters')
    
    
if __name__ == "__main__":        
    fc = os.path.join(os.path.dirname(__file__), 
                      "world_airports.gdb\\Airports")

    process_gdb(fc)
    process_inmemory(fc)
    

