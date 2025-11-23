from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()  # save in variable
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # save in variable
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    try:
        user_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_days)
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
