import clr
clr.AddReference('System.Data') # Namespace
from System.Data import SqlClient, ConnectionState 

Server = 'TIGER03957\SQLSERVER2022'
Database = 'dbapsqlserver'
User = 'amritsql'
Password = 'Amrit-sql876'
connectionString = f'Server = {Server}; Database = {Database}; Integrated Security=True; Connect Timeout=10'
connection = SqlClient.SqlConnection(connectionString)

query = "select * from dbo.tablea"

cmd = connection.CreateCommand()
cmd.CommandText = query

try:
    connection.Open()
    reader = cmd.ExecuteReader()
    print(reader.HasRows)
    print(reader.FieldCount)
    while reader.Read():
        print(reader['id'])
        # print(reader[0])
    connection.Close()
except Exception as e:
    print(e)
    connection.Close()

cmd = SqlClient.SqlCommand()
cmd.Connection = connection
cmd.CommandText = query

try:
    connection.Open()
    reader = cmd.ExecuteReader()
    print(reader.HasRows)
    print(reader.FieldCount)
    while reader.Read():
        print(reader['id'])
        # print(reader[0])
    connection.Close()
except Exception as e:
    print(e)
    connection.Close()

cmd = SqlClient.SqlCommand(query, connection)

try:
    connection.Open()
    reader = cmd.ExecuteReader()
    print(reader.HasRows)
    print(reader.FieldCount)
    while reader.Read():
        print(reader['id'])
        # print(reader[0])
    connection.Close()
except Exception as e:
    print(e)
    connection.Close()