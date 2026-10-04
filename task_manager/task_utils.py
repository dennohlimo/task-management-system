from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not (validate_task_title(title)
            and validate_task_description(description)
            and validate_due_date(due_date)):
        return
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = []
    for i, task in enumerate(tasks):
        if task["completed"] == False:
            pending.append(task)
            print(f"{i + 1}: {task['title']}")
            print(f"{task['description']}")
            print(f"due: {task['due_date']}")
    if len(pending) == 0:
        print("No pending tasks")
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    completed = 0
    for task in tasks:
        if task["completed"] == True:
            completed += 1
    progress = (completed / len(tasks)) * 100
    return progress