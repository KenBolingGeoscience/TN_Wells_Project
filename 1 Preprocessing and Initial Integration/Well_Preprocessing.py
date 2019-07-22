import geopandas as gpd
import pandas as pd
import numpy as np
from simpledbf import Dbf5
import matplotlib
import os

# set working directory
os.chdir('C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files')


# load in the Kentucky O&G well locations shapefile using geopandas
ky_well_locations = gpd.read_file('KY\\kyog_dd.shp')

# Now load in the formation tops data and first check if t here are any duplicate entries (there are).

ky_tops_data = pd.read_csv('KY\\KY_TOPS\\KY_FM_Tops_Data_csv_update.csv')


duplicate_tops_count = ky_tops_data.duplicated(subset=['record_number',
                                           'pick_fm_name',
                                           'fm_top_depth_ft',
                                           'comments',
                                           'source'], keep='first').sum()

print('total duplicate entries:',duplicate_tops_count)


# drop the duplicates

ky_tops_data.drop_duplicates(subset=['record_number',
                                           'pick_fm_name',
                                           'fm_top_depth_ft',
                                           'comments',
                                           'source'], keep='first', inplace=True)


ky_group = ky_tops_data.groupby(['record_number', 'pick_fm_name']).mean().reset_index()



ky_merge = pd.merge(ky_tops_data, ky_group, how='inner', on=['record_number', 'pick_fm_name'])
ky_merge['pick_delta'] = abs(ky_merge.fm_top_depth_ft_x - ky_merge.fm_top_depth_ft_y)


ky_mask = ky_merge['pick_delta'] <= 20
ky_masked = ky_merge[ky_mask]


# load TN files (converted from .xls files to .csv files)
tn_ogtop_csv = pd.read_excel('C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\TN\\Tops_A.xls', header=0)

tn_ogtop = tn_ogtop_csv.drop(['SECTN',
                         'TOWNSHIP',
                         'RANGE',
                         'FEETEW',
                         'EW',
                         'FEETNS',
                         'NS',
                         'TSPEAST83',
                         'TSPNRTH83',
                         'LATDEG83',
                         'LATMIN83',
                         'LATSEC83',
                         'LONDEG83',
                         'LONMIN83',
                             'LONSEC83',
                             'LATDEG27',
                             'LATMIN27',
                             'LATSEC27',
                             'LONDEG27',
                             'LONMIN27',
                             'LONSEC27',
                             'PERMIT'
                              ], axis=1)

print (tn_ogtop)

tn_ogloc_csv = pd.read_csv(
    'C:\\Users\\Ken\Google Drive\\TN Structure\\OG_initial_well_files\\TN\\TNOG0617_A.csv',
    header=0)

tn_ogloc = tn_ogloc_csv.drop(['SECTN',
                         'TOWNSHIP',
                         'RANGE',
                         'FEETEW',
                         'EW',
                         'FEETNS',
                         'NS',
                         'QUAD',
                         'COUNTYNAME',
                         'FIELDTYPE',
                         'FIELDPOOL',
                         'ELEMEA',
                         'PERMDT',
                         'OPNAME',
                              'PROPTD',
                              'PROPFORM',
                              'LOGTD',
                              'TDSYST',
                              'TDFORM',
                              'TDFRMEST',
                              'CASEDESC',
                              'RESULT',
                              'GASTEST',
                              'IPGAS',
                              'OILTEST',
                              'IPOIL',
                              'PRESS01',
                              'PRESSTYP01',
                              'PRESS02',
                              'PRESTYP02',
                              'CHOKE',
                              'SPUDDT',
                              'TDDATE',
                              'LOGLOW',
                              'LOGHIGH',
                              'LOGTP01',
                              'LOGTP02',
                              'LOGTP03',
                              'LOGTP04',
                              'LOGTP05',
                              'LOGTP06',
                              'LOGTP07',
                              'LOGTP08',
                              'LOGTP09',
                              'LOGTP10',
                              'LOGTP11',
                              'LOGTP12',
                              'LOGTP13',
                              'LOGTP14',
                              'LOGTP15',
                              'PLUGDATE',
                              'SAMPRECDT',
                              'SAMPSTUDY',
                              'SAMPTYPE',
                              'SSDATE',
                              'SS1',
                              'SS2',
                              'SS3',
                              'SSLOW',
                              'SSHIGH',
                              'LATDEG83',
                              'LATMIN83',
                              'LATSEC83',
                              'LONDEG83',
                              'LONMIN83',
                              'LONSEC83',
                              'LATDEG27',
                              'LATMIN27',
                              'LATSEC27',
                              'LONDEG27',
                              'LONMIN27',
                              'LONSEC27',
                              'TSPEAST83',
                              'TSPNRTH83',
                              'WHRECDT',
                              'RVRBSN',
                              'RPTMON',
                              'RPTYEA'], axis=1)


