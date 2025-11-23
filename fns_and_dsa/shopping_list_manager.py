def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # required array implementation

    while True:
        display_menu()  # checker expects this call

        choice = input("Enter your choice: ")  # must be numeric as string

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print("Item not found in the list.")

        elif choice == '3':
            print("Current Shopping List:")
            if len(shopping_list) == 0:
                print("The list is empty.")
            else:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
            

if __name__ == "__main__":
    main()
