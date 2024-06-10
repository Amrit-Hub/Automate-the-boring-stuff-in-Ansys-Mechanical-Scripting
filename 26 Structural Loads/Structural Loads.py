a = Model.Analyses[0]
a.Activate()
face = ExtAPI.SelectionManager.CurrentSelection
f = a.AddForce()
f.Location = face


f.DefineBy =  LoadDefineBy.Components
f.XComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
f.XComponent.Output.DiscreteValues = [Quantity('0 [N]'),Quantity('10 [N]'),Quantity('20 [N]')]

m = a.AddMoment()
m.Location = face
m.Magnitude.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
m.Magnitude.Output.DiscreteValues = [Quantity('0 [N mm]'),Quantity('10 [N mm]'),Quantity('20 [N mm]')]

p = a.AddPressure()
p.Location = face
p.Magnitude.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
p.Magnitude.Output.DiscreteValues = [Quantity('0 [Pa]'),Quantity('10 [Pa]'),Quantity('20 [Pa]')]

b = a.AddBearingLoad()
