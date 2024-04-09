# Replace the first or first N characters in a String in Python

my_str = 'bobbyhadz.com'

# ✅ replace first character in a string

new_str = '_' + my_str[1:]
print(new_str)  # 👉️ _obbyhadz.com