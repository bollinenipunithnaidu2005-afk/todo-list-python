import os

FILE_NAME = "tasks.txt"

def menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")

    with open(FILE_NAME, "a") as file:
        file.write(task + ",Pending\n")

    print("✅ Task added!")

def view_tasks():
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return

    print("\n--- Task List ---")
    with open(FILE_NAME, "r") as file:
        for i, line in enumerate(file, start=1):
            task, status = line.strip().split(",")
            print(f"{i}. {task} [{status}]")

def mark_complete():
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        task, status = line.strip().split(",")
        print(f"{i}. {task} [{status}]")

    try:
        task_num = int(input("Enter task number to mark complete: "))
    except ValueError:
        print("❌ Please enter a valid number")
        return

    if 1 <= task_num <= len(lines):
        task, status = lines[task_num - 1].strip().split(",")
        lines[task_num - 1] = f"{task},Completed\n"

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        print("✅ Task marked as completed!")
    else:
        print("❌ Invalid task number")

def delete_task():
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        task, status = line.strip().split(",")
        print(f"{i}. {task} [{status}]")

    try:
        task_num = int(input("Enter task number to delete: "))
    except ValueError:
        print("❌ Please enter a valid number")
        return

    if 1 <= task_num <= len(lines):
        lines.pop(task_num - 1)

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        print("✅ Task deleted!")
    else:
        print("❌ Invalid task number")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        mark_complete()

    elif choice == '4':
        delete_task()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")