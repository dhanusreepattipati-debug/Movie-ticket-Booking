# Movie-ticket-Booking
Movie Ticket Booking System 🎬

A simple Python console-based Movie Ticket Booking System that allows users to:

Book movie tickets
Cancel booked tickets
View theater seat layout
Display booking summary and revenue
Generate random ticket codes

This project is beginner-friendly and demonstrates important Python concepts like:

Functions
Dictionaries
Lists
Tuples
Loops
Conditional statements
Lambda & Filter
Recursion
Random module
📌 Features

✅ Movie setup with custom movie name, timing, ticket price, rows, and seats
✅ Visual theater seat layout using rows and columns
✅ Ticket booking system
✅ Ticket cancellation system
✅ Random ticket code generation
✅ Booking summary with revenue calculation
✅ Recursive menu system
✅ Displays available and booked seats

🛠️ Technologies Used
Python 3
📂 Project Structure
Movie-Ticket-Booking-System/
│
├── movie_ticket_booking.py
└── README.md
▶️ How to Run the Project
Step 1: Install Python

Download Python from:

Python Official Website

Make sure Python is installed correctly.

Check using:

python --version
Step 2: Download the Project

Clone the repository:

git clone https://github.com/your-username/Movie-Ticket-Booking-System.git

Or download ZIP from GitHub.

Step 3: Open in VS Code

Open the project folder in:

Visual Studio Code

Step 4: Run the Program

Open terminal and run:

python movie_ticket_booking.py
💻 Sample Output
--- MOVIE SETUP ---
Enter Movie Name: Avengers
Enter Time: 7 PM
Enter Ticket Price: 200
How many rows?: 3
How many seats per row?: 5

1. Book Ticket
2. Cancel Ticket
3. Show Summary
4. Exit
🎯 Concepts Used in the Project
Concept	Usage
Dictionary	Store seat status and ticket code
Tuple	Seat positions like ('A', 1)
List	Store booking details
Loops	Create seat arrangement
Functions	Separate functionalities
Conditional Statements	Check seat availability
Lambda + Filter	Find available seats
Random Module	Generate ticket codes
Recursion	Repeat menu system
🪑 Seat Layout Example
      1  2  3  4  5
      ---------------
A:    [ ][X][ ][ ][ ]
B:    [ ][ ][X][ ][ ]
C:    [ ][ ][ ][ ][ ]

Legend:
[ ] = Free
[X] = Booked
📊 Summary Information

The project displays:

Total seats
Booked seats
Available seats
Ticket codes
Total revenue
🚀 Future Improvements

You can improve this project by adding:

User login system
Database connection (MySQL)
GUI using Tkinter
Online payment integration
Multiple movie support
File handling for saving bookings
