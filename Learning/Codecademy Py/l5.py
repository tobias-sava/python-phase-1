# 10/12/2024

# creating a simple to-do list application

# using chatgpt-generated flow

# features needed:
# 1. add tasks
# 2. remove tasks
# 3. view all tasks
# 4. mark tasks as done (assign boolean)

tasks = [["test", False], ["test2", True]]

def menu():
    print("\nWelcome to to-do.")
    print("1. Add task.")
    print("2. Remove task.")
    print("3. View tasks.")
    print("4. Mark task as completed")
    print("5. Exit.")
    
def main():
    
    while True:
        user_choice = input("Please input a number from (1-5): ")
        if user_choice == '1':
            task_add = input("Please enter task:").strip().lower()
            tasks.append([task_add, False])
            print(f"{task_add} has been added.")
        
        elif user_choice == '2':
            print(tasks)
            task_remove = int(input("Enter task number to remove: "))
            tasks.pop([task_remove])
            print(f"Task {task_remove} has been removed.")

# taking break this is not good

# moving on


