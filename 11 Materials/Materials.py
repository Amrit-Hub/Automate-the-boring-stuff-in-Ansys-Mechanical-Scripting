# material objects

# body object material
b1 = Model.Geometry.GetChildren(DataModelObjectCategory.Body, True)[0]
b1.Material = "Aluminum Alloy"



# body geodata material
bg1 = b1.GetGeoBody()
b1mat = bg1.Material
materials.GetMaterialPropertyByName(b1mat, "Elasticity")


# materials module
"C:\Program Files\ANSYS Inc\v212\Addins\ACT\libraries\Mechanical\materials.py"