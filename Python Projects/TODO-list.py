import json
from pathlib import Path


TASKS_FILE = Path(__file__).parent.parent / "files" / "tasks.json"

def load():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(tasks):
    
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


tasks = load()
print("""
 - TODO -
1. Append
2. Show
3. Delete
4. Exit
    """)

while True:
    cmd = input("Menu > ")

    if cmd == "1":
        tasks.append(input("New task > "))
        save(tasks)
    elif cmd == "2":
        for i, t in enumerate(tasks, 1):
            print(f"- {i}. {t}")
    elif cmd == "3":
        try:
            num = int(input("Task number > "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                save(tasks)
                print("Deleted!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Enter a valid number!")
    elif cmd == "4":
        exit(0)