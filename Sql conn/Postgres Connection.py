import clr
# clr.AddReference('System.Data')
clr.AddReferenceToFileAndPath('dll/Mono.Security.dll')
clr.AddReferenceToFileAndPath('dll/Npgsql45.dll') # Namespace
import Npgsql as pgsql
Server = 'localhost'
Database = 'postgres'
User = 'amritsql'
Password = 'Amrit-sql876'
connectionString = 'server = {}; database = {}; user id = {}; password = {};'.format(Server, Database, User, Password)
connection = pgsql.NpgsqlConnection(connectionString)
connection.Open()

query = "select * from myschema.newtable"

cmd = NpgsqlCommand(query, connection)


