tasks = []

def show_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. View Tasks")
    print("4. Exit")
    print("5. Delete Task")


def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")  
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

def mark_task_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        mark_task_done()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the program.")
        break
    elif choice == '5':
        delete_task()
    else:
        print("Invalid choice. Please select a valid option.")