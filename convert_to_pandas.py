import arcpy
import pandas
import os


def convert_to_pandas_df(table):
    # Get a list of field names to display
    field_names = [i.name for i in arcpy.ListFields(table) if i.type != 'OID']
    
    # Open a cursor to extract results from stats table
    cursor = arcpy.da.SearchCursor(table, field_names)
    
    # Create a pandas dataframe to display results
    df = pandas.DataFrame(data=[row for row in cursor],
                          columns=field_names)

    return df


if __name__ == "__main__":        
    fc = os.path.join(os.path.dirname(__file__), 
                      "world_airports.gdb\\Airports")

    data_frame = convert_to_pandas_df(fc)
    print(data_frame.head())
    