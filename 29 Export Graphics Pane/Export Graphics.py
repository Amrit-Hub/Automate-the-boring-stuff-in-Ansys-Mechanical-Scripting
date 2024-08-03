analysis = Model.Analyses[0]
solution = analysis.Solution
result = solution.Children[1]

Tree.Activate(result)

ExtAPI.Graphics.ExportImage(r"D:\test\sample2.jpg")

# With settings
imgSetting = Ansys.Mechanical.Graphics.GraphicsImageExportSettings()
imgSetting.Background = GraphicsBackgroundType.White
imgSetting.Resolution = GraphicsResolutionType.HighResolution
# imgSetting.FontMagnification = 1.3  # Doesn't work.
imgSetting.Width = 1200
imgSetting.Height = 1000
imgSetting.CurrentGraphicsDisplay = False
 
ExtAPI.Graphics.ExportImage(r"D:\test\sample2.jpg", GraphicsImageExportFormat.JPG, imgSetting)

ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doImageCaptureForGraphics(1);')


# ********* USING SCREEN CAPTURE *********

graphics = ExtAPI.UserInterface.GetPane(MechanicalPanelEnum.Graphics)
 
width = graphics.ControlUnknown.Width # Can be user defined
height = graphics.ControlUnknown.Height # Can be user defined
loc_x = graphics.CommandContainer.WindowRect.Left # X co-ordinates
loc_y = graphics.CommandContainer.WindowRect.Top # Y co-ordinates
print(loc_x,loc_y,width,height)
 
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

ImgPath = r"D:\test\graphics.jpg"
ScreenCapture(ImgPath,loc_x,loc_y,width,height)