import json
from pathlib import Path

def load():
    if Path('../files/tasks.json').exists():
        return json.load(open('../files/tasks.json', 'r'))
    return []

def save(tasks):
    json.dump(tasks, open('../files/tasks.json', 'w'), indent=2, ensure_ascii=False)

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
            print(f"Enter a valid number!")
    elif cmd == "4":
        exit(0)