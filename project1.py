from datetime import date, datetime
professional_tasks = []
personal_tasks = []
next_id = 1
def show_menu():
    print("\n TO-DO LIST MENU ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task (by ID)")
    print("4. Search by ID")
    print("5. Search by Date")
    print("6. Exit")

def print_task(task):
    print("ID:", task["id"],
          "| Task:", task["task"],
          "| Created:", task["task_date"],
          "| Due:", task["due_date"])

def get_valid_date(message):

    while True:
        text = input(message).strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date! Use format YYYY-MM-DD (example: 2026-10-25)")


# ---------- FEATURES ----------
def view_tasks():
    print("\nPROFESSIONAL TASKS")
    if not professional_tasks:
        print("No professional tasks.")
    else:
        for task in professional_tasks:
            print_task(task)

    print("\nPERSONAL TASKS")
    if not personal_tasks:
        print("No personal tasks.")
    else:
        for task in personal_tasks:
            print_task(task)


def add_task():
    global next_id

    task_name = input("\nEnter the task: ").strip()
    if task_name == "":
        print("Task cannot be empty.")
        return

    print("\nChoose category:")
    print("1. Professional")
    print("2. Personal")
    category = input("Enter 1 or 2: ").strip()
    if category not in ("1", "2"):
        print("Invalid category. Task not added.")
        return
    due_date = get_valid_date("Enter due date (YYYY-MM-DD): ")
    task = {
        "id": next_id,
        "task": task_name,
        "task_date": str(date.today()),
        "due_date": due_date,
    }
    if category == "1":
        professional_tasks.append(task)
        print("Added to PROFESSIONAL list. Task ID:", next_id)
    else:
        personal_tasks.append(task)
        print("Added to PERSONAL list. Task ID:", next_id)

    next_id += 1

def delete_task():
    if not professional_tasks and not personal_tasks:
        print("\nNo tasks to delete.")
        return

    view_tasks()
    text = input("\nEnter the Task ID to delete: ").strip()
    if not text.isdigit():
        print("Please enter a valid number.")
        return
    task_id = int(text)
    for task in professional_tasks:
        if task["id"] == task_id:
            professional_tasks.remove(task)
            print("Task", task_id, "deleted from PROFESSIONAL list.")
            return
    for task in personal_tasks:
        if task["id"] == task_id:
            personal_tasks.remove(task)
            print("Task", task_id, "deleted from PERSONAL list.")
            return
    print("No task found with ID", task_id)
def search_by_id():
    text = input("\nEnter the Task ID to search: ").strip()
    if not text.isdigit():
        print("Please enter a valid number.")
        return
    task_id = int(text)
    for task in professional_tasks:
        if task["id"] == task_id:
            print("\nFound in PROFESSIONAL list:")
            print_task(task)
            return
    for task in personal_tasks:
        if task["id"] == task_id:
            print("\nFound in PERSONAL list:")
            print_task(task)
            return
    print("No task found with ID", task_id)
def search_by_date():
    search_date = get_valid_date("\nEnter date to search (YYYY-MM-DD): ")
    found = False
    for task in professional_tasks:
        if task["task_date"] == search_date or task["due_date"] == search_date:
            print("[Professional]", end=" ")
            print_task(task)
            found = True
    for task in personal_tasks:
        if task["task_date"] == search_date or task["due_date"] == search_date:
            print("[Personal]", end=" ")
            print_task(task)
            found = True
    if not found:
        print("No tasks found for", search_date)
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            search_by_id()
        elif choice == "5":
            search_by_date()
        elif choice == "6":
            print("\nExiting the program")
            break
        else:
            print("\nInvalid choice...Please choose 1 to 6.")


if __name__ == "__main__":
    main()