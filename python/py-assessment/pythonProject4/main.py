# main.py
import note_manager
import log_manager
import validation

def display_menu():
    """Display the application menu to the user."""
    print("     Welcome to python  E-Note")
    print("\n")
    print("     Press 1 for generate Note")
    print("     Press 2 for view Note")
    print("     Press 3 for Exit")
    print("\n")

def main():
    """Main function driving the application."""
    note_manager.initialize_notes_directory()
    log_manager.initialize_logger()

    while True:
        display_menu()
        choice = input("Enter your choice : ")

        if validation.validate_choice(choice):
            if choice == '1':
                note_manager.add_note()
                log_manager.log_transaction("Added a new note.")
            elif choice == '2':
                note_manager.view_notes()
                log_manager.log_transaction("Viewed notes.")
            elif choice == '3':
                confirm_exit = input("Are you sure you want to exit? (yes/no): ")
                if confirm_exit.lower() == 'yes':
                    print("Exiting E-Note Book. Goodbye!")
                    log_manager.log_transaction("Exited the application.")
                    break
                else:
                    print("Returning to menu.")
        else:
            print("Invalid choice, please select a valid option.")
        # Continue displaying menu until user exits.

if __name__ == "__main__":
    main()
