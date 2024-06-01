face = ExtAPI.SelectionManager.CurrentSelection

a0 = Model.Analyses[0]
fs = a0.AddFixedSupport()
fs.Location = face

ds = a0.Adddslacement()
ds.Location = face

ds.DefineBy = LoadDefineBy.Components
ds.XComponent.Inputs
ds.XComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
ds.XComponent.Output.DiscreteValues = [Quantity('0 [mm]'),Quantity('10 [mm]'),Quantity('20 [mm]')]
ds.YComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
ds.YComponent.Output.DiscreteValues = [Quantity('0 [mm]'),Quantity('10 [mm]'),Quantity('20 [mm]')]
ds.ZComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
ds.ZComponent.Output.DiscreteValues = [Quantity('0 [mm]'),Quantity('10 [mm]'),Quantity('20 [mm]')]

ds.XComponent.Output.DiscreteValues = None

rd= a0.AddRemotedslacement()
rd.Location = face
rd.YCoordinate = Quantity('-10 [mm]')
rd.YComponent.Output.DiscreteValues = [Quantity('10 [mm]')]
rd.RotationY.Output.DiscreteValues = [Quantity('10 [deg]')]