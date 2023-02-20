import clr
clr.AddReferenceToFileAndPath('MySql.Data.dll') # Namespace
from MySql.Data import MySqlClient

Server = 'tiger03957'
Database = 'world'
User = 'amritsql'
Password = 'Amrit-sql876'
connectionString = 'server={}; database={}; uid={}; pwd={}'.format(Server, Database, User, Password)
connection = MySqlClient.MySqlConnection(connectionString)

query = "select * from world.city where id = 1"

# cmd = connection.CreateCommand()
# cmd.CommandText = query

# try:
#     connection.Open()
#     reader = cmd.ExecuteReader()
#     print(reader.HasRows)
#     print(reader.FieldCount)
#     while reader.Read():
#         print(reader['id'])
#         # print(reader[0])
#     connection.Close()
# except Exception as e:
#     print(e)
#     connection.Close()

# cmd = MySqlClient.MySqlCommand()
# cmd.Connection = connection
# cmd.CommandText = query

# try:
#     connection.Open()
#     reader = cmd.ExecuteReader()
#     print(reader.HasRows)
#     print(reader.FieldCount)
#     while reader.Read():
#         print(reader['id'])
#         # print(reader[0])
#     connection.Close()
# except Exception as e:
#     print(e)
#     connection.Close()

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

# nonQuery = "insert into dbo.tablea (id) values (5)"
# # nonQuery = "delete from dbo.tablea where id = 5"
# cmd = MySqlClient.MySqlCommand(nonQuery, connection)

# try:
#     connection.Open()
#     cmd.ExecuteNonQuery()
#     connection.Close()
# except Exception as e:
#     print(e)
#     connection.Close()
