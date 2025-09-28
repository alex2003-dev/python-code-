f = open("log.txt")
i = w = e = 0
for l in f:
    if "INFO" in l: i += 1
    elif "WARN" in l: w += 1
    elif "ERROR" in l: e += 1
f.close()
print("INFO:", i)
print("WARN:", w)
print("ERROR:", e)
