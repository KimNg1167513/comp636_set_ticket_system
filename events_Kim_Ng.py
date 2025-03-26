# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: Kim Ng (Lion)
# Student ID : 1167513 
# ================================================================
 
from datetime import datetime,timedelta,date     # datetime module is required for working with dates

# Make the variables and function in set_data.py available in this code (without needing 'set_data.' prefix)
from set_data import customers,events,unique_id,display_formatted_row 

# Alternative for testing   
# from set_data_alternative import customers,events,unique_id,display_formatted_row   

continue_text = "\nPress Enter to continue."

sorted_customers = sorted(customers, key=lambda x: (x[2], x[1])) # ordered by family name, then first name
sorted_events = {k: events[k] for k in sorted(events)} #  sort the events via dictionary comprehension, shortcut to create a new dictionary.

def list_all_customers(sorted=False):
    """
    Lists customer details.
    This is an example of how to produce basic output."""
    if sorted == True:
        data = sorted_customers
    else:
        data = customers

    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","First Name","Family Name","Birth Date","e-Mail"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for customer in data:
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]

        display_formatted_row([id,fname,famname,birthdate,email],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    input(continue_text)

def list_customers_and_tickets(do_not_continue=False):
    """
    Lists Customer details (including birth date), and the events they have purchased tickets to attend."""
    # sorted_customers = sorted(customers, key=lambda x: (x[2], x[1]))  # update the sorted events in case a new customer is added
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

        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]
        event = str(tickets)

        display_formatted_row([id,famname,fname,birthdate,email,event],format_str)   

    if do_not_continue == False:
        input(continue_text)

def list_event_details(age=None):
    """
    List the events, show all details except Customers who have purchased tickets."""
    # age is an argument to filter the events for age_restriction, if this argument is provided, the event auto filtered by the date as well

    format_str = "{: <25} {: <18} {: <15} {: <14} {: <28}"    
    format_str_with_id = "{: <10} {: <18} {: <15} {: <14} {: <28}"    
    
    if age:
        display_formatted_row(["ID","Event Name","Event Date","Capacity","Tickets Sold"],format_str_with_id)  
        result=[]
    else:
        display_formatted_row(["Event Name","Age Restriction","Event Date","Capacity","Tickets Sold"],format_str)  

    for index, event_name in enumerate(sorted_events, start=1):
        event = sorted_events[event_name]
        if age:
            # Check if the event has passed, the age restriction and if the tickets are sold up
            if datetime.now().date() >= event['event_date'] or age < int(event['age_restriction']) or event["capacity"] - event['tickets_sold'] <= 0:
                continue

        event_id = index
        name=event_name
        age_restriction=str(event['age_restriction'])
        date=event['event_date'].strftime("%d %b %Y")
        capacity=str(event['capacity'])
        tickets_sold=str(event['tickets_sold'])
        if age:
            display_formatted_row([event_id,name,date,capacity,tickets_sold],format_str_with_id)
            result.append({"id":event_id,"name":name ,"age_restriction":age_restriction,"event_date":date,"capacity":capacity,"tickets_sold":tickets_sold, "customers":event['customers']})
        else:
            display_formatted_row([name,age_restriction,date,capacity,tickets_sold],format_str)
    
    if age:
        return result
    else:        
        input(continue_text)

