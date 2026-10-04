# Import functions from task_manager.task_utils package
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                add_task(title,description,due_date)
            except ValueError as error:
                print("Error:", error)
                
        elif choice == "2":
            try:
                task_number = int(input("Enter the task number to mark as done: "))
                mark_task_as_complete(task_number-1)
            except ValueError:
                print("Error: Please enter a valid number")
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            progress=calculate_progress()
            print("Progress", round(progress, 2), "%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
