from __future__ import print_function
import clr
clr.AddReference("System.Data")
from System.Data import OleDb, DataSet

pathXlsx = r"D:\AnsysScripting\003 Excel from IronPython\ansys.xlsx"
pathXls = r"D:\AnsysScripting\003 Excel from IronPython\ansys.xls"
# HDR indicates sheet has headers
# connectionString = 'Provider=Microsoft.ACE.OLEDB.12.0;Data Source="{}";Extended Properties="Excel 12.0;HDR=YES;";'.format(pathXlsx) # for 32bit xlsx
# connectionString = 'Provider=Microsoft.ACE.OLEDB.12.0;Data Source="{}";Extended Properties="Excel 12.0;HDR=YES;";'.format(pathXls) # for 32bit xls


connection = OleDb.OleDbConnection(connectionString)

# Select Query
query = "Select * From [Sheet1$]"
cmd = OleDb.OleDbCommand(query, connection)

try:
    connection.Open()
    # Create an OleDbDataAdapter to fill the data into a DataSet
    adapter = OleDb.OleDbDataAdapter(cmd)
    # Create a DataSet to hold the data
    excelDataset = DataSet()
    # Fill the DataSet with the data from the query
    adapter.Fill(excelDataset)
    connection.Close()
    table = excelDataset.Tables[0]
    print([table.TableName for table in excelDataset.Tables])
    for row in table.Rows:
        id = row["id"]
        name = row["name"]
        address = row["address"]
        print("ID: {}, Name: {}, Address: {}".format(id, name, address))
except Exception as e:
    print(e)
    connection.Close()

# -------------------------
# Insert Query
query = "INSERT INTO [Sheet1$] (id, name, address) VALUES (66, 'ee', 'eee')"
# # query = "INSERT INTO [Sheet1$] (id, name, address) VALUES (@id, @name, @address)"
# # query = "UPDATE [Sheet1$] SET name = 'ff', address = 'fff' WHERE [id] = 66"
command = OleDb.OleDbCommand(query, connection)
try:
    connection.Open()
    # command.Parameters.AddWithValue("@id", 55)
    # command.Parameters.AddWithValue("@name", "ee")
    # command.Parameters.AddWithValue("@address", "eee")
    command.ExecuteNonQuery()
    connection.Close()
    print("Query executed successfully.")
except Exception as e:
    print(e)
    connection.Close()
# -------------------------
