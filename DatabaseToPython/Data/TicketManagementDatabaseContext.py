import pymssql

class TicketManagementDatabaseContext:

    def __init__(self):
        connection = pymssql.connect(host=r'localhost\SQLEXPRESS',database='TicketManagementDatabase')

        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Planes')

        rows = cursor.fetchall()

        for row in rows:
            print(row)

TicketManagementDatabaseContext = TicketManagementDatabaseContext()
