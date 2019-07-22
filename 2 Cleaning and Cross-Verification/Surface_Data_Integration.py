

import arcpy
#add the desired fields to the file

arcpy.env.overwriteOutput = True

arcpy.env.workspace ='C:\\Users\\Ken\\Google Drive\\TN Structure\\Geologic Map Data.gdb'

arcpy.ddd.InterpolateShape(surface, fc, outFC,
                                           10, 1, method, True)

tn24k='TN_24K_Lines_NAD83_UTM16_intshp_pnts'
ky24k='KY_24K_Lines_NAD83_UTM16_intshp_pnts'
tnquery = '('+'"'+'OBJECTID'+'"'+' / 6= round( '+'"'+'OBJECTID'+'"'+' /6,0) or '+'"'+'OBJECTID'+'"'+" = 1) AND (LINE <> 'BOUND') AND map_name NOT IN ('sw_418', 'se_418',  'sw_426', 'se_426', 'sw_434', 'se_434', 'sw_442', 'se_442',  'ne_18', 'nw_28', 'ne_28',  'ne_300', 'nw_300', 'ne_301',  'nw_301',  'ne_303',  'nw_303',  'nw_306', 'ne_306', 'nw_309', 'ne_309', 'nw_312', 'ne_312', 'nw_316', 'ne_316',  'nw_320',  'ne_320', 'nw_324',  'ne_324', 'nw_329', 'ne_329', 'nw_333', 'ne_333',  'nw_335', 'ne_335', 'nw_336', 'ne_336', 'nw_337',  'ne_337', 'nw_338',  'ne_338', 'nw_144', 'ne_144' )"
kyquery ='('+'"'+'OBJECTID'+'"'+' / 6= round( '+'"'+'OBJECTID'+'"'+' /6,0) or '+'"'+'OBJECTID'+'"'+" = 1) AND (contact_type = 'CONTACT')"
tn24kout = 'tn24k_cleaned'
ky24kout = 'ky24k_cleaned'
tnkymerge = 'TN_KY_cleaned'

#creates layers
try:
    arcpy.MakeFeatureLayer_management(
        in_features=tn24k,
        out_layer=tn24kout,
        where_clause=tnquery)
    print("tnlayer created")

    arcpy.MakeFeatureLayer_management(
        in_features=ky24k,
        out_layer=ky24kout,
        where_clause=kyquery)
    print("kylayer created")

    arcpy.Merge_management(inputs=[tn24kout,ky24kout],
                           output=tnkymerge,
                           field_mappings='LINE "LINE" true true false 7 Text 0 0 ,First,#,TN_24K_Lines_NAD83_UTM16_intshp_pnts,LINE,-1,-1;Combo_Units "Combo_Units" true true false 20 Text 0 0 ,First,#,TN_24K_Lines_NAD83_UTM16_intshp_pnts,Combo_Units,-1,-1,KY_24K_Lines_NAD83_UTM16_intshp_pnts,Combo_Units,-1,-1;identifier "identifier" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,identifier,-1,-1;name "name" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,name,-1,-1;description "description" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,description,-1,-1;contactType "contactType" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,contactType,-1,-1;observationMethod "observationMethod" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,observationMethod,-1,-1;source "source" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,source,-1,-1;contact_type "contact_type" true true false 10 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,contact_type,-1,-1;formation_code "formation_code" true true false 8 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,formation_code,-1,-1;contact_style "contact_style" true true false 20 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,contact_style,-1,-1;geologicUnitType_uri "geologicUnitType_uri" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,geologicUnitType_uri,-1,-1;representativeLithology_uri "representativeLithology_uri" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,representativeLithology_uri,-1,-1;representativeOlderAge_uri "representativeOlderAge_uri" true true false 255 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,representativeOlderAge_uri,-1,-1;kgs_formation_code "kgs_formation_code" true true false 8 Text 0 0 ,First,#,KY_24K_Lines_NAD83_UTM16_intshp_pnts,kgs_formation_code,-1,-1')
except Exception as err:
    print(err.args[0])

