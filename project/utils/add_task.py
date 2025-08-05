# src: ./utils/add_task.py

def add_task(tasks):
    task = input("\nEnter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"\nTask added: '{task}'")
    else:
        print("\nTask cannot be empty!")
