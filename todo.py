class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add task\n2. View tasks\n3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()