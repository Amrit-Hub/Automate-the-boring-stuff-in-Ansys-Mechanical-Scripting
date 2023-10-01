# Analyses
ExtAPI.DataModel.Project.Model.Analyses
Model.Analyses
ExtAPI.DataModel.AnalysisList
Model.AddStaticStructuralAnalysis()
Model.AddModalAnalysis()
Model.Analyses[0].PhysicsType


# Analysis
ss1 = Model.Analyses[0]
Model.GetChildren(DataModelObjectCategory.Analysis, True)
Model.Analyses[0].Name
ss1.AnalysisSettings
ss1.AnalysisType
ss1.PhysicsType

ss1.Activate()
ss1.AddAcceleration()
ss1.AddBearingLoad()
ss1.AddBoltPretension()
ss1.AddCompressionOnlySupport()
ss1.AddDisplacement()
ss1.AddEarthGravity()
ss1.AddForce()
ss1.AddMoment()
ss1.AddPressure()
ss1.AddRemoteDisplacement()
ss1.Children
ss1.GetChildren
ss1.DataModelObjectCategory

ss1.GeoData
ss1.MeshData

ss1.WorkingDir
ss1.GetPath
ss1.GetType()

ss1.Duplicate
ss1.Delete

ss1.Solution

ss1.Solve
ss1.ClearGeneratedData

