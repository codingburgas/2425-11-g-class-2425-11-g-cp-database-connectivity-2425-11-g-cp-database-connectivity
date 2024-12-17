from DAL.Data.TicketManagementDatabaseContext import TicketManagementDatabaseContext
from DAL.Models.Plane import Plane

# CRUD IMPLEMENTATION
class PlaneRepository:

    @property
    def context(self):
        return TicketManagementDatabaseContext()

    # READ METHOD
    def read_from_planes(self):
        cursor = self.context.connection.cursor()

        cursor.execute('SELECT * FROM [Planes]')

        rows = cursor.fetchall()

        for column in rows:
            plane = Plane()

            plane.id = column[0]
            plane.name = column[1]
            plane.make = column[2]
            plane.model = column[3]

            self.context.plane_list.insert(column[0], plane)

        cursor.close()

    # CREATE METHOD
    def write_to_planes(self, plane = Plane()):
        cursor = self.context.connection.cursor()

        query_string = ('INSERT INTO [Planes] VALUES(%id, %name, %make, %model)')

        data_to_write = [
            {plane.id},
            {plane.name},
            {plane.make},
            {plane.model}
        ]

        cursor.executemany(query_string, data_to_write)

        self.context.connection.commit()

        cursor.close()

repository = PlaneRepository()

plane = Plane()
plane.id = 668
plane.name = 'Something'
plane.make = 'Something'
plane.model = 'Something'

repository.write_to_planes(plane)

repository.read_from_planes()

print('---------------------PLANES---------------------------')

for plane in repository.context.plane_list:
    print(f'{plane.id} - {plane.name} - {plane.make} - {plane.model}')