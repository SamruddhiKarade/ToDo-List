# ToDo-List Application (Python)
A simple **command-line To-Do List application** built using Python.  
This project helps users manage daily tasks by allowing them to add tasks, view them, mark them as completed, and optionally set due dates.  
Tasks are stored locally using a JSON file to maintain persistence.

---

## Features

- Add new tasks
- View all tasks with completion status
- Mark tasks as completed
- Optional due date and time for tasks
- Data persistence using JSON file
- Simple and user-friendly CLI menu

---

## Technologies Used

- Python 3
- JSON (for data storage)
- datetime module
- File handling

---

## Project Structure
todo-list-python/
│
├── todo.py # Main Python application
├── basic_tasks.json # Stores task data (auto-generated)
├── README.md # Project documentation
└── .gitignore # Ignored files

---

## How to Run the Project

1. Make sure Python is installed:
python --version
2. Clone the repository:
git clone https://github.com/your-username/todo-list-python.git
3. Navigate to the project directory:
cd todo-list-python
4. Run the application:
python todo.py

---

## Application Menu
1. Add a task
2. View tasks
3. Mark task as complete
4. Exit

---

## Due Date Format

When entering a due date, use the following format:
YYYY-MM-DD HH:MM
Example:
2026-01-15 18:30

If no due date is required, you can leave the input blank.

---

## Learning Outcomes

- Understanding Python file handling
- Working with JSON data
- Using the `datetime` module
- Implementing a menu-driven CLI application
- Writing clean and modular Python code

---

## Author

**Samruddhi Karade**

---

## License

This project is created for learning and academic purposes.


