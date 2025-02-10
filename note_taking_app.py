import os

def display_menu():
    print("Note Taking App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

def view_notes():
    print("Your Notes")
    note_dir = "notes"
    if not os.path.exists(note_dir):
        print("No notes found.")
        return
    for filename in os.listdir(note_dir):
        with open(os.path.join(note_dir, filename), "r") as file:
           content =  file.read()
        print(f"Note {filename[:,-4]}:{content}")



def add_note():
    note_title = input("Enter your note title: ")
    note_content = input("Enter the content of your note: ")

    note_dir = "notes"
    if not os.path.exists(note_dir):
        os.makedirs(note_dir)

    note_file = os.path.join(note_dir, note_title + ".txt")
    with open(note_file, "w") as file:
        file.write(f"{note_title}\n")
        print(f"Note {note_title} has been added.")     
    
def delete_notes():
    note_title = input("Enter the title of the note you want to delete: ")
    note_file = os.path.join("notes", note_title + ".txt")
    if os.path.exists(note_file):
        os.remove(note_file)
        print(f"Note {note_title} has been deleted.")
    else:
        print(f"Note {note_title} not found.")



def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
