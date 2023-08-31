import sys
sys.path.append("D:/_Common")  # import username password credentials
from cred import cred  # import username password credentials
import clr
clr.AddReference('System.Data') # Namespace
from System.Data import SqlClient, ConnectionState 

Server = cred['personal']['sqlserver']['server']
Database = cred['personal']['sqlserver']['database']
User = cred['personal']['sqlserver']['username']
Password = cred['personal']['sqlserver']['password']

connectionString = 'Server = {}; Database = {}; Integrated Security=True; User = {}; Password = {}; Connect Timeout=10'.format(Server, Database, User, Password)
connection = SqlClient.SqlConnection(connectionString)

query = "select * from dbo.testTable"

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

nonQuery = "insert into dbo.tablea (id) values (5)"
nonQuery = "delete from dbo.tablea where id = 5"
cmd = SqlClient.SqlCommand(nonQuery, connection)

try:
    connection.Open()
    cmd.ExecuteNonQuery()
    connection.Close()
except Exception as e:
    print(e)
    connection.Close()