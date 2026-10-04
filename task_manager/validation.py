from datetime import datetime

def validate_task_title(title):
    if not title:
        print("Title cannot be empty")
        return False
    return True
    
def validate_task_description(description):
    if not description:
        print("Description cannot be empty") 
        return False
    return True  
    
def validate_due_date(due_date):
    if not due_date:
        print("Due date cannot be empty")
        return False
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return False

