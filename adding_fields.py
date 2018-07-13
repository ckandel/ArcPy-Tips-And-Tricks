import arcpy
import numpy
import os
from my_time_utils import timing

arcpy.env.overwriteOutput = True

@timing
def add_fields_by_extend(fc):
   
    # Join fields to the feature class, using ExtendTable
    inarray = numpy.array([],
                          numpy.dtype([('intfield', numpy.int32),
                                       ('Name', '|S10'),
                                       ('Descript', '|S10'),
                                       ('Type', '|S255'),
                                       ('Comment', '|S10'),
                                       ('Symbol', '|S10'),
                                       ('DateTimeS', '|S10'),
                                       ('Elevation', numpy.float),
                                       ]))
    
    arcpy.da.ExtendTable(fc, "OID@", inarray, "intfield")

@timing
def add_fields(fc):
    
    arcpy.AddField_management(fc, 'intfield', 'LONG')
    arcpy.AddField_management(fc, 'Name', 'TEXT', field_length=10)
    arcpy.AddField_management(fc, 'Descript', 'TEXT', field_length=10)
    arcpy.AddField_management(fc, 'Type', 'TEXT', field_length=255)
    arcpy.AddField_management(fc, 'Comment', 'TEXT', field_length=10)
    arcpy.AddField_management(fc, 'Symbol', 'TEXT', field_length=10)
    arcpy.AddField_management(fc, 'DateTimeS', 'TEXT', field_length=10)
    arcpy.AddField_management(fc, 'XX', 'FLOAT')


if __name__ == "__main__":        
    sr = arcpy.SpatialReference(4326, 115700)
    fc1 = arcpy.CreateFeatureclass_management(arcpy.env.scratchGDB, 
                                              'add_field_1', 'POINT', 
                                              spatial_reference=sr)[0]
    
    
    fc2 = arcpy.CreateFeatureclass_management(arcpy.env.scratchGDB, 
                                              'add_field_2', 'POINT', 
                                              spatial_reference=sr)[0]

    add_fields_by_extend(fc1)
    add_fields(fc2)