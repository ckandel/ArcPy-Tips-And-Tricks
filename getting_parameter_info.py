import arcpy

for tool in arcpy.ListTools():
    for p in arcpy.GetParameterInfo(tool):
        if p.parameterType == 'Derived' and p.datatype == 'Long':
            print('Tool: {}\n\tparameter: {}'.format(tool, p.displayName))
            