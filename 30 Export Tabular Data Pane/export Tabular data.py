# Any Tabular Data

table=ExtAPI.UserInterface.GetPane(MechanicalPanelEnum.TabularData)
control = table.ControlUnknown

num_columns = control.ColumnsCount+1
num_rows = control.RowsCount+1
# print(num_rows-1, num_columns-1)
lines = ""
for row in range(1, num_rows):
    line = []
    for col in range(2, num_columns):
        cell = control.cell(row, col).Text
        if cell:
            line.append(cell)
    lines = lines + ",".join(line) + "\n"
print(lines)
with open(r"D:\test\text.csv", 'w') as f:
    f.write(lines)

# FREQ1 = TOTAL_DEFORMATION_1.TabularData["Frequency"][0]


ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doTabularData_DisplayContextMenu("ID_ExportTabularData");')

ExtAPI.Application.ScriptByName("jscript").ExecuteCommand('DS.Script.doTabularDataWindow();')

jstring = """
if (!DS.Script.isTabularDataWindowActive())
    DS.Script.doTabularDataWindow();
"""
ExtAPI.Application.ScriptByName("jscript").ExecuteCommand(jstring)