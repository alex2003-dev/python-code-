import json
import os

file_name = "tasks.json"

class Task:
    def __init__(self, title, date, status):
        self.title = title
        self.date = date
        self.status = status

    def to_dict(self):
        return {"title": self.title, "date": self.date, "status": self.status}

def load_tasks():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            return [Task(x["title"], x["date"], x["status"]) for x in data]
    except:
        print("Error loading file")
        return []

def save_tasks(tasks):
    try:
        with open(file_name, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
    except:
        print("Error saving file")

def add_task():
    title = input("Title: ")
    date = input("Due date (YYYY-MM-DD): ")
    status = input("Status (todo/done): ")
    t = Task(title, date, status)
    tasks = load_tasks()
    tasks.append(t)
    save_tasks(tasks)
    print("Task added")

def show_all():
    tasks = load_tasks()
    for t in tasks:
        print(t.title, "-", t.date, "-", t.status)

def filter_status():
    s = input("Status: ")
    tasks = load_tasks()
    for t in tasks:
        if t.status.lower() == s.lower():
            print(t.title, "-", t.date, "-", t.status)

def filter_date():
    d = input("Date (YYYY-MM-DD): ")
    tasks = load_tasks()
    for t in tasks:
        if t.date == d:
            print(t.title, "-", t.date, "-", t.status)

def main():
    while True:
        print("\n1 Add task")
        print("2 Show all")
        print("3 Filter by status")
        print("4 Filter by date")
        print("5 Exit")
        c = input("Choose: ")
        if c == "1":
            add_task()
        elif c == "2":
            show_all()
        elif c == "3":
            filter_status()
        elif c == "4":
            filter_date()
        elif c == "5":
            print("Bye")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
