# Converts polygons to line features representing the geologic contacts for every quad
# This process collects the FID information about the neighboring polygons for each line segment
# The FID is then matched with the label on each polygon to get the geologic unit information

import arcpy

# Set the workspace environment

arcpy.env.workspace = "C:\\ArcMap_SSD_Workspace\\Nashville_Files.gdb"

feature_class_list = arcpy.ListFeatureClasses("*_arc")


# convert polygons to lines keeping neighbor FID information by default
arcpy.PolygonToLine_management(in_features = fc, out_feature_class = outFeatureClass)

# use FID info to get the geologic units on either side of the geologic contact
for fc in feature_class_list:

    # get the original FIDs of the polygons
    polygon_features = fc.replace('_arc', '_polygon')

    in_features = fc
    join_field_left = "LEFT_FID"
    join_field_right = "RIGHT_FID"
    join_field_target = "OBJECTID"
    field_name = ["Geology"]

    arcpy.JoinField_management(in_data = in_features,
                               in_field = join_field_left,
                               join_table = polygon_features,
                               join_field = join_field_target,
                               fields= field_name)

    arcpy.JoinField_management(in_data=in_features,
                               in_field=join_field_right,
                               join_table=polygon_features,
                               join_field=join_field_target,
                               fields=field_name)

    combofield = "Combo_Units"

    ComboFieldsExpression = "!Geology! + '-' + !Geology_1!"
    arcpy.AddField_management(in_features, combofield, "TEXT", "", "", "20")
    arcpy.CalculateField_management(in_features, combofield, ComboFieldsExpression, "PYTHON")

