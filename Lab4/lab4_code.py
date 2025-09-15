import arcpy

arcpy.env.workspace = r'C:\Users\Natalie\Desktop\Class\pitts-online-GEOG676-fall2025\Lab4\codes.env'
folder_path = r'C:\Users\Natalie\Desktop\Class\pitts-online-GEOG676-fall2025\Lab4'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'C:\Users\Natalie\Desktop\Class\TAMU-MGSc-Online-GEOG676-GIS-PROGRAMMING-main\data\homework\04\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

campus = r'C:\Users\Natalie\Desktop\Class\TAMU-MGSc-Online-GEOG676-GIS-PROGRAMMING-main\data\homework\04\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + 'Garage_Points_buffered', 150)

arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\\Garage_Building_Intersection.dbf', 'C:\\Users\\Natalie\\Desktop\\Class\\pitts-online-GEOG676-fall2025\\Lab4', 'nearbybuildings.csv')