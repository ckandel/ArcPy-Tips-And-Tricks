import arcpy
from my_time_utils import timing

arcpy.env.overwriteOutput = True

@timing
def create_geom_with_obj(fc, coords, sr):
    with arcpy.da.InsertCursor(fc, 'SHAPE@') as cursor:
        for coordset in coords:
            line = arcpy.Polyline(
                arcpy.Array([arcpy.Point(i[0], i[1]) for i in coordset]), 4326)
            cursor.insertRow([line])

@timing    
def create_geom_with_coords(fc, coords, sr):
    with arcpy.da.InsertCursor(fc, 'SHAPE@') as cursor:
        for coordset in coords:
            cursor.insertRow([coordset])


if __name__ == "__main__":
    
    fc = arcpy.CreateFeatureclass_management(arcpy.env.scratchGDB,
                                             'line_fc',
                                             'POLYLINE',
                                             spatial_reference=4326)[0]

    coords = [[(-137.7129, 27.5053), (-137.6948, 27.5068), 
               (-137.7486, 27.8083), (-137.7296, 27.7905)],
              [(-138.1582, 27.6142), (-138.1167, 27.5895),
               (-137.4899, 27.7587), (-137.4865, 27.7584)],
              [(-137.4865, 27.7584), (-137.4779, 27.7575),
               (-137.4779, 27.7575), (-137.4664, 27.7567)],
              [(-137.4664, 27.7567), (-137.4617, 27.7563),
               (-137.4617, 27.7563), (-137.4446, 27.7560)],
              [(-137.4446, 27.7560), (-137.4403, 27.7559),
               (-137.4403, 27.7559), (-137.4355, 27.7558)],
              [(-137.4355, 27.7558), (-137.4316, 27.7557),
               (-137.4316, 27.7557), (-137.4146, 27.7558)]]
    
    create_geom_with_obj(fc, coords, 4326)
    create_geom_with_coords(fc, coords, 4326)