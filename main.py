#from openpyxl import load_workbook
import pymysql
'''
'db_user_name' => 'suite_user',
'db_password' => 'lollipop300777',
'db_name' => 'suitecrm',
'''
# Open database connection
db = pymysql.connect("localhost","suite_user","lollipop300777","suitecrm" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
result = cursor.execute("SELECT * from project_task limit 100")
print(result)
# disconnect from server
db.close()
