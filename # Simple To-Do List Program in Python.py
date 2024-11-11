
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")

def show_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            status = "Done" if task['done'] else "Not done"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("\nYour To-Do list is empty.")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append({'task': task, 'done': False})
    print(f"Task '{task}' added.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
