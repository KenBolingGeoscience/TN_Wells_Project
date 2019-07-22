# Add the name of the quad as a field for each quad

import arcpy

# allow files to be overwritten
arcpy.env.overwriteOutput = "TRUE"

# Set the workspace for the ListFeatureClass function
arcpy.env.workspace = "C:\\ArcMap_SSD_Workspace\\Nashville_Files.gdb"

# adds a field with the map index number from the file name
# to each of the different file types

try:
     for fc in arcpy.ListFeatureClasses("","all",""):

             map_name = fc
             map_name = map_name.replace('_polygon', '')
             map_name = map_name.replace('_label', '')
             map_name = map_name.replace('_arc', '')
             map_name = map_name.replace('_tic', '')


             arcpy.AddField_management(fc, "map_name", "TEXT","","","30")

             arcpy.CalculateField_management(fc, "map_name","\"" + map_name + "\"", "PYTHON")

except:
     print ("It's not working")
     print (arcpy.GetMessages())

else:
    print ("It Works!")
