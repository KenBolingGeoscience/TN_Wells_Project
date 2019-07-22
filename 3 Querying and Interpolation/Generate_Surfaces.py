# Import system modules
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\intermediate well files.gdb"
arcpy.env.overwriteOutput = True

Input_points_fc = "whatever"
Input_barriers =''
mdcquery="FORMATION IN ('Chatt shale', 'Chatt Shale', 'Chattanooga Sh', 'Chattanooga Shale', 'Ohio Sh', 'Ohio Shale, Upper Part', 'New Albany Sh', 'New Providence & New Albany Undif'))OR (Combo_Units IN ('-Ccr-Mfp','-Cr-Mfp','Sll-Dc','Sl-Dc','Dc-Sl','Dc-Sll','Sob-Dc','Dc-Sob','Oc-Dc','Ccr-Mfp','Ccr-Mfp','Db-MDfpc','Db-Mfp','Dch-Mfp','Dcr-Mfp','Dfg-Mfp','Dfgr-Mfp','Dh-Mfp','Dhr-Mfp','Dr-Mfp','DSu-Mfp','Fe-Mfp','Mb-Mfp','Mdc-Mfp','MDc-Mfp','MDfpc-Ofl','MDfpc-Ofs','MDfpc-Olcy','MDfpc-Olic','MDfpc-Os','MDfpc-Sbr','MDfpc-Swbr','Mf-Mfc','Mfp-Al','Mfp-Cc','Mfp-Dch','Slo-Dc','Dc-Slo','Mfp-Dcr','Mfp-Dfg','Mfp-Dh','Mfp-Dhr','Sw-Dp','Dp-Sw','Dp-Os','Os-Dp','Mfp-Dpc','Mfp-Dr','Mfp-DSu','Mfp-Fe','Mfp-Mb','Mfp-Mdc','Mfp-MDc','Mfp-O-Ck','Mfp-Obc','Mfp-Oc','Mfp-Ochu','Mfp-OCk','Mfp-Ocy','Mfp-Ofa','Mfp-Oh','Mfp-Ol','Mfp-Olcy','Mfp-Oma','Mfp-Omf','Mfp-Omfa','Mfp-Omfl','Mfp-Omfs','Mfp-Omn','Mfp-Or','Mfp-Orh','Mfp-Os','Mfp-Osr' ,'Mfp-Sbp','Mfp-Sbr','Sbr-Mfp','Mfp-Rl','Mfp-Sd','Mfp-Sdx','Mfp-Sl','Mfp-So','Mfp-Sr','Mfp-Su','Mfp-Sw','Sw-Mfp','Mfp-Swbr','O-Ck-Mfp','Obc-Mfp','Oc-Mfp','Ocn-Mfp','Ocy-Mfp','Ofa-Mfp','Ofl-MDfpc','Ofs-MDfpc','Oh-Mfp','Ol-Mfp','Olcy-MDfpc','Olcy-Mfp','Olic-MDfpc','Oma-Mfp','Omf-Mfp','Omfa-Mfp','Omfs-Mfp','Omn-Mfp','Or-Mfp','Os-Mfp','Os-MDfpc','Osr-Mp','Dc-Oc','Dsb-MDna','MDna-Dsb','So-Dnsb','Do-Sae','Do-Sbi','Sbi-Do','Do-Se','Se-Do','Do-Sa','Sa-Do','Sae-Do','Mb-Dna','Do-Db','Db-Do','Dna-Mb','Dc-Od','Dc-Sb','Dc-Slo','Dc-Slwl','Dc-Sob','Dc-SOlc','Oc-Dc','Od-Dc','Sb-Dc','Slo-Dc','Slwl-Dc','Sob-Dc','SOlc-Dc','Dc-Db','Db-Dc','Db-MDna' ,'Mdna-Db','Mdna-Odr','Odr-Mdna','MDna-So','MDna-Sl','MDna-Sd','MDna-Sco','MDna-Scb','MDna-Sbi','MDna-Sb','MDna-Sae','MDna-Sa','MDna-Ogl','MDna-Og','MDna-Odr','MDna-Odb','MDna-Od','MDna-Ocf','MDna-Occ','MDna-Oate','MDna-Oat','MDna-Oasg','MDna-Oart','MDna-Oar','MDna-Oag','MDna-Oa','So-MDna','Sl-MDna','Sd-MDna','Sco-MDna','Scb-MDna','Sbi-MDna','Sb-MDna','Sae-MDna','Sa--MDna','Ogl-MDna','Og-MDna','Odr-MDna','Odb-MDna','Od-MDna','Ocf-MDna','Occ-MDna','Oate-MDna','Oat-MDna','Oasg--MDna','Oart-MDna','Oar-MDna','Oag-MDna','Oa-MDna','MDna-Db','Dnsb-Slv','Dnsb-Sb','Dnsb-Sl','Dnsb-Slw', 'Dnsb-Slwl', 'Dnsb-So', 'Slv-Dnsb', 'Sb-Dnsb', 'Sl-Dnsb', 'Slw-Dnsb', 'Slwl-Dnsb', 'So--Dnsb'))"

(FORMATION IN ('Chatt shale', 'Chatt Shale', 'Chattanooga Sh', 'Chattanooga Shale', 'Ohio Sh', 'Ohio Shale, Upper Part', 'New Albany Sh', 'New Providence & New Albany Undif')
AND
(( fuckarcmap_elev_difference <= 20) AND (fuckarcmap_elev_difference >= -20)))

OR

