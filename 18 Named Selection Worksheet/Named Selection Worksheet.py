ns=Model.AddNamedSelection() 
ns.ScopingMethod=GeometryDefineByType.Worksheet
ns.Name="Test"
CRC=ns.GenerationCriteria

CRC.Add(None)

CRC[0]=Ansys.ACT.Automation.Mechanical.NamedSelectionCriterion()
CRC[0].Action=SelectionActionType.Add
CRC[0].EntityType=SelectionType.GeoEdge
CRC[0].Criterion=SelectionCriterionType.NamedSelection
CRC[0].Operator=SelectionOperatorType.Equal

ns.ScopingMethod=GeometryDefineByType.Worksheet

ns.Location = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.WorksheetSpecific)

wsselinfo = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.WorksheetSpecific)