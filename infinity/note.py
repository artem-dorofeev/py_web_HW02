import os
import subprocess

NOTES_FOLDER = 'notes'


def add_note(note_name: str, tags: list) -> None:
    note_filename = f"{note_name}.md"
    note_path = os.path.join(NOTES_FOLDER, note_filename)

    if os.path.exists(note_path):
        print(f"[-] Note '{note_name}' already exists. Use a different name.")
    else:
        with open(note_path, 'w') as note_file:
            if tags:
                tag_line = ' '.join(tags)
                note_file.write(f"Tags: {tag_line}\n")

        open_in_default_editor(note_path)


def delete_note(note_name: str) -> None:
    note_path = os.path.join(NOTES_FOLDER, f"{note_name}.md")

    if os.path.exists(note_path):
        os.remove(note_path)
        print(f"[+] Deleted note: {note_name}.md")
    else:
        print("[-] Note not found.")


def edit_note(note_name: str) -> None:
    note_path = os.path.join(NOTES_FOLDER, f"{note_name}.md")

    if os.path.exists(note_path):
        open_in_default_editor(note_path)
    else:
        print("[-] Note not found.")


def edit_tags(note_name: str) -> None:
    note_path = os.path.join(NOTES_FOLDER, f"{note_name}.md")

    if os.path.exists(note_path):
        with open(note_path, 'r') as note_file:
            lines = note_file.readlines()

        tags_line_index = None
        for i, line in enumerate(lines):
            if line.startswith("Tags:"):
                tags_line_index = i
                break

        if tags_line_index is not None:
            tags = input("Enter new tags (space-separated): ").split()
            lines[tags_line_index] = f"Tags: {' '.join(tags)}\n"

            with open(note_path, 'w') as note_file:
                note_file.writelines(lines)
        else:
            print("[-] No tags found in the note.")

    else:
        print("[-] Note not found.")


def show_all_notes() -> None:
    note_files = [f for f in os.listdir(NOTES_FOLDER) if f.endswith('.md')]

    if note_files:
        print("[+] Result:")
        for idx, note_file in enumerate(note_files, start=1):
            note_name = os.path.splitext(note_file)[0]
            tags = get_tags_from_note_file(os.path.join(NOTES_FOLDER, note_file))
            tag_line = ' '.join(tags) if tags else "No tags"
            print(f"{idx}. {note_name} - Tags: {tag_line}")
    else:
        print("[-] No notes found.")


def get_tags_from_note_file(note_path: str) -> list:
    with open(note_path, 'r') as note_file:
        for line in note_file:
            if line.startswith("Tags:"):
                return line.strip().replace("Tags:", "").strip().split()
    return []


def search_note_by_name(name: str) -> None:
    note_files = [f for f in os.listdir(NOTES_FOLDER) if f.endswith('.md') and name in f]

    if note_files:
        print("[+] Result:")
        for note_file in note_files:
            note_name = os.path.splitext(note_file)[0]
            tags = get_tags_from_note_file(os.path.join(NOTES_FOLDER, note_file))
            tag_line = ' '.join(tags) if tags else "No tags"
            print(f"{note_name} - Tags: {tag_line}")
    else:
        print("[-] No matching notes found.")


def search_note_by_tag(tag: str) -> None:
    note_files = []
    for note_file in os.listdir(NOTES_FOLDER):
        if note_file.endswith('.md'):
            note_path = os.path.join(NOTES_FOLDER, note_file)
            tags = get_tags_from_note_file(note_path)
            if tag in tags:
                note_name = os.path.splitext(note_file)[0]
                print(f"{note_name} - Tags: {' '.join(tags)}")
                note_files.append(note_file)

    if not note_files:
        print("[-] No notes with matching tag found.")


def open_in_default_editor(filename: str) -> None:
    try:
        if os.name == 'nt':  # Windows
            os.startfile(filename)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['xdg-open', filename])
    except Exception as e:
        print(f"[-] Error opening the file in the default editor: {e}")


def note_book() -> None:
    if not os.path.exists(NOTES_FOLDER):
        os.mkdir(NOTES_FOLDER)

    while True:
        command = input("\nNOTE BOOK: Enter valid commad or enter \"exit\" to leave>>> ")
        parts = command.split()

        if not parts:
            continue

        action = parts[0] if len(parts) >= 1 else ""
        sub_action = parts[1] if len(parts) >= 2 else ""
        note_name = parts[2] if len(parts) >= 3 else ""
        tags = parts[3:] if len(parts) > 3 else []

        if action == 'help':
            print("[i] Commands: 'add note <name> <tags>', 'delete note <name>', 'edit note <name>', 'edit tags <name>', 'show all', 'search note <name>', 'search tag <tag>', exit")
        elif action == 'add' and sub_action == 'note':
            add_note(note_name, tags)
        elif action == 'delete' and sub_action == 'note':
            delete_note(note_name)
        elif action == 'edit' and sub_action == 'note':
            edit_note(note_name)
        elif action == 'edit' and sub_action == 'tags':
            edit_tags(note_name)
        elif action == 'show' and sub_action == 'all' and len(parts) == 2:
            show_all_notes()
        elif action == 'search' and sub_action == 'note' and len(parts) == 3:
            search_note_by_name(note_name)
        elif action == 'search' and sub_action == 'tag' and len(parts) == 3:
            search_note_by_tag(note_name)
        elif action == 'clear' and len(parts) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif action == 'exit' and len(parts) == 1:
            return "NOTE BOOK: End of programm!"
        else:
            print("[-] Invalid command. Try again.")


if __name__ == "__main__":
    note_book()
