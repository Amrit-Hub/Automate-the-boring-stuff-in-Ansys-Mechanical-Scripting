geom = Model.Geometry
geodata = ExtAPI.DataModel.GeoData
geodata.Assemblies[0].AllParts[0].Name

# Getting faces using GeoData
geodata = ExtAPI.DataModel.GeoData
geoparts = geodata.Assemblies[0].AllParts
BoltFaces = []
NutFaces = []
for part in geoparts:
    if part.Name in ("Bolt", "Nut"):
        for body in part.Bodies:
            for face in body.Faces:
                if face.SurfaceType.ToString() == "GeoSurfaceCylinder" and round(face.Area, 5) == 0.00276:
                    BoltFaces.append(face.Id)
                elif face.SurfaceType.ToString() == "GeoSurfaceCylinder" and round(face.Area, 5) == 0.00075:
                    NutFaces.append(face.Id)
print(BoltFaces)
print(NutFaces)

# Getting faces using bodies
import time
geom = Model.Geometry
parts = geom.Children
selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
BoltFaces = []
NutFaces = []
for part in parts:
    if part.Name in ("Bolt", "Nut"):
        for body in part.Children:
            geobody = body.GetGeoBody()
            for face in geobody.Faces:
                if face.SurfaceType.ToString() == "GeoSurfaceCylinder" and round(face.Area, 5) == 0.00276:
                    BoltFaces.append(face.Id)
                elif face.SurfaceType.ToString() == "GeoSurfaceCylinder" and round(face.Area, 5) == 0.00075:
                    NutFaces.append(face.Id)
print(BoltFaces)
selinfo.Ids = BoltFaces
ExtAPI.SelectionManager.NewSelection(selinfo)
print(NutFaces)
time.sleep(2)
selinfo.Ids = NutFaces
ExtAPI.SelectionManager.NewSelection(selinfo)

# Create named selection
def createNamedSelection(locationList, name):
    selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    selinfo.Ids = locationList
    ns = Model.AddNamedSelection()
    ns.Name = name
    ns.Location = selinfo

createNamedSelection(BoltFaces, "ns_BoltFaces")
createNamedSelection(NutFaces, "ns_NutFaces")

# Create bolt pretension
pretensionFaces = ExtAPI.DataModel.GetObjectsByName("ns_BoltFaces")[0]
selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
for face in pretensionFaces.Location:
    selinfo.Ids = [face]
    boltPretension = Model.Analyses[0].AddBoltPretension()
    boltPretension.Location = selinfo

# Create bolt pretension using bodies
geom = Model.Geometry
a0 = Model.Analyses[0]
selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
parts = geom.Children
BoltBodyList = []
for part in parts:
    if part.Name == "Bolt":
        BoltBodyList.append(part.Children[0].GetGeoBody().Id)
print(BoltBodyList)
selinfo.Ids = BoltBodyList
ExtAPI.SelectionManager.NewSelection(selinfo)
for boltBody in BoltBodyList:
    cs = Model.CoordinateSystems.AddCoordinateSystem()
    cs.Name = "bolt_" + cs.Name + str(boltBody)
    selinfo.Ids = [boltBody]
    cs.OriginLocation = selinfo
    boltPretension = a0.AddBoltPretension()
    boltPretension.Location = selinfo
    boltPretension.CoordinateSystem = cs
    
# Load and Lock
bpt = ExtAPI.DataModel.GetObjectsByName("Bolt Pretension")[0]
bpt.GetDefineBy(1)
bpt.SetDefineBy(1, BoltLoadDefineBy.Load)
bpt.SetDefineBy(2, BoltLoadDefineBy.Lock)

bpt.Preload
bpt.Preload.Inputs[0].DiscreteValues
bpt.Preload.Output.DiscreteValues = [Quantity('10 [N]'),Quantity('0 [N]')]
bpt.Preadjustment.Output.DiscreteValues