lengthAxis = "X"
appliedForce = 50
meshsize = 20
# MECH
# Entry Points
geometry = Model.Geometry
mesh = Model.Mesh
analysis = Model.Analyses[0]
solution = analysis.Solution
namedselection = Model.NamedSelections
geoparts = ExtAPI.DataModel.GeoData.Assemblies[0].Parts

mesh.ElementSize = Quantity(meshsize, 'mm')

def returnFaces(geoparts):
    faceList = []
    for part in geoparts:
        for body in part.Bodies:
            for face in body.Faces:
                faceList.append(face)
    return faceList

def findsurface(axis, location):
    selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    if axis == "X":
        axis = 0
    elif axis == "Y":
        axis = 1
    elif axis == "Z":
        axis = 2
    faceList = returnFaces(geoparts)
    faceCentroidAxisList = [round(face.Centroid[axis], 3) for face in faceList]
    if location == "min":
        reqFace = faceList[faceCentroidAxisList.index(min(faceCentroidAxisList))]
    elif location == "max":
        reqFace = faceList[faceCentroidAxisList.index(max(faceCentroidAxisList))]
    selinfo.Ids = [reqFace.Id]
    return selinfo
NS_FixedSupport = Model.AddNamedSelection()
NS_FixedSupport.Name = "NS_FixedSupport"
NS_FixedSupport.Location = findsurface(lengthAxis, 'min')
NS_Force = Model.AddNamedSelection()
NS_Force.Name = "NS_Force"
NS_Force.Location = findsurface(lengthAxis, 'max')
fixedsupport = analysis.AddFixedSupport()
fixedsupport.Location = NS_FixedSupport
force = analysis.AddForce()
force.Location = NS_Force
force.Magnitude.Output.DiscreteValues= [Quantity(appliedForce, 'N')]
eqvStress = solution.AddEquivalentStress()
totalDef = solution.AddTotalDeformation()
solution.Solve()