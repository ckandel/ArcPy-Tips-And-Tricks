import arcpy

print("scratch gdb is {}".format(arcpy.env.scratchGDB))

arcpy.Delete_management(arcpy.env.scratchGDB)

# scratchGDB (and scratchFolder) will always exist if you need it
print("scratch gdb is {}".format(arcpy.env.scratchGDB))

