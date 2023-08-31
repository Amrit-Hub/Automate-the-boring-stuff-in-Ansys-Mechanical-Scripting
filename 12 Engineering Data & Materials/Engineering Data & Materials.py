GetAllSystems()
sys = GetSystem(Name = "SYS")
ed = sys.GetContainer(ComponentName = 'Engineering Data')
ed.GetMaterials()
ss = ed.GetMaterial(Name = 'Structural Steel')
ssden = ss.GetProperty(Name= "Density")
ssden.GetData(Variables = 'Density')
ssden.GetChartData()
ssden.GetData(Variables = 'Density')
ssden.GetData(Variables = ['Density', 'Temperature'])
ssden.SetData(Variables = 'Density', Values = '8050 [kg m^-3]')
ssden.SetData(Variables = 'Density', Values = ['8050 [kg m^-3]', '8090 [kg m^-3]' ])
ssden.SetData(Variables = ['Density', 'Temperature'], Values = ['8030 [kg m^-3]', '30 [C]'])
ssden.SetData(Variables = ['Density', 'Temperature'], Values = [['8030 [kg m^-3]', '9030 [kg m^-3]'], ['30 [C]', '50 [C]' ] ])


sselas = ss.GetProperty(Name = "Elasticity")
sselas.GetChartData()
sselas.GetData(Variables = "Bulk Modulus")
sselas.SetData(Variables = "Young's Modulus", Values = '200 [Pa]')

ss.Delete
ss.Duplicate
ss.DisplayName
ss.Description
ss.SetSuppression(Suppressed = True)
ss.IsSuppressed()


# Create
mymat = ed.CreateMaterial(Name = 'mymat')
myden = mymat.CreateProperty(Name = "Density")
myden.SetData(Variables = 'Density', Values = '8050 [kg m^-3]')

concrete = ed.ImportMaterial(Name="Concrete", Source="General_Materials.xml")

mymat = ed.CreateMaterial(Name = 'mymat')
myden = mymat.CreateProperty(Name = "Density")
myiscte = mymat.CreateProperty(Name="Coefficient of Thermal Expansion", Definition="Secant", Behavior="Isotropic")
myielas = mymat.CreateProperty(Name = "Elasticity", Behavior="Isotropic")

mymat.CreateProperty(Name = 'Isotropic Hardening', Definition = 'Bilinear')
mymat.CreateProperty(Name="Isotropic Hardening",Definition="Nonlinear",Behavior="Power Law")
.CreateProperty(
    Name="Polynomial",
    Definition="1st Order")

# Name="Uniaxial Plastic Strain Test Data",
# Name="Strain Hardening",
# Name="Norton",
# Name="S-N Curve",
# Name="S-N Curve",Definition="Linear",
# Name="S-N Curve",  Definition="Bilinear",
# Name="Gasket Model",
# Name="Shear Data - Viscoelastic",
# Name="Linear Fracture Criterion",



EngData.WriteMaterials(MaterialList=[mymat],FilePath='D:\YouTube\Ansys_ACT\19 Engineering Data & Materials II\test.xml', Format="MatML31",UnitSystem="BIN_STANDARD",ReplaceMaterial=True,OverwriteTarget=True)

ed.Import(Source="D:/AnsysScripting/xml material/Structural Steel.xml")

GetUnitSystemsNames()


mymat.Duplicate
mymat.Delete
mymat.SetSuppression(Suppressed = True)
mymat.IsSuppressed()