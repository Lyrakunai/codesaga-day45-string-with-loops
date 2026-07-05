# ==========================
# Codesaga Day 45
# String with Loops
# Practice File
# ==========================


# --------------------------
# 1. Loop through a string
# --------------------------

text = "Python"

for char in text:
    print(char)


# --------------------------
# 2. Count Alphabets
# --------------------------

text = "Python123"

letters = 0

for char in text:
    if char.isalpha():
        letters += 1

print("Letters :", letters)


# --------------------------
# 3. Count Digits
# --------------------------

text = "Python123"

digits = 0

for char in text:
    if char.isdigit():
        digits += 1

print("Digits :", digits)


# --------------------------
# 4. Count Uppercase
# --------------------------

text = "PyTHon"

upper = 0

for char in text:
    if char.isupper():
        upper += 1

print("Uppercase :", upper)


# --------------------------
# 5. Count Lowercase
# --------------------------

text = "PyTHon"

lower = 0

for char in text:
    if char.islower():
        lower += 1

print("Lowercase :", lower)


# --------------------------
# 6. Count Spaces
# --------------------------

text = "Hello Python World"

spaces = 0

for char in text:
    if char.isspace():
        spaces += 1

print("Spaces :", spaces)


# --------------------------
# 7. Check Alphabet Exists
# --------------------------

text = "123A45"

has_alpha = False

for char in text:
    if char.isalpha():
        has_alpha = True

print("Alphabet Present :", has_alpha)


# --------------------------
# 8. Check Digit Exists
# --------------------------

text = "Python7"

has_digit = False

for char in text:
    if char.isdigit():
        has_digit = True

print("Digit Present :", has_digit)


# --------------------------
# 9. Password Check
# --------------------------

password = "Abc123@"

has_upper = False
has_lower = False
has_digit = False
has_at = False

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    elif char == "@":
        has_at = True

print(has_upper)
print(has_lower)
print(has_digit)
print(has_at)


# --------------------------
# 10. PIN Validation
# Only Digits Allowed
# --------------------------

pin = "1234"

status = "Valid"

for char in pin:

    if not char.isdigit():
        status = "Invalid"

print(status)


# --------------------------
# 11. Streak count
# --------------------------

text = "Hello.....World"

dot_count = 0

for char in text:

    if char == ".":
        dot_count += 1
    else:
        dot_count = 0
    if dot_count >= 3:
        print("spam")

# --------------------------
# 12. Consecutive Underscore
# --------------------------

username = "user___name"

previous = ""

status = "Valid"

for char in username:

    if previous == "_" and char == "_":
        status = "Invalid"

    previous = char

print(status)


# --------------------------
# 13. Special Character Logic
# --------------------------

text = "Python@123"

special = 0

for char in text:

    if (
        not char.isalpha()
        and not char.isdigit()
        and not char.isspace()
        and char != "_"
    ):
        special += 1

print("Special Characters :", special)