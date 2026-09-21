import json
import os

TASK_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    try:
        if not os.path.exists(TASK_FILE):
            return []

        with open(TASK_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Error reading task file. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error saving tasks: {error}")


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- TASK LIST ---")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def complete_task(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task is already completed.")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print("Task completed successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Display the main menu."""
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    """Run the Task Manager application."""
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main() 
