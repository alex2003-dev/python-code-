import csv

def read_grades(filename):
    grades = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)  # если разделитель другой — скажи
            next(reader)  # пропускаем заголовок
            for row in reader:
                print("Read row:", row)
                if len(row) < 2:
                    print("Skipped row (not enough columns):", row)
                    continue
                try:
                    grade = float(row[1])
                    grades.append(grade)
                except ValueError:
                    print("Skipped row (not a number):", row)
    except FileNotFoundError:
        print("File not found:", filename)
    return grades

file = 'names.csv'
grades = read_grades(file)
print("Grades collected:", grades)

