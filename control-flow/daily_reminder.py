# Get task information from user
task = input("Enter your task: ")
priority = input("Enter priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process task based on priority using match case
match priority:
    case "high":
        reminder = f"URGENT: Complete '{task}' - High Priority"
    case "medium":
        reminder = f"IMPORTANT: Complete '{task}' - Medium Priority"
    case "low":
        reminder = f"REMINDER: Complete '{task}' - Low Priority"
    case _:
        reminder = f"REMINDER: Complete '{task}'"

# Add time sensitivity information
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Display the reminder
print(reminder)