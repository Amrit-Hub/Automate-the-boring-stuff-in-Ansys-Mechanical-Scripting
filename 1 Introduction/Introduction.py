lengthAxis = "X"
appliedForce = 50
meshsize = 20
#------------------------------
#Entry Points
geometry = ExtAPI.DataModel.Project.Model.Geometry
mesh = ExtAPI.DataModel.Project.Model.Mesh
analysis = ExtAPI.DataModel.Project.Model.Analyses[0]
solution = analysis.Solution
namedselection = ExtAPI.DataModel.Project.Model.NamedSelections
geoparts = ExtAPI.DataModel.GeoData.Assemblies[0].Parts

selinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mesh.ElementSize = Quantity(meshsize, 'mm')
def findsurface(axis, location):
    if axis == "X":
        axis = 0
    elif axis == "Y":
        axis = 1
    elif axis == "Z":
        axis = 2
    if location == "min":
        for part in geoparts:
            for body in part.Bodies:
                for face in body.Faces:
                    try:
                        if round(face.Centroid[axis], 5) < round(reqFace.Centroid[axis], 5):
                            reqFace = face
                    except:
                        reqFace = face
    elif location == "max":
        for part in geoparts:
            for body in part.Bodies:
                for face in body.Faces:
                    try:
                        if round(face.Centroid[axis], 5) > round(reqFace.Centroid[axis], 5):
                            reqFace = face
                    except:
                        reqFace = face
    selinfo.Ids = [reqFace.Id]
    return selinfo
NS_FixedSupport = ExtAPI.DataModel.Project.Model.AddNamedSelection()
NS_FixedSupport.Name = "NS_FixedSupport"
NS_FixedSupport.Location = findsurface(lengthAxis, 'min')
NS_Force = ExtAPI.DataModel.Project.Model.AddNamedSelection()
NS_Force.Name = "NS_Force"
NS_Force.Location = findsurface(lengthAxis, 'max')
fixedsupport = analysis.AddFixedSupport()
fixedsupport.Location = NS_FixedSupport
force = analysis.AddForce()
force.Location = NS_Force
force.Magnitude.Output.DiscreteValues= [Quantity(appliedForce, 'N')]
solution.AddEquivalentStress()
solution.AddTotalDeformation()
solution.Solve()
