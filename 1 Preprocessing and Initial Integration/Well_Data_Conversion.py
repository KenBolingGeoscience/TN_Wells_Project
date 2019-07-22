# Import system modules
import arcpy

#remember to delete layer files and schema before rerunning

# Set environment settings
arcpy.env.workspace = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\intermediate well files.gdb"
arcpy.env.overwriteOutput = True

#input feature class
out_location = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\intermediate well files.gdb"


#load the AL csv file, create a layer using the XY coordinates, and save as a feature class

try:
    # Set the local variables
    arcpy.env.overwriteOutput = True
    alogwells = 'C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\alogwells.csv'
    alx_coords = "Longitude"
    aly_coords =  "Latitude"
    alout_Layer = "alogwells"
    alsaved_Layer = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\alogwells.lyr"

    # Set the spatial reference
    alspRef = r"Coordinate Systems\Projected Coordinate Systems\NAD 1927.prj"

    # Make the XY event layer for tnogwells
    arcpy.MakeXYEventLayer_management(alogwells, alx_coords, aly_coords, alout_Layer, alspRef)

    # Print the total rows
    print(arcpy.GetCount_management(alout_Layer))

    # Save to a layer file
    arcpy.SaveToLayerFile_management(alout_Layer, alsaved_Layer)

    #convert to feature class
    arcpy.FeatureClassToFeatureClass_conversion(alsaved_Layer, out_location, out_name='alogwells')

except Exception as err:
    print(err.args[0])


#load the KY csv file, create a layer using the XY coordinates, and save as a feature class

try:
    # Set the local variables
    arcpy.env.overwriteOutput = True
    kyogwells = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\kyogwells.csv"
    kyx_coords = "Rec_Lng83"
    kyy_coords =  "Rec_Lat83"
    kyout_Layer = "kyogwells"
    kysaved_Layer = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\kyogwells.lyr"

    # Set the spatial reference
    kyspRef = r"Coordinate Systems\Projected Coordinate Systems\NAD 1983.prj"


    # Make the XY event layer for tnogwells
    arcpy.MakeXYEventLayer_management(kyogwells, kyx_coords, kyy_coords, kyout_Layer, kyspRef)

    # Print the total rows
    print(arcpy.GetCount_management(kyout_Layer))

    # Save to a layer file
    arcpy.SaveToLayerFile_management(kyout_Layer, kysaved_Layer)

    #convert to feature class
    arcpy.FeatureClassToFeatureClass_conversion(kysaved_Layer, out_location, out_name='kyogwells')

except Exception as err:
    print(err.args[0])

#load the TN csv file, create a layer using the XY coordinates, and save as a feature class

try:
    # Set the local variables
    arcpy.env.overwriteOutput = True
    tnogwells = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\tnogwells.csv"
    tnx_coords = "TSPEAST27"
    tny_coords =  "TSPNRTH27"
    tnout_Layer = "tnogwells"
    tnsaved_Layer = "C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\tnogwells.lyr"

    # Set the spatial reference
    tnspRef = r"Coordinate Systems\Projected Coordinate Systems\NAD 1927 StatePlane Tennessee FIPS 4100.prj"

    # Make the XY event layer for tnogwells
    arcpy.MakeXYEventLayer_management(tnogwells, tnx_coords, tny_coords, tnout_Layer, tnspRef)

    # Print the total rows
    print(arcpy.GetCount_management(tnout_Layer))

    # Save to a layer file
    arcpy.SaveToLayerFile_management(tnout_Layer, tnsaved_Layer)

    #convert to feature class
    arcpy.FeatureClassToFeatureClass_conversion(tnsaved_Layer, out_location, out_name='tnogwells')

except Exception as err:
    print(err.args[0])


#convert the AL coordinates to NAD 1983
try:
    # Set the local variables
    arcpy.env.overwriteOutput = True


    fcin = "alogwells"
    fcout = 'alogwells83'
    outCS = arcpy.SpatialReference('NAD 1983')


    arcpy.Project_management(fcin, fcout, outCS)
    print ('alwells converted to nad 1983')

except Exception as err:
    print(err.args[0])

#convert the TN coordinates to NAD 1983
try:
    # Set the local variables
    arcpy.env.overwriteOutput = True


    fcin = "tnogwells"
    fcout = 'tnogwells83'
    outCS = arcpy.SpatialReference('NAD 1983')


    arcpy.Project_management(fcin, fcout, outCS)
    print ('tnwells converted to nad 1983')

except Exception as err:
    print(err.args[0])


#convert the KY coordinates to NAD 1983
try:
    # Set the local variables
    arcpy.env.overwriteOutput = True
    fcin1 = 'tnogwells83'
    fcin2 = 'kyogwells'
    fcout = 'merged_wells83'

    arcpy.Merge_management(inputs=[fcin1, fcin2],
                           output=fcout,
                           field_mappings='Field1 "Field1" true true false 4 Long 0 0 ,First,#,tnogwells83,Field1,-1,-1,kyogwells,Field1,-1,-1;API "API" true true false 8000 Text 0 0 ,First,#,tnogwells83,API,-1,-1,kyogwells,API,-1,-1;ELEVTN "ELEVTN" true true false 8 Double 0 0 ,First,#,tnogwells83,ELEVTN,-1,-1,kyogwells,ELEVTN,-1,-1;FRMATN "FRMATN" true true false 8000 Text 0 0 ,First,#,tnogwells83,FRMATN,-1,-1,kyogwells,FRMATN,-1,-1;QUADNAME "QUADNAME" true true false 8000 Text 0 0 ,First,#,tnogwells83,QUADNAME,-1,-1,kyogwells,QUADNAME,-1,-1;WELLNAME "WELLNAME" true true false 8000 Text 0 0 ,First,#,tnogwells83,WELLNAME,-1,-1,kyogwells,Org_Farm,-1,-1;bestpick "bestpick" true true false 8 Double 0 0 ,First,#,tnogwells83,bestpick,-1,-1,kyogwells,bestpick,-1,-1')
    print ('wells merged')


except Exception as err:
    print(err.args[0])

arcpy.Merge_management(inputs="alogwells83;merged_wells83",
                       output="C:/Users/Ken/Google Drive/TN Structure/OG_initial_well_files/intermediate files/intermediate well files.gdb/AL_TN_KY_wells83", field_mappings='API "API" true true false 8000 Text 0 0 ,First,#,alogwells83,API,-1,-1,merged_wells83,API,-1,-1;Elevation "Elevation" true true false 8 Double 0 0 ,First,#,alogwells83,Elevation,-1,-1,merged_wells83,ELEVTN,-1,-1;WellName "WellName" true true false 8000 Text 0 0 ,First,#,alogwells83,WellName,-1,-1,merged_wells83,WELLNAME,-1,-1;FORMATION "FORMATION" true true false 8000 Text 0 0 ,First,#,alogwells83,FORMATION,-1,-1,merged_wells83,FRMATN,-1,-1;bestpick "bestpick" true true false 4 Long 0 0 ,First,#,alogwells83,bestpick,-1,-1,merged_wells83,bestpick,-1,-1')