tn_og_ksbpicks_csv = pd.read_csv(
    'C:\\Users\\Ken\Google Drive\\TN Structure\\OG_initial_well_files\\TN\\Tennessee_well_picks_KSB.csv',
    header=0)
tn_ogpicks = tn_og_ksbpicks_csv.drop(['SECTN',
                              'TOWNSHIP',
                              'RANGE',
                              'FEETEW',
                              'EW',
                              'FEETNS',
                              'NS',
                              'QUAD',
                              'COUNTYNAME',
                              'FIELDTYPE',
                              'FIELDPOOL',
                              'ELEMEA',
                                      'PERMDT',
                                      'OPNAME',
                                      'PROPTD',
                                      'PROPFORM',
                                      'LOGTD',
                                      'TDSYST',
                                      'TDFORM',
                                      'TDFRMEST',
                                      'CASEDESC',
                                      'RESULT',
                                      'GASTEST',
                                      'IPGAS',
                                      'OILTEST',
                                      'IPOIL',
                                      'PRESS01',
                                      'PRESSTYP01',
                                      'PRESS02',
                                      'PRESTYP02',
                                      'CHOKE',
                                      'SPUDDT',
                                      'TDDATE',
                                      'LOGLOW',
                                      'LOGHIGH',
                                      'LOGTP01',
                                      'LOGTP02',
                                      'LOGTP03',
                                      'LOGTP04',
                                      'LOGTP05',
                                      'LOGTP06',
                                      'LOGTP07',
                                      'LOGTP08',
                                      'LOGTP09',
                                      'LOGTP10',
                                      'LOGTP11',
                                      'LOGTP12',
                                      'LOGTP13',
                                      'LOGTP14',
                                      'LOGTP15',
                                      'PLUGDATE',
                                      'SAMPRECDT',
                                      'SAMPSTUDY',
                                      'SAMPTYPE',
                                      'SSDATE',
                                      'SS1',
                                      'SS2',
                                      'SS3',
                                      'SSLOW',
                                      'SSHIGH',
                                      'LATDEG83',
                                      'LATMIN83',
                                      'LATSEC83',
                                      'LONDEG83',
                                      'LONMIN83',
                                      'LONSEC83',
                                      'TSPEAST83',
                                      'TSPNRTH83',
                                      'WHRECDT',
                                      'RVRBSN',
                                      'RPTMON',
                                      'RPTYEA',
                                      'Shape *',
                                      'FID',
                                      'LATDEG27',
                                      'LATMIN27',
                                      'LATSEC27',
                                      'LONDEG27',
                                      'LONMIN27',
                                      'LONSEC27'], axis=1)




# CO2 project files are in three seperate databases: one for each formation.

#Carters CO2 data
tnco2ocdbf = Dbf5(
    'C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\TN\\CO2_STP_7_ELV_Oca_Revised4.dbf')
tnco2ocdf = tnco2ocdbf.to_dataframe()
tnco2oc = tnco2ocdf[['API', 'ELEVTN', 'Top_Oca', 'WELLNAME', 'TSPEAST27', 'TSPNRTH27', 'QUADNAME']]
tnco2oc['FRMATN'] = 'Carters Lime'
tnco2ocwells = tnco2oc[pd.notnull(tnco2oc['WELLNAME'])]
tnco2ocwells.rename(columns={"Top_Oca": "bestpick"
                             }, inplace=True)
#Knox CO2 data
tnco2okdbf = Dbf5(
    'C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\TN\\CO2_STP_7_ELV_OCk_Revised4.dbf')
tnco2okdf = tnco2okdbf.to_dataframe()
tnco2ok = tnco2okdf[['API', 'ELEVTN', 'Top_OCk', 'WELLNAME', 'TSPEAST27', 'TSPNRTH27', 'QUADNAME']]
tnco2ok['FRMATN'] = 'Knox-Ordovician'
tnco2okwells = tnco2ok[pd.notnull(tnco2ok['WELLNAME'])]
tnco2okwells.rename(columns={"Top_OCk": "bestpick"
                             }, inplace=True)
