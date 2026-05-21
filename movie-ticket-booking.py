import random

# --- Global Variables ---
print("--- MOVIE SETUP ---")
movie_name = input("Enter Movie Name: ")
movie_time = input("Enter Time: ")
price = int(input("Enter Ticket Price: "))
rows = int(input("How many rows?: "))
cols = int(input("How many seats per row?: "))

# Using a Dictionary where Key is a Tuple (Row, Col) and Value is a List [Status, Code]
# Example: seats[('A', 1)] = ['Free', 0]
seats = {} 
row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Using Loops to make the seats
for r in range(rows):
    current_row_char = row_letters[r]
    for c in range(1, cols + 1):
        # Tuple used here (Row, Number)
        seat_pos = (current_row_char, c)
        # List used here ['Free', 0]
        seats[seat_pos] = ['Free', 0]

# --- Functions ---

def display_seats():
    """Display visual seat layout with Y-axis (rows) and X-axis (columns)"""
    print("\n" + "="*60)
    print("SEAT LAYOUT - Theater")
    print("="*60)
    
    # X-axis header (seat numbers)
    print("      ", end="")
    for c in range(1, cols + 1):
        print(f"{c:3}", end="")
    print()
    print("      " + "-" * (cols * 3))
    
    # Y-axis (rows) with seat status
    for r in range(rows):
        current_row_char = row_letters[r]
        print(f"{current_row_char}:    ", end="")
        
        for c in range(1, cols + 1):
            seat_pos = (current_row_char, c)
            if seats[seat_pos][0] == 'Free':
                print("[ ]", end="")
            else:
                print("[X]", end="")
        print()
    
    print("      " + "-" * (cols * 3))
    print("\nLegend: [ ] = Free | [X] = Booked")
    print("="*60)

def display_summary():
    print("\n" + "="*30)
    print("MOVIE DETAILS")
    print("Movie:", movie_name)
    print("Time:", movie_time)
    
    # Requirement: Use lambda with filter to find available seats
    # We allow the filter to look at the keys where the value at index 0 is 'Free'
    available_list = list(filter(lambda x: seats[x][0] == 'Free', seats))
    
    # Calculate booked seats
    booked_list = []
    for s in seats:
        if seats[s][0] == 'Booked':
            booked_list.append(s)
            
    total_revenue = len(booked_list) * price
    
    print("Total Seats:", len(seats))
    print("Booked Seats:", len(booked_list))
    print("Revenue: $", total_revenue)
    
    print("\nAvailable Seats (Row, Col):")
    print(available_list)
    
    print("\nYour Bookings:")
    for b in booked_list:
        # Show ticket code
        print("Seat:", b, "Code:", seats[b][1])
    print("="*30)

def book_seat():
    display_seats()
    print("\n-- BOOKING --")
    r_in = input("Enter Row Letter (Y-axis, e.g., A, B, C): ").upper()
    c_in = int(input("Enter Seat Number (X-axis, e.g., 1, 2, 3): "))
    
    target = (r_in, c_in) # Tuple
    
    # Conditionals to check availability
    if target in seats:
        if seats[target][0] == 'Free':
            # Requirement: Use random to generate ticket code
            ticket_code = random.randint(1000, 9999)
            
            seats[target][0] = 'Booked'
            seats[target][1] = ticket_code
            print("Success! Ticket Code is:", ticket_code)
        else:
            print("Sorry, that seat is already taken.")
    else:
        print("Invalid seat selection.")

def cancel_seat():
    display_seats()
    print("\n-- CANCELLING --")
    r_in = input("Enter Row Letter (Y-axis, e.g., A, B, C): ").upper()
    c_in = int(input("Enter Seat Number (X-axis, e.g., 1, 2, 3): "))
    
    target = (r_in, c_in)
    
    if target in seats:
        if seats[target][0] == 'Booked':
            seats[target][0] = 'Free'
            seats[target][1] = 0
            print("Booking cancelled.")
        else:
            print("This seat wasn't booked anyway.")
    else:
        print("Invalid seat.")

# Requirement: Use recursion for repeated menu
def menu():
    print("\n1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Show Summary")
    print("4. Exit")
    
    choice = input("Select option: ")
    
    if choice == '1':
        book_seat()
        menu() # Recursive call
    elif choice == '2':
        cancel_seat()
        menu() # Recursive call
    elif choice == '3':
        display_summary()
        display_seats()
        menu() # Recursive call
    elif choice == '4':
        # Show final state before leaving
        display_summary()
        display_seats()
        print("Bye!")
    else:
        print("Wrong input.")
        menu() # Recursive call

# --- Run the Code ---
menu()
