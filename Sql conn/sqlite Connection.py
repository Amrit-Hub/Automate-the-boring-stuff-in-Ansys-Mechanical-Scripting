import clr
clr.AddReferenceToFileAndPath(r'D:\AnsysScripting\Sql conn\dll\sqlite-netFx40-binary-bundle-x64-2010-1.0.117.0\System.Data.SQLite.dll')
import System.Data.SQLite as sqlite

connection = sqlite.SQLiteConnection(r'DataSource=X:\path\to\Chinook_Sqlite.sqlite;')
query = "select * from myschema.newtable"
cmd = sqlite.SQLiteCommand(query, connection)

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