def buy_tickets():
    """
    Choose a customer, then a future event, the purchase can only proceed if they meet the minimum age requirement and tickets are available """
    
    # Display ordered customer name and ask which customer you want to buy for
    def getCustomerID():
        list_customers_and_tickets(True)
        print("")
        customer_id = input('Please select a customer by entering ID or enter "X" to escape: ')
        # return customer_id
        
        if customer_id:
            if customer_id == 'X' or customer_id == 'x':
                pass
            else:
                try:
                    customer_id = int(customer_id)
                    print(f'Checking the given ID:({customer_id})...')
                    # target_customer = next((customer for customer in sorted_customers if customer[0] == customer_id), None)
                    target_customer = next((customer for customer in sorted_customers if customer[0] == customer_id), None)
                    if target_customer == None:
                        print(f'ID: {customer_id} not found, please enter an valid ID.')
                        print('')
                        getCustomerID()
                    else:
                        # Found the customer, display events
                        # Check the DOB and today's date
                        age = datetime.now().year - target_customer[3].year
                        
                        # Filter the events, so the customer can only see the suitable events
                        available_events = list_event_details(age)
                        # print(available_events)
                        
                        def buyTicket():
                            while True:
                                # 1st, check if input is an integer
                                try:
                                    target_event_id = int(input('Please enter the Event ID: '))
                                except ValueError:
                                    print('Please enter an valid event ID.')
                                    continue # Skip the rest and retry

                                # Then, check if event exists
                                target_event = next((ev for ev in available_events if ev['id'] == target_event_id), None)
                                if target_event is None:
                                    print("Oops, event ID not found.")
                                    continue

                                try:
                                    remain_tickets = int(target_event['capacity']) - int(target_event['tickets_sold'])
                                    ticket_quantity = int(input(f'How many tickets you want to buy (min 1 ~ max {remain_tickets}): '))
                                except ValueError:
                                    print('Please enter a valid number.')
                                    continue

                                if ticket_quantity > remain_tickets or ticket_quantity <= 0:
                                    print('Oops, please enter a valid number.')
                                    continue
                                else:
                                    print(f'Customer ID: {customer_id}, Event Name: {target_event["name"]}, Ticket Bought: {ticket_quantity}')
                                    customer_data = sorted_events[target_event["name"]]['customers']
                                    for index, customer in enumerate(customer_data):
                                        if customer[0] == customer_id:
                                            customer_data[index] = (customer_id, customer[1] + ticket_quantity)
                                            break
                                    else: # Only runs if the loop completes without breaking (no match found)
                                        customer_data.append((customer_id, ticket_quantity))
                                    sorted_events[target_event["name"]]['tickets_sold'] += ticket_quantity # update tickets sold
                                    # print(customer_data)
                                break
                        
                        buyTicket()

                        buy_more = get_yes_no_input('Do you want to buy more tickets? Please enter "y" for yes, "n" for no: ')
                        
                        if buy_more == 'Y':
                            buy_tickets()
                        else:
                            print('Thank You for Purchasing!')
                        
                        # print(sorted_events)
                except ValueError:
                    print("Please enter an valid ID.")
                    print('')
                    getCustomerID()            
        else:
            print("!!! Please select a customer to continue.")
            getCustomerID()

        
    # Display filter events (age restriction and date) and ask which event
    # Multiple events?

    getCustomerID()
    # input(continue_text) 

def add_new_customer():
    """
    Add a new customer to the customer list."""

    exit_prompt = '(or "x" to exit)'
    def get_input(prompt):
        value = input(prompt).strip()
        if value.upper() == 'X':
            raise SystemExit("Quiting...")
        elif value == "":
            get_input(prompt)
        return value
    
    def dob_nz_format():
        today = datetime.now()
        while True:
            user_input = input("Enter date (DD/MM/YYYY): ").strip()
            try:
                # parse with NZ format
                date_obj = datetime.strptime(user_input, "%d/%m/%Y").date()
                delta = today.date() - date_obj
                # Approximate (doesn't account for leap years)
                if delta >= timedelta(days=110*365) or delta < timedelta(days=0):
                    raise ValueError
                return date_obj
            except ValueError:
                print("Please enter a valid date. Please use DD/MM/YYYY (e.g., 24/03/1991)")

    
    try:
        while True:
            firstname = get_input(f'Please enter firstname {exit_prompt}: ')
            lastname = get_input(f'Please enter lastname {exit_prompt}: ')
            date_of_birth = dob_nz_format()
            email = input(f'Please enter a valid email, optional, press enter to skip {exit_prompt}: ').strip()
            if email == '':
                email = 'N/A'

            new_customer = [unique_id(), firstname.capitalize(), lastname.capitalize(), date_of_birth, email]

            customers.append(new_customer)
            sorted_customers.append(new_customer)

            print("")
            print("Thank you for you input.")
            break
    except SystemExit:
        pass
        

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

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().upper()
        if response in ('Y', 'N'):
            return response
        print('Opps, something is wrong. Please enter "y" or "n".')

print("")
print("### Disable the main program for now so I can do some dev ###")
print("")
# add_new_customer()
# exit() # for dev

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

