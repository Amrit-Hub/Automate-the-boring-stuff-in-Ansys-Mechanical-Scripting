ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doTimelineWindow();')

jstring = """
if (!DS.Script.isTimelineWindowActive())
    DS.Script.doTimelineWindow();
"""
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand(jstring)

# file:///C:/Program%20Files/ANSYS%20Inc/v232/aisol/DesignSpace/DSPages/html/DSSolutionOutputGraph.htm

# NOT ResultChart, ProbeResult, SolutionSettings, SolutionInfoTool, Convergence

jstring = """
// stepControl = timelinePane.LoadControl(GenWBProgId("WBGraphUtility.WBGraph"), wb);
var stepControl = DS.Script.stepControl
var fName = "D:/test/text1234.jpg";
stepControl.WriteJpgFile(fName, 1200, 1000, true);
// WritePngFile
// WriteBmpFile
"""
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand(jstring)

# ExtAPI.Graphics.ExportViewportChart(0, r"D:\test\222.bmp",500,600, GraphicsImageExportFormat.PNG)
