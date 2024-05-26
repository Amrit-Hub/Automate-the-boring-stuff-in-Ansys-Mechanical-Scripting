a0 = Model.Analyses[0]
acc = a0.AddAcceleration()
acc.DefineBy
acc.DefineBy = LoadDefineBy.Components
acc.DefineBy = LoadDefineBy.Vector
acc.Magnitude.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
acc.Magnitude.Output.DiscreteValues = [Quantity('0 [mm sec^-1 sec^-1]'),Quantity('10 [mm sec^-1 sec^-1]'),Quantity('20 [mm sec^-1 sec^-1]')]

# vector = Ansys.ACT.Math.Vector3D(0,0,1)
vector = Vector3D(0,0,1)
acc.Direction = vector
acc.DefineBy = LoadDefineBy.Components
acc.XComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
acc.XComponent.Output.DiscreteValues = [Quantity('0 [mm sec^-1 sec^-1]'),Quantity('10 [mm sec^-1 sec^-1]'),Quantity('20 [mm sec^-1 sec^-1]')]
acc.YComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
acc.YComponent.Output.DiscreteValues = [Quantity('0 [mm sec^-1 sec^-1]'),Quantity('10 [mm sec^-1 sec^-1]'),Quantity('20 [mm sec^-1 sec^-1]')]
acc.ZComponent.Inputs[0].DiscreteValues = [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]')]
acc.ZComponent.Output.DiscreteValues = [Quantity('0 [mm sec^-1 sec^-1]'),Quantity('10 [mm sec^-1 sec^-1]'),Quantity('20 [mm sec^-1 sec^-1]')]

aeg = a0.AddEarthGravity()
aeg.Direction = GravityOrientationType.NegativeYAxis
