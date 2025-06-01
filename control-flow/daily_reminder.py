# Get task information from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority using match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}'"

# Add time sensitivity information
if time_bound == "yes":
    if priority == "medium":
        reminder += " that should be completed within the next few days!"
    else:
        reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    elif priority == "medium":
        reminder += ". Plan to complete this task soon."
    else:
        reminder += ". Schedule this in your calendar."

# Display the reminder
print(reminder)
