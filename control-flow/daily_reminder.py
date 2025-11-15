# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Modify reminder if task is time-bound
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder)
