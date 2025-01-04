ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.toggleWorksheetVisibility();')

jstring = """
if (!DS.Script.isWorksheetWindowActive())
    DS.Script.toggleWorksheetVisibility();
"""
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand(jstring)




# file:///C:/Program%20Files/ANSYS%20Inc/v232/aisol/DesignSpace/DSPages/html/DSSolutionOutputGraph.htm

# ResultChart, ProbeResult, SolutionSettings, SolutionInfoTool, Convergence

jstring = """
var g_WorksheetTabBrowser = DS.Script.g_WorksheetTabBrowser
var fName = "D:/test/text1234.jpg";
g_WorksheetTabBrowser.Document.Script.WriteGraphToFile(1, fName);
// 0 png
// 1 jpg
// 3 bmp
"""
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand(jstring)

# ContactGroup, PrototypeGroup, Environment, ProbeResult, ContactDataTable, ResultChart, ResultTable, CoordinateSystemGroup, ImportedCoordinateSystemCollection, ImportedElementOrientationCollection, ImportedPointMassCollection, ImportedSpringConnectorCollection, ImportedPliesCollection, ImportedRigidRemoteConnectorCollection, ImportedFlexibleRemoteConnectorCollection, ImportedIndependentPointManager, ImportedConstraintEquationCollection, ImportedShellThicknessCollection, ImportedPremeshedBoltPretensionCollection, ImportedMaterialAssignmentCollection, ImportedCrossSectionAlignmentCollection, ImportedContactCollection, ImportedBoltPretensionCollection, ImportedLoadCollection, ImportedStressCollection, ThermalCondition, AnalysisSettings, ContactTool, AnswerSet, Convergence, MeshControlGroup, ConstraintEquation, BoltTool, ConnectionGroup, NodeMove, CompositeFailureTool, CompositeFailureCriteria, ComponentGroup

ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doExportWorksheetToTextFile("D:/test/WorsheetResult.txt");')
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doExportWorksheetToTextFile("D:/test/WorsheetResult.xls");')

# ********* USING SCREEN CAPTURE *********
WorksheetPane = ExtAPI.UserInterface.GetPane(MechanicalPanelEnum.Worksheet)
 
width = WorksheetPane.Control.Width # Can be user defined
height = WorksheetPane.Control.Height # Can be user defined
loc_x = WorksheetPane.CommandContainer.WindowRect.Left # X co-ordinates
loc_y = WorksheetPane.CommandContainer.WindowRect.Top # Y co-ordinates

# Screen Capture
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
 
from System.Drawing import Bitmap,Graphics,Point,Size

def ScreenCapture(ImgPath,location_X,location_Y,width,height):
    bmp = Bitmap((width), (height))
    g = Graphics.FromImage(bmp)
    g.CopyFromScreen(location_X,location_Y ,0,0, Size((width),(height))) 
    bmp.Save(ImgPath)
    g.Dispose()

ImgPath = r"D:\test\sample.jpg"
ScreenCapture(ImgPath,loc_x,loc_y,width,height)