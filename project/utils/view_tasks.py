# src: ./utils/view_tasks.py

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks to show.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
