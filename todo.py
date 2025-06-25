def display_menu():
    print("\nTo-Do List Manager")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['description']} - {status}")

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    print(f"\nTask '{description}' added successfully.")

def update_task(tasks, index, description=None, completed=None):
    if 1 <= index <= len(tasks):
        if description:
            tasks[index-1]["description"] = description
            print(f"\nTask {index} description updated.")
        if completed is not None:
            tasks[index-1]["completed"] = completed
            print(f"\nTask {index} status updated to {'Completed' if completed else 'Pending'}.")
    else:
        print("\nInvalid task number.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index-1)
        print(f"\nTask '{removed_task['description']}' deleted.")
    else:
        print("\nInvalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
        
        elif choice == "2":
            description = input("Enter task description: ")
            if description.strip():
                add_task(tasks, description)
            else:
                print("\nTask description cannot be empty.")
        
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to update: "))
                update_choice = input("Update (1) Description, (2) Status, or (3) Both? (1-3): ")
                if update_choice == "1":
                    description = input("Enter new description: ")
                    if description.strip():
                        update_task(tasks, index, description=description)
                    else:
                        print("\nDescription cannot be empty.")
                elif update_choice == "2":
                    status = input("Mark as (C)ompleted or (P)ending? (C/P): ").lower()
                    if status in ["c", "p"]:
                        update_task(tasks, index, completed=(status == "c"))
                    else:
                        print("\nInvalid status choice.")
                elif update_choice == "3":
                    description = input("Enter new description: ")
                    if description.strip():
                        status = input("Mark as (C)ompleted or (P)ending? (C/P): ").lower()
                        if status in ["c", "p"]:
                            update_task(tasks, index, description=description, completed=(status == "c"))
                        else:
                            print("\nInvalid status choice.")
                    else:
                        print("\nDescription cannot be empty.")
                else:
                    print("\nInvalid update choice.")
            except ValueError:
                print("\nInvalid task number.")
        
        elif choice == "4":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(tasks, index)
            except ValueError:
                print("\nInvalid task number.")
        
        elif choice == "5":
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()