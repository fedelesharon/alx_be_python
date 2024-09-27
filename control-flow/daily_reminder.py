# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task based on priority using match case
    match priority:
        case 'high':
            message = f"'{task}' is a high priority task"
        case 'medium':
            message = f"'{task}' is a medium priority task"
        case 'low':
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Modify the reminder if the task is time-bound
    if time_bound == 'yes':
        message += " that requires immediate attention today!"
    elif time_bound == 'no':
        message += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    # Print the customized reminder
    print(f"Reminder: {message}")

if __name__ == "__main__":
    main()
