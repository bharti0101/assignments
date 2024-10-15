import os

NOTES_DIR = 'notes/'

def initialize_notes_directory():
    """Create the notes directory if it doesn't exist."""
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def add_note():
    """Add a new note by asking the user for input."""
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    if title and content:
        filename = f"{NOTES_DIR}{title}.txt"
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Note '{title}' saved successfully.")
    else:
        print("Title and content cannot be empty!")

def view_notes():
    """Display all notes stored in the notes directory."""
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes available.")
    else:
        for note in notes:
            print(f"\n--- {note.replace('.txt', '')} ---")
            with open(f"{NOTES_DIR}{note}", 'r') as file:
                print(file.read())
            print("-" * 20)
