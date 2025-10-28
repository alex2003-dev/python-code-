import re

text = "Hello,,,   this   is   my email:   test.email@@gmail.com!!  Call   me at +1 (234) - 567 - 8900..."

text = re.sub(r'[ ]+', ' ', text)
text = re.sub(r'[,!?.]{2,}', '.', text)
text = re.sub(r'\s*@+\s*', '@', text)
text = re.sub(r'\s*\.\s*', '.', text)
text = re.sub(r'\+?\s*\(?(\d{1,3})\)?[\s\-]*(\d{3})[\s\-]*(\d{3})[\s\-]*(\d{2,4})', r'+\1\2\3\4', text)

print(text)
