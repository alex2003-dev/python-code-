<<<<<<< HEAD
text = input("Enter text: ")
text = text.lower()
text = text.replace('.', ' ')
text = text.replace(',', ' ')
text = text.replace('!', ' ')
text = text.replace('?', ' ')

=======
<<<<<<< HEAD

=======
text = input("Enter text: ")
text = text.lower()
text = text.replace('.', ' ')
text = text.replace(',', ' ')
text = text.replace('!', ' ')
text = text.replace('?', ' ')

>>>>>>> 460ef79 (conflict in test7.py)
stop_words = ["and", "the", "is", "in", "at", "to", "a", "of", "on", "for", "it", "with", "as", "was", "but"]

words = text.split()

word_counts = {}

for word in words:
    if word not in stop_words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

word_items = list(word_counts.items())

for i in range(len(word_items)):
    for j in range(i + 1, len(word_items)):
        if word_items[j][1] > word_items[i][1]:
            temp = word_items[i]
            word_items[i] = word_items[j]
            word_items[j] = temp

print("Top 10 words:")
count = 0
for item in word_items:
    print(item[0], ":", item[1])
    count = count + 1
    if count == 10:
<<<<<<< HEAD
        break
=======
        break
>>>>>>> f177cb9 (Word Frequency Analyzer)
>>>>>>> 460ef79 (conflict in test7.py)
