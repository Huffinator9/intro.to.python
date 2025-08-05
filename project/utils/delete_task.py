# src: ./utils/delete_task.py

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return
    view_tasks(tasks)
    try:
        index = int(input("\nEnter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"\nDeleted task: '{removed}'")
        else:
            print("\nTask number out of range.")
    except ValueError:
        print("\nPlease enter a valid number.")
