# Import system modules
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\intermediate well files.gdb"
arcpy.env.overwriteOutput = True
#arcpy.env.scratchWorkspace = "C:\ArcMap_SSD_Workspace\SSD_SCRATCH_WORKSPACE.gdb"
#input feature class
out_location = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\intermediate well files.gdb"
arcpy.CheckOutExtension("3D")

#add Z values to the well points by interpolating the shape off the 1/3rd arc seconcd dems
#this takes a long time!

def add_elev():
    try:
        # Set the local variables
        arcpy.env.overwriteOutput = True
        inraster = 'G:\Elevation Data\one_third_arcsecond_usgs_dems\NED_elevation_1_3rd_arcsecond.gdb\\elevation'
        infc = 'AL_TN_KY_wells83'
        outfc = 'AL_TN_KY_wells83_elv'
        method = "BILINEAR"
        Z_factor="3.28084"
    #Z_factor converts meters to feet
        arcpy.InterpolateShape_3d(in_surface=inraster,
                              in_feature_class=infc,
                              out_feature_class=outfc,
                              method=method)
        print('zvalues added to well points')


    except Exception as err:
        print(err.args[0])

