# 9/12/2024 - codecademy "introduction to lists - review"

# practicing usage of lists (finished exercises on codecademy)

# personal practice:

# use chatgpt to create a simple project with tasks, avoid direct guidance,
# use documentation predominantly

# Grocery List Manager

def display_menu():
    print("\nGrocery List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear List")
    print("5. Exit")

def main():
    grocery_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:
                grocery_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in grocery_list:
                grocery_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            if grocery_list:
                print("\nCurrent Grocery List:")
                for idx, item in enumerate(grocery_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The grocery list is empty.")
        elif choice == '4':
            confirm = input("Are you sure you want to clear the list? (yes/no): ").strip().lower()
            if confirm == 'yes':
                grocery_list.clear()
                print("The list has been cleared.")
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
