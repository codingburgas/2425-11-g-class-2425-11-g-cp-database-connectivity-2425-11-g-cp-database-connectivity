import pymssql
from Models.Plane import Plane
from Models.Customer import Customer
from Models.Ticket import Ticket


class TicketManagementDatabaseContext:

    @property
    def connection(self):
        return pymssql.connect(host=r'localhost\SQLEXPRESS',database='TicketManagementDatabase')

    plane_list = []
    customer_list = []
    ticket_list = []

    def __init__(self):
        self.read_from_planes()
        self.read_from_customers()
        self.read_from_tickets()

    def read_from_planes(self):
        cursor = self.connection.cursor()

        cursor.execute('SELECT * FROM [Planes]')

        rows = cursor.fetchall()

        for column in rows:
            plane = Plane()

            plane.id = column[0]
            plane.name = column[1]
            plane.make = column[2]
            plane.model = column[3]

            self.plane_list.insert(column[0], plane)

        cursor.close()

    def read_from_customers(self):
        cursor = self.connection.cursor()

        cursor.execute('SELECT * FROM [Customers]')

        rows = cursor.fetchall()

        for column in rows:
            customer = Customer()

            customer.id = column[0]
            customer.first_name = column[1]
            customer.last_name = column[2]
            customer.country = column[3]
            customer.age = column[4]

            self.customer_list.append(customer)

        cursor.close()

    def read_from_tickets(self):
        cursor = self.connection.cursor()

        cursor.execute('SELECT * FROM [Tickets]')

        rows = cursor.fetchall()

        for column in rows:
            ticket = Ticket()

            ticket.id = column[0]
            ticket.fromm = column[1]
            ticket.to = column[2]
            ticket.departure_time = column[3]
            ticket.arrival_time = column[4]
            ticket.seat_number = column[5]
            ticket.plane_id = self.plane_list[column[6]]
            ticket.customer_id = self.customer_list[column[7]]

            self.ticket_list.append(ticket)

        cursor.close()

context = TicketManagementDatabaseContext()

print('---------------------PLANES---------------------------')

for plane in context.plane_list:
    print(f'{plane.id} - {plane.name} - {plane.make} - {plane.model}')

print('---------------------CUSTOMERS--------------------------')
for customer in context.customer_list:
    print(f'{customer.id} - {customer.first_name} - {customer.last_name} - {customer.country} - {customer.age}')

print('---------------------TICKETS-----------------------------')
for ticket in context.ticket_list:
    print(f'{ticket.id} - {ticket.fromm} - {ticket.to} - {ticket.departure_time} - {ticket.arrival_time} - {ticket.seat_number} - {ticket.plane_id} - {ticket.customer_id}')