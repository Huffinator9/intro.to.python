# Coding Temple Intro to Python Module Project
# To Do CLI App

def show_menu():
    print("\nMenu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    task = input("\nEnter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"\nTask added: '{task}'")
    else:
        print("\nTask cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks to show.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

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

def main():
    tasks = []
    print("\nWelcome to the Newly Winged To Do List CLI App.")

    while True:
        show_menu()
        try:
            choice = input("\nSelect an option (1-4): ").strip()
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("\nGoodbye!\n")
                break
            else:
                print("\nInvalid option. Please choose between 1-4.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
