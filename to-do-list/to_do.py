import os

class ToDoList:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [line.strip() for line in file.readlines()]
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self):
        task = input("Enter the task: ").strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty.")
            return
        print("\n--- Your Tasks ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def remove_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(self.tasks):
                removed = self.tasks.pop(task_num - 1)
                self.save_tasks()
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo = ToDoList()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            todo.add_task()
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