#Hermitage CO2 data
tnco2ohdbf = Dbf5(
    'C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\TN\\CO2_STP_7_ELV_Oh_Revised4.dbf')
tnco2ohdf = tnco2ohdbf.to_dataframe()
tnco2oh = tnco2ohdf[['API', 'ELEVTN', 'Top_Oh', 'WELLNAME', 'TSPEAST27', 'TSPNRTH27', 'QUADNAME']]
tnco2oh['FRMATN'] = 'Hermitage'
tnco2ohwells = tnco2oh[pd.notnull(tnco2oh['WELLNAME'])]
tnco2ohwells.rename(columns={"Top_Oh": "bestpick"
                             }, inplace=True)

#append CO2 project files
tnco2merge = tnco2ohwells.append([
    tnco2ocwells,
    tnco2okwells], ignore_index=True)

print (tnco2merge)




# asign best pick for TN top pick GEO<LOG<SAMP<WELL HISTORY
conditions = [
    (tn_ogtop['TOPGEO'] > 0),
    (tn_ogtop['TOPGEO'] == 0) & (tn_ogtop['TOPLOGS'] > 0),
    (tn_ogtop['TOPGEO'] == 0) & (tn_ogtop['TOPLOGS'] == 0) & (tn_ogtop['TOPSAMP'] > 0),
    (tn_ogtop['TOPGEO'] == 0) & (tn_ogtop['TOPLOGS'] == 0) & (tn_ogtop['TOPSAMP'] == 0) & (tn_ogtop['TOPWH'] > 0)]
choices = [tn_ogtop['TOPGEO'], tn_ogtop['TOPLOGS'], tn_ogtop['TOPSAMP'], tn_ogtop['TOPWH']]
tn_ogtop['bestpick'] = np.select(conditions, choices)



tnogwellsint = pd.merge(tn_ogloc, tn_ogtop, how='inner', on=['API', 'TSPNRTH27', 'TSPEAST27', 'ELEVTN'])
print (tnogwellsint)

tnogwellsint2 = tnogwellsint.append(tn_ogpicks, ignore_index=True)
print (tnogwellsint2)

tnogwells = tnogwellsint2.append(tnco2merge, ignore_index=True)

tnogwells.drop_duplicates(subset=['API', 'FRMATN', 'TSPEAST27', 'TSPNRTH27'], inplace=True)

print (tnogwells)



kymaskedgroup = ky_masked.drop_duplicates(subset=['record_number',
                                                 'pick_fm_name',
                                                 'fm_top_depth_ft_y'])
kymaskedgroup.rename(columns={"fm_top_depth_ft_y": "top_depth_avg"}, inplace=True)

kytopfinal = kymaskedgroup.drop(['datum_ft_y',
                                 'fm_bottom_depth_ft_y',
                                 'pick_stratcode_y',
                                 'secondary_lithology',
                                 'primary_lithology',
                                 'type'], axis=1)

kyogwells = pd.merge(ky_well_locations_columns, kytopfinal, how='inner', on=['record_number'])

print (kyogwells)



# kyogwells.rename(columns={"KGS_Recno": "record_number"
#                        },inplace=True)

kyogwellsdrop = kyogwells  #.drop(
    #['pick_delta', 'comments', 'date_added', 'source', 'interpreter_name', 'show', 'record_number', 'Org_Oper',
    #'Org_WellNo', 'interpreter_name','fm_bottom_depth_ft_x','datum_ft_x'], axis=1)

kyogwellsout = kyogwellsdrop.rename(columns={"Surf_Elev": "ELEVTN",
                                             "USGS_Quad": "QUADNAME",
                                             "top_depth_avg": "bestpick",
                                             "pick_fm_name": "FRMATN"})

kyogwellsout['Formation_Sea_Level'] = kyogwellsout['ELEVTN'] -  kyogwellsout['bestpick']

print (kyogwellsout)

kyogwellsout.to_csv('C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\kyogwells.csv')


tnogwellsout = tnogwells.drop(['TOPGEO','TOPLOGS','TOPSAMP','TOPWH','source','TD'], axis=1)
tnogwellsout['Formation_Sea_Level'] = tnogwellsout['ELEVTN'] -  tnogwellsout['bestpick']

print (tnogwellsout)
tnogwellsout.to_csv('C:\\Users\\Ken\\Google Drive\\TN Structure\\OG_initial_well_files\\intermediate files\\tnogwells.csv')