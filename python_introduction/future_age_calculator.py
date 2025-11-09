#!/usr/bin/python3
# future_age_calculator.py

# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Calculate age in 2050 (assuming current year is 2023)
years_until_2050 = 2050 - 2023
future_age = current_age + years_until_2050

# Print the result
print(f"In 2050, you will be {future_age} years old.")
