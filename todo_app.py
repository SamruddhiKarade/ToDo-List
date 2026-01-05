import json
import os
from datetime import datetime

# --- Global Variables ---
TASKS_FILE = "basic_tasks.json"  # A different file name for this basic version
tasks = []  # This list will hold our tasks

# --- Core Functions ---

def load_tasks():
    """Loads tasks from the JSON file."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                tasks = json.load(f)
            print("Tasks loaded.")
        except json.JSONDecodeError:
            print("Error loading tasks file. Starting fresh.")
            tasks = []
    else:
        print("No task file found. Starting with an empty list.")
        tasks = []


def save_tasks():
    """Saves current tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
    print("Tasks saved.")


def add_task(name, due_str=None):
    """Adds a new task with an optional due date/time."""
    name = name.strip()
    if not name:
        print("Task name cannot be empty.")
        return

    due = None
    if due_str:
        try:
            due_dt = datetime.strptime(due_str, "%Y-%m-%d %H:%M")
            due = due_dt.isoformat()
        except ValueError:
            print("Invalid date/time format. Use YYYY-MM-DD HH:MM. Task will have no due date.")

    tasks.append({"name": name, "completed": False, "due": due})
    print(f"Added: '{name}'" + (f", due {due}" if due else ""))
    save_tasks()


def view_tasks():
    """Displays all tasks with status and due dates."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        status = "✓" if task.get("completed") else " "
        due_str = task.get("due")
        if due_str:
            due_dt = datetime.fromisoformat(due_str)
            due_fmt = due_dt.strftime("%Y-%m-%d %H:%M")
            print(f"{i + 1}. [{status}] {task['name']} (Due: {due_fmt})")
        else:
            print(f"{i + 1}. [{status}] {task['name']}")
    print("-----------------------\n")


def mark_task_complete(index):
    """Marks a task as complete."""
    if 0 <= index < len(tasks):
        if not tasks[index].get("completed"):
            tasks[index]["completed"] = True
            print(f"Completed: '{tasks[index]['name']}'")
            save_tasks()
        else:
            print(f"Task '{tasks[index]['name']}' is already complete.")
    else:
        print("Invalid task number.")

# --- Main Application Loop ---

def main():
    """Runs the main To-Do List application."""
    load_tasks()  # Load tasks when the app starts

    while True:
        print("\n--- Menu ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            task_name = input("Enter new task: ")
            due_input = input("Enter due date and time (YYYY-MM-DD HH:MM), or leave blank: ")
            due_input = due_input.strip() or None
            add_task(task_name, due_input)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()  # Show tasks first
            try:
                task_num = int(input("Enter task number to complete: "))
                mark_task_complete(task_num - 1)  # Adjust for 0-based index
            except ValueError:
                print("Please enter a number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# --- Run the application ---

if __name__ == "__main__":
    main()
