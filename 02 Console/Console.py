import sys
sys.path
GetAllSystems()
statictemp = GetTemplate(TemplateName = "Static Structural")
statictemp = GetTemplate(TemplateName = "Static Structural", Solver = "Ansys")
statictemp = GetTemplate(TemplateName = "Static Structural", Solver = "ANSYS")
staticsys = statictemp.CreateSystem()

# CREATE MODAL
modaltemp = GetTemplate(TemplateName = "Modal", Solver = "ANSYS")
modalsys = modaltemp.CreateSystem()
modalsys.DisplayText = "My Modal"
modalsys.Name #readonly, cant assign

# ACCESS SYSTEM BY SYS NAME
sys = GetSystem(Name = "SYS")
sys.DisplayText = "modeeeel"
sys.Name
sys = GetSystem(DisplayText = "displaye name") #not possible
sys.ComponentName

# ACCESS COMPOENENT BY COMPONENET NAME
model1 = static.GetComponent(Name = "Model")
model2 = static.GetContainer(ComponentName = "Model")
model1.Name
model2.Name
model1.Type
model2.Type

dir(model1) #what you see in project component
['Clean', 'Container', 'DeleteShare', 'DeleteTransfer', 'DirectoryName', 'DisplayText', 'GetContainer', 'GetEntityProperties', 'GetEntityProperty', 'GetExpression', 'GetProperties', 'GetProperty', 'HasAssociatedParameter', 'Name', 'Notes', 'Refresh', 'RemoveFromSystem', 'ReplaceWithShare', 'Reset', 'SetEntityProperties', 'SetEntityProperty', 'SimulationSetEntityProperty', 'ToString', 'TransferData', 'TransferSpecificData', 'Type', 'Update', 'UpdateConditionParameter', 'UpdateUpstreamComponents', 'UserId']

dir(model2) # inside container like mechanical
['Edit', 'Exit', 'Export', 'ExportASMJournal', 'ExportGeometry', 'ExportMesh', 'GetACPImportOptions', 'GetAllParameters', 'GetFiles', 'GetMechanicalMesh', 'GetMechanicalMeshFile', 'GetMechanicalModel', 'GetMechanicalSystemType', 'GetMeshProperties', 'GetModelComponentProperties', 'GetSimulationImportOptions', 'Name', 'SendCommand', 'ToString', 'Type']

model2.Refresh() #refresh is important
model2.Edit()

model1.Reset()
command1 = "ExtAPI.DataModel.Project.Model.Analyses[0].AddForce()"
model2.SendCommand(Command = command1, Language = "Python")

statictemp = GetTemplate(TemplateName = "Static Structural", Solver = "ANSYS")
staticsys = statictemp.CreateSystem()
model2 = staticsys.GetContainer(ComponentName = "Model")
model2.Refresh()
model2.Edit() #Optional
model2.SendCommand(Command = command1, Language = "Python")

# WIZARD

command = """statictemp = GetTemplate(TemplateName = "Static Structural", Solver = "ANSYS")
staticsys = statictemp.CreateSystem()"""
ExtAPI.ExecuteCommand(command)
ExtAPI.DataModel.CurrentUnitFromQuantityName("Length")
