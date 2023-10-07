import sys
sys.path.append("path\to\cred.py")  # import username password credentials
from cred import cred  # import username password credentials
import clr
clr.AddReferenceToFileAndPath(r'path\to\MySql.Data.dll') # Namespace
from MySql.Data import MySqlClient

Server = cred['personal']['mysql']['server']
Database = cred['personal']['mysql']['database']
User = cred['personal']['mysql']['username']
Password = cred['personal']['mysql']['password']
connectionString = 'server={}; database={}; uid={}; pwd={}'.format(Server, Database, User, Password)
connection = MySqlClient.MySqlConnection(connectionString)

query = "select * from ansysdb.testtable"

# METHOD 1
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

# METHOD 2
cmd = MySqlClient.MySqlCommand()
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

# METHOD 3
cmd = MySqlClient.MySqlCommand(query, connection)

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

nonQuery = "insert into ansysdb.testtable (id, name) values (55, 'ee')"
# nonQuery = "delete from dbo.tablea where id = 55"
cmd = MySqlClient.MySqlCommand(nonQuery, connection)

try:
    connection.Open()
    cmd.ExecuteNonQuery()
    connection.Close()
except Exception as e:
    print(e)
    connection.Close()
