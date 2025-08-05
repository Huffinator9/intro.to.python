# Coding Temple Intro to Python Module Project
# To Do CLI App

from utils.add_task import add_task
from utils.show_menu import show_menu
from utils.view_tasks import view_tasks
from utils.delete_task import delete_task

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
