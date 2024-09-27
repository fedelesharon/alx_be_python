# pattern_drawing.py

def main():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))
        
        # Ensure the user enters a positive integer
        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Initialize a variable for the while loop
        row = 0
        
        # Use a while loop to iterate through each row
        while row < size:
            # Use a for loop to print the asterisks in each row
            for col in range(size):
                print("*", end="")
            # Move to the next line after each row
            print()
            row += 1

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
