solution = Model.Analyses[0].Solution
soli = solution.SolutionInformation

result = solution.Children[1]
img = result.AddImage()
# ExtAPI.Graphics.ExportImage(r"D:\test\image.jpg") # Width and Height to Mechanical graphics size
result.ExportToTextFile(r'D:\test\text.txt')
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doExportToTextFile("D:/test/WorsheetResult.txt");')
result.PlotData
result.PlotData["Values"]
result.PlotData["Node"]
