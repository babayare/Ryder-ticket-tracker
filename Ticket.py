import uuid
import random
from datetime import datetime

class Ticket:
    def __init__(self, first_name, last_name, employee_id, phone_number, department, issue, comment):
        self.ticket_number = str(uuid.uuid4())[:8]  # Generate a unique ticket number
        self.timestamp = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.phone_number = phone_number
        self.department = department
        self.issue = issue
        self.comment = comment
        self.assigned_to = None
        self.status = "Open"

    def assign_ticket(self, assigned_to, estimated_time):
        self.assigned_to = assigned_to
        self.estimated_time = estimated_time

    def view_ticket(self):
        print("\nTicket Number:", self.ticket_number)
        print("Timestamp:", self.timestamp)
        print("Name:", self.first_name, self.last_name)
        print("Employee ID:", self.employee_id)
        print("Phone Number:", self.phone_number)
        print("Department:", self.department)
        print("Issue:", self.issue)
        print("Comment:", self.comment)
        print("Status:", self.status)
        if self.assigned_to:
            print("Assigned To:", self.assigned_to)
            print("Estimated Time:", self.estimated_time)

class TicketTracker:
    def __init__(self):
        self.tickets = []

    def open_ticket(self, ticket):
        self.tickets.append(ticket)
        print("\nTicket opened successfully.")
        print("Ticket Number:", ticket.ticket_number)

    def view_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.view_ticket()
                return
        print("Ticket not found.")

if __name__ == "__main__":
    tracker = TicketTracker()

    while True:
        print("\nRyder Ticket Tracker")
        print("1. Open a Ticket")
        print("2. View a Ticket")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            employee_id = input("Enter your employee ID: ")
            phone_number = input("Enter your phone number: ")
            department = input("Enter your department: ")
            issue = input("Enter the issue you are facing: ")
            comment = input("Enter any additional comments: ")

            ticket = Ticket(first_name, last_name, employee_id, phone_number, department, issue, comment)
            tracker.open_ticket(ticket)

        elif choice == "2":
            ticket_number = input("Enter the ticket number: ")
            tracker.view_ticket(ticket_number)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
