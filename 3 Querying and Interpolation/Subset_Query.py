import arcpy

#remember to pause google drive before running

arcpy.env.workspace = "C:\Users\Ken\Google Drive\TN Structure\OG_initial_well_files\intermediate files\intermediate well files.gdb"
arcpy.env.overwriteOutput = True

infc = 'wells_ready_for_checking'

#makes a layer files that holds the source data
arcpy.MakeFeatureLayer_management(sourcefc, "Wells_lyr")

mdcquery="(Combo_Units IN ('-Ccr-Mfp', '-Cr-Mfp', 'Sll-Dc', 'Sl-Dc', 'Dc-Sl', 'Dc-Sll', 'Sob-Dc', 'Dc-Sob', 'Oc-Dc', 'Ccr-Mfp', 'Ccr-Mfp', 'Db-MDfpc', 'Db-Mfp', 'Dch-Mfp', 'Dcr-Mfp', 'Dfg-Mfp', 'Dfgr-Mfp', 'Dh-Mfp', 'Dhr-Mfp', 'Dr-Mfp', 'DSu-Mfp', 'Fe-Mfp', 'Mb-Mfp', 'Mdc-Mfp', 'MDc-Mfp', 'MDfpc-Ofl', 'MDfpc-Ofs', 'MDfpc-Olcy', 'MDfpc-Olic', 'MDfpc-Os', 'MDfpc-Sbr', 'MDfpc-Swbr', 'Mf-Mfc', 'Mfp-Al', 'Mfp-Cc', 'Mfp-Dch', 'Slo-Dc', 'Dc-Slo', 'Mfp-Dcr', 'Mfp-Dfg', 'Mfp-Dh', 'Mfp-Dhr', 'Sw-Dp', 'Dp-Sw', 'Dp-Os', 'Os-Dp', 'Mfp-Dpc', 'Mfp-Dr', 'Mfp-DSu', 'Mfp-Fe', 'Mfp-Mb', 'Mfp-Mdc', 'Mfp-MDc', 'Mfp-O-Ck', 'Mfp-Obc', 'Mfp-Oc', 'Mfp-Ochu', 'Mfp-OCk', 'Mfp-Ocy', 'Mfp-Ofa', 'Mfp-Oh', 'Mfp-Ol', 'Mfp-Olcy', 'Mfp-Oma', 'Mfp-Omf', 'Mfp-Omfa', 'Mfp-Omfl', 'Mfp-Omfs', 'Mfp-Omn', 'Mfp-Or', 'Mfp-Orh', 'Mfp-Os', 'Mfp-Osr', 'Mfp-Sbp', 'Mfp-Sbr', 'Sbr-Mfp', 'Mfp-Rl', 'Mfp-Sd', 'Mfp-Sdx', 'Mfp-Sl', 'Mfp-So', 'Mfp-Sr', 'Mfp-Su', 'Mfp-Sw', 'Sw-Mfp', 'Mfp-Swbr', 'O-Ck-Mfp', 'Obc-Mfp', 'Oc-Mfp', 'Ocn-Mfp', 'Ocy-Mfp', 'Ofa-Mfp', 'Ofl-MDfpc', 'Ofs-MDfpc', 'Oh-Mfp', 'Ol-Mfp', 'Olcy-MDfpc', 'Olcy-Mfp', 'Olic-MDfpc', 'Oma-Mfp', 'Omf-Mfp', 'Omfa-Mfp', 'Omfs-Mfp', 'Omn-Mfp', 'Or-Mfp', 'Os-Mfp', 'Os-MDfpc', 'Osr-Mp', 'Dc-Oc', 'Dsb-MDna', 'MDna-Dsb', 'So-Dnsb', 'Do-Sae', 'Do-Sbi', 'Sbi-Do', 'Do-Se', 'Se-Do', 'Do-Sa', 'Sa-Do', 'Sae-Do', 'Mb-Dna', 'Do-Db', 'Db-Do', 'Dna-Mb', 'Dc-Od', 'Dc-Sb', 'Dc-Slo', 'Dc-Slwl', 'Dc-Sob', 'Dc-SOlc', 'Oc-Dc', 'Od-Dc', 'Sb-Dc', 'Slo-Dc', 'Slwl-Dc', 'Sob-Dc', 'SOlc-Dc', 'Dc-Db', 'Db-Dc', 'Db-MDna','Mdna-Db','Mdna-Odr','Odr-Mdna','MDna-So','MDna-Sl','MDna-Sd','MDna-Sco','MDna-Scb','MDna-Sbi','MDna-Sb','MDna-Sae','MDna-Sa','MDna-Ogl','MDna-Og','MDna-Odr','MDna-Odb','MDna-Od','MDna-Ocf','MDna-Occ','MDna-Oate','MDna-Oat','MDna-Oasg','MDna-Oart','MDna-Oar','MDna-Oag','MDna-Oa','So-MDna','Sl-MDna','Sd-MDna','Sco-MDna','Scb-MDna','Sbi-MDna','Sb-MDna','Sae-MDna','Sa--MDna','Ogl-MDna','Og-MDna','Odr-MDna','Odb-MDna','Od-MDna','Ocf-MDna','Occ-MDna','Oate-MDna','Oat-MDna','Oasg--MDna','Oart-MDna','Oar-MDna','Oag-MDna','Oa-MDna','MDna-Db','Dnsb-Slv','Dnsb-Sb','Dnsb-Sl','Dnsb-Slw','Dnsb-Slwl','Dnsb-So','Slv-Dnsb','Sb-Dnsb','Sl-Dnsb','Slw-Dnsb','Slwl-Dnsb','So--Dnsb'))"



knoxquery = "(FRMATN = 'Knox-Ordovician' OR FRMATN = 'Knox Gp') AND (( elev_difference >= -20) OR (elev_difference <= 20))"

wcquery="(FRMATN = 'Wells Creek Fm' OR FRMATN = 'Wells Creek') AND (( elev_difference >= -20) OR (elev_difference <= 20)) AND ( Formation_Sea_Level >-15000)"

Ocquery="(FRMATN = 'Stones Riv Grp' OR FRMATN = 'Stones River' OR FRMATN = 'carters' OR FRMATN = 'Carters' OR FRMATN = 'Carters Lime' OR FRMATN = 'Tyrone Ls, High Bridge Gp' OR  FRMATN = 'Millbrig Bent' OR  FRMATN = 'Mud Cave' OR  FRMATN = 'Mud Cave Bentonite, High Bridge Gp' OR FRMATN = 'mud cave' OR FRMATN = 'High Bridge Gp' OR FRMATN = 'Black River Stage') AND (elev_difference >= -20 AND elev_difference <= 20 AND API <> '16057003970000' AND API <> '137-20720' AND API <> '129-20725' AND API <> '129-20863')"



#knox selection

try:
    fcname='knox_wells'

    arcpy.SelectLayerByAttribute_management(
        in_layer_or_view="Wells_lyr",
        selection_type='NEW_SELECTION',
        where_clause=knox)

    #export the selected features
    arcpy.CopyFeatures_management("Wells_lyr", fcname)
    # Print the total rows
    count = arcpy.GetCount_management(fcname)
    print(str(count) + ' rows in ' + str(fcname))
except Exception as err:
    print(err.args[0])


#Wells Creek selection

try:
    fcname='wells_creek_wells'

    arcpy.SelectLayerByAttribute_management(
        in_layer_or_view="Wells_lyr",
        selection_type='NEW_SELECTION',
        where_clause=wellscreek)

    #export the selected features
    arcpy.CopyFeatures_management("Wells_lyr", fcname)
    # Print the total rows
    count = arcpy.GetCount_management(fcname)
    print(str(count) + ' rows in ' + str(fcname))
except Exception as err:
    print(err.args[0])


#Carters selection

try:
    fcname='carters_wells'

    arcpy.SelectLayerByAttribute_management(
        in_layer_or_view="Wells_lyr",
        selection_type='NEW_SELECTION',
        where_clause=carters)

    #export the selected features
    arcpy.CopyFeatures_management("Wells_lyr", fcname)
    # Print the total rows
    count = arcpy.GetCount_management(fcname)
    print(str(count) + ' rows in ' + str(fcname))
except Exception as err:
    print(err.args[0])
