from datetime import datetime, timedelta

def display_current_datetime():
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    # Formatting and printing the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Part 2: Calculate a Future Date
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Printing the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