(Combo_Units IN ('-Ccr-Mfp','-Cr-Mfp','Sll-Dc','Sl-Dc','Dc-Sl','Dc-Sll','Sob-Dc','Dc-Sob','Oc-Dc','Ccr-Mfp','Ccr-Mfp','Db-MDfpc','Db-Mfp','Dch-Mfp','Dcr-Mfp','Dfg-Mfp','Dfgr-Mfp','Dh-Mfp','Dhr-Mfp','Dr-Mfp','DSu-Mfp','Fe-Mfp','Mb-Mfp','Mdc-Mfp','MDc-Mfp','MDfpc-Ofl','MDfpc-Ofs','MDfpc-Olcy','MDfpc-Olic','MDfpc-Os','MDfpc-Sbr','MDfpc-Swbr','Mf-Mfc','Mfp-Al','Mfp-Cc','Mfp-Dch','Slo-Dc','Dc-Slo','Mfp-Dcr','Mfp-Dfg','Mfp-Dh','Mfp-Dhr','Sw-Dp','Dp-Sw','Dp-Os','Os-Dp','Mfp-Dpc','Mfp-Dr','Mfp-DSu','Mfp-Fe','Mfp-Mb','Mfp-Mdc','Mfp-MDc','Mfp-O-Ck','Mfp-Obc','Mfp-Oc','Mfp-Ochu','Mfp-OCk','Mfp-Ocy','Mfp-Ofa','Mfp-Oh','Mfp-Ol','Mfp-Olcy','Mfp-Oma','Mfp-Omf','Mfp-Omfa','Mfp-Omfl','Mfp-Omfs','Mfp-Omn','Mfp-Or','Mfp-Orh','Mfp-Os','Mfp-Osr' ,'Mfp-Sbp','Mfp-Sbr','Sbr-Mfp','Mfp-Rl','Mfp-Sd','Mfp-Sdx','Mfp-Sl','Mfp-So','Mfp-Sr','Mfp-Su','Mfp-Sw','Sw-Mfp','Mfp-Swbr','O-Ck-Mfp','Obc-Mfp','Oc-Mfp','Ocn-Mfp','Ocy-Mfp','Ofa-Mfp','Ofl-MDfpc','Ofs-MDfpc','Oh-Mfp','Ol-Mfp','Olcy-MDfpc','Olcy-Mfp','Olic-MDfpc','Oma-Mfp','Omf-Mfp','Omfa-Mfp','Omfs-Mfp','Omn-Mfp','Or-Mfp','Os-Mfp','Os-MDfpc','Osr-Mp','Dc-Oc','Dsb-MDna','MDna-Dsb','So-Dnsb','Do-Sae','Do-Sbi','Sbi-Do','Do-Se','Se-Do','Do-Sa','Sa-Do','Sae-Do','Mb-Dna','Do-Db','Db-Do','Dna-Mb','Dc-Od','Dc-Sb','Dc-Slo','Dc-Slwl','Dc-Sob','Dc-SOlc','Oc-Dc','Od-Dc','Sb-Dc','Slo-Dc','Slwl-Dc','Sob-Dc','SOlc-Dc','Dc-Db','Db-Dc','Db-MDna' ,'Mdna-Db','Mdna-Odr','Odr-Mdna','MDna-So','MDna-Sl','MDna-Sd','MDna-Sco','MDna-Scb','MDna-Sbi','MDna-Sb','MDna-Sae','MDna-Sa','MDna-Ogl','MDna-Og','MDna-Odr','MDna-Odb','MDna-Od','MDna-Ocf','MDna-Occ','MDna-Oate','MDna-Oat','MDna-Oasg','MDna-Oart','MDna-Oar','MDna-Oag','MDna-Oa','So-MDna','Sl-MDna','Sd-MDna','Sco-MDna','Scb-MDna','Sbi-MDna','Sb-MDna','Sae-MDna','Sa--MDna','Ogl-MDna','Og-MDna','Odr-MDna','Odb-MDna','Od-MDna','Ocf-MDna','Occ-MDna','Oate-MDna','Oat-MDna','Oasg--MDna','Oart-MDna','Oar-MDna','Oag-MDna','Oa-MDna','MDna-Db','Dnsb-Slv','Dnsb-Sb','Dnsb-Sl','Dnsb-Slw', 'Dnsb-Slwl', 'Dnsb-So', 'Slv-Dnsb', 'Sb-Dnsb', 'Sl-Dnsb', 'Slw-Dnsb', 'Slwl-Dnsb', 'So--Dnsb'))
#Top of the Knox


arcpy.SplineWithBarriers_3d(Input_point_features="Wells_elev_quads83_no_Z",
                            Z_value_field="Formation_Sea_Level_Z_points",
                            Input_barrier_features="Nashville_Jessamine_faults",
                            Output_cell_size="0.02",
                            Output_raster="C:/Users/Ken/Google Drive/TN Structure/Output_Rasters/Structure Contour Maps.gdb/Knox_20_cutoff_spline",
                            Smoothing_Factor="0")




# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Wells_elev_quads83_no_Z", "Nashville_Jessamine_faults"
arcpy.SplineWithBarriers_3d(Input_point_features="Wells_elev_quads83_no_Z",
                            Z_value_field="Formation_Sea_Level_Z_points",
                            Input_barrier_features="Nashville_Jessamine_faults",
                            Output_cell_size=".02",
                            Output_raster="C:/Users/Ken/Google Drive/TN Structure/Output_Rasters/Structure Contour Maps.gdb/Knox_20_cutoff_spline",
                            Smoothing_Factor="0")

arcpy.gp.Contour_sa("Knox",
                    "C:/Users/Ken/Google Drive/TN Structure/Output_Rasters/Structure Contour Maps.gdb/Knox_100ft_Contour",
                    "100",
                    "0",
                    "1")