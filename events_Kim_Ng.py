# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: Kim Ng (Lion)
# Student ID : 1167513 
# ================================================================
 
from datetime import datetime,timedelta     # datetime module is required for working with dates

# Make the variables and function in set_data.py available in this code (without needing 'set_data.' prefix)
from set_data import customers,events,unique_id,display_formatted_row   

continue_text = "\nPress Enter to continue."

sorted_customers = sorted(customers, key=lambda x: (x[2], x[1])) # ordered by family name, then first name
sorted_events = {k: events[k] for k in sorted(events)} #  sort the events via dictionary comprehension, shortcut to create a new dictionary.

def list_all_customers():
    """
    Lists customer details.
    This is an example of how to produce basic output."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","First Name","Family Name","Birth Date","e-Mail"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for customer in customers:
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]

        display_formatted_row([id,fname,famname,birthdate,email],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    input(continue_text)

def list_customers_and_tickets():
    """
    Lists Customer details (including birth date), and the events they have purchased tickets to attend."""
    
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <28} {: <30}"    
    display_formatted_row(["ID","Family Name","First Name","Birth Date","e-Mail", "Events (Tickets)"],format_str)  
    event_names = sorted(events.keys())
    for customer in sorted_customers:
        tickets=[]
        for event_name in event_names:
            customer_data = events[event_name]["customers"]
            for data in customer_data:
                if data[0] == customer[0]:
                    tickets.append((event_name, data[1]))
        if len(tickets) == 0:
            tickets = 'N/A'
        else:
            ticket_info = ', '.join(f"{ticket[0]} ({ticket[1]})" for ticket in tickets)  # Extract the first element
            tickets = ticket_info
        customer.append(str(tickets))

        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]
        event = customer[5]

        display_formatted_row([id,famname,fname,birthdate,email,event],format_str)   

    input(continue_text)

def list_event_details():
    """
    List the events, show all details except Customers who have purchased tickets."""
    format_str = "{: <20} {: <18} {: <15} {: <14} {: <28}"    
    display_formatted_row(["Event Name","Age Restriction","Event Date","Capacity","Tickets Sold"],format_str)  
    for event_name in sorted_events:
        event = sorted_events[event_name]
        name=event_name
        age_restriction=str(event['age_restriction'])
        date=event['event_date'].strftime("%d %b %Y")
        capacity=str(event['capacity'])
        tickets_sold=str(event['tickets_sold'])
        display_formatted_row([name,age_restriction,date,capacity,tickets_sold],format_str) \
        
    input(continue_text)

def buy_tickets():
    """
    Choose a customer, then a future event, the purchase can only proceed if they meet the minimum age requirement and tickets are available """
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_new_customer():
    """
    Add a new customer to the customer list."""
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def list_future_available_events():
    """
    List all future events that have tickets available
    """
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)


def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TO SELWYN EVENT TICKETING SYSTEM ===")
    print(" 1 - List Customers")
    print(" 2 - List Customers and their Events")
    print(" 3 - List Event Details")
    print(" 4 - Buy Tickets")
    print(" 5 - Future Events with tickets")
    print(" 6 - Add New Customer")
    print(" X - Exit (stops the program)")


print("")
print("### Disable the main program for now so I can do some dev ###")
print("")


# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"

response = ""
while response != "X":
    disp_menu()
    
    print("")
    # Display menu for the first time, and ask for response
    response = input("Please enter menu choice: ")    
    print("")

    # Make the string uppercase either x or X is able to exit the program
    if response == "x":
        response = response.upper()

    if response == "1":
        list_all_customers()
    elif response == "2":
        list_customers_and_tickets()
    elif response == "3":
        list_event_details()
    elif response == "4":
        buy_tickets()
    elif response == "5":
        list_future_available_events()
    elif response == "6":
        add_new_customer()
    elif response != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)")

    print("")

print("\n=== Thank you for using the SELWYN EVENT TICKET SYSTEM! ===\n")

