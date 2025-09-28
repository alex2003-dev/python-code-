 grades = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) 
            next(reader) 
            reader = csv.reader(csvfile)  
            next(reader)  
            reader = csv.reader(csvfile) 
            next(reader)  
            for row in reader:
                print("Read row:", row)
                if len(row) < 2: