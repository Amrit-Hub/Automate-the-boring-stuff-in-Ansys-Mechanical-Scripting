import sys
sys.path.append('D:\AnsysScripting\Sql conn')
from cred import cred
import clr
clr.AddReferenceToFileAndPath(r'D:\AnsysScripting\Sql conn\dll\Npgsql3.0.5\net45\Npgsql.dll')

import Npgsql
Server = cred['personal']['postgres']['server']
Database = cred['personal']['postgres']['database']
User = cred['personal']['postgres']['username']
Password = cred['personal']['postgres']['password']
connectionString = 'server = {}; database = {}; user id = {}; password = {};'.format(Server, Database, User, Password)
print(connectionString)
connection = Npgsql.NpgsqlConnection(connectionString)

query = "select * from myschema.newtable"
cmd = Npgsql.NpgsqlCommand(query, connection)
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

# nonQuery = "insert into myschema.newtable (id) values (5)"
# # nonQuery = "delete from dbo.tablea where id = 5"
# cmd = Npgsql.NpgsqlCommand(nonQuery, connection)

# try:
#     connection.Open()
#     cmd.ExecuteNonQuery()
#     connection.Close()
# except Exception as e:
#     print(e)
#     connection.Close()


