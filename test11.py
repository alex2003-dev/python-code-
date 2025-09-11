def is_valid_email(s: str) -> bool:
    return '@' in s and '.' in s.split('@')[-1] and s.count('@') == 1

print(is_valid_email("justsanchez241@gmail..com"))
print(is_valid_email("stepa180877@gmail.com"))
print(is_valid_email("stepa2007@bigmir.net"))
