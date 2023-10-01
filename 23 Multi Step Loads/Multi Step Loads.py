acc = Model.Analyses[0].AddAcceleration()
acc.Magnitude # Constant, Tabular, Function
acc.Magnitude.GetType() # Ansys.ACT.Mechanical.Fields.Field
acc.Magnitude.Output
acc.Magnitude.Output.GetType() # Ansys.ACT.Mechanical.Fields.Variable
acc.Magnitude.Inputs
acc.Magnitude.Inputs # Ansys.ACT.Mechanical.Fields.InputVariableList

# Constant
# [Quantity('10 [mm sec^-1 sec^-1]')]
# [[Quantity('1 [sec]')]]
acc.Magnitude.Inputs[0].DiscreteValues
acc.Magnitude.Output.DiscreteValues
# Tabular
# [Quantity('0 [mm sec^-1 sec^-1]'),Quantity('10 [mm sec^-1 sec^-1]'),Quantity('20 [mm sec^-1 sec^-1]'),Quantity('30 [mm sec^-1 sec^-1]')]
# [Quantity('0 [sec]'),Quantity('1 [sec]'),Quantity('2 [sec]'),Quantity('3 [sec]')]


acc.Magnitude.Output.Formula = 10*time

acc.XComponent







 