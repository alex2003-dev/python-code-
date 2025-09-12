todos = []

def add(task):
    todos.append(task)
    return todos

def remove(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return todos

def view():
    for i, t in enumerate(todos):
        print(f"{i}: {t}")
    return todos

def main():
    while True:
        cmd = input("cmd (add/rm/view/exit): ")
        if cmd == "add":
            t = input("task: ")
            add(t)
        elif cmd == "rm":
            i = int(input("index: "))
            remove(i)
        elif cmd == "view":
            view()
        elif cmd == "exit":
            break

main()