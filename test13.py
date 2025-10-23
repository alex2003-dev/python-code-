
def add(n): open("notes.txt", "a").write(n + "\n")

def list(): 
    try: print(*open("notes.txt"), sep="")
    except: print("No notes found.")

def search(k):
    try:
        f = [l for l in open("notes.txt") if k.lower() in l.lower()]
        print(*f if f else ["No matches found."], sep="")
    except: print("No notes found.")

add("Buy milk")
add("Read book")
list()
search("milk")

