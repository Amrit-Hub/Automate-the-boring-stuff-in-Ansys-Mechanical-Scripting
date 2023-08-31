"C:\Program Files\ANSYS Inc\v212\Addins\ACT\libraries\Mechanical\wbjn.py"


GetAllSystems()[0].DisplayText = 'Hello'
modal = GetTemplate(TemplateName = "Modal", Solver = "ANSYS").CreateSystem()
	

query = """
sys = GetSystem(Name = "SYS")
ed = sys.GetContainer(ComponentName = 'Engineering Data')
ss = ed.GetMaterial(Name = 'Structural Steel')
ssden = ss.GetProperty(Name= "Density")
den = ssden.GetData(Variables = 'Density').ToString()
returnValue(den)
"""
wbjn.ExecuteCommand(ExtAPI, query)

query = """returnValue(str(GetAllSystems()))"""
wbjn.ExecuteCommand(ExtAPI, query)


from System.Threading import ApartmentState, Thread, ThreadStart
-------------------------------------------
def executeQuery():
	sys = GetSystem(Name = "SYS")
	ed = sys.GetContainer(ComponentName = 'Engineering Data')
	ss = ed.GetMaterial(Name = 'Structural Steel')
	ssden = ss.GetProperty(Name= "Density")
	ssden.SetData(Variables = 'Density', Values = '800 [kg m^-3]')
thread = Thread(ThreadStart(executeQuery))
thread.Start()	
--------------------------------------
def fn_main(query):
	def fn_execute():
		import wbjn
		wbjn.ExecuteCommand(ExtAPI,query)
	thread = Thread(ThreadStart(fn_execute))
	thread.Start()

query = """
sys = GetSystem(Name = "SYS")
ed = sys.GetContainer(ComponentName = 'Engineering Data')
ss = ed.GetMaterial(Name = 'Structural Steel')
ssden = ss.GetProperty(Name= "Density")
ssden.SetData(Variables = 'Density', Values = '88 [kg m^-3]')"""
fn_main(query)
-------------------------------------------
def executeQuery():
	query = """
	sys = GetSystem(Name = "SYS")
	ed = sys.GetContainer(ComponentName = 'Engineering Data')
	ss = ed.GetMaterial(Name = 'Structural Steel')
	ssden = ss.GetProperty(Name= "Density")
	ssden.SetData(Variables = 'Density', Values = '888 [kg m^-3]')"""
	import wbjn
	wbjn.ExecuteCommand(ExtAPI,query)
thread = Thread(ThreadStart(executeQuery))
thread.Start()


