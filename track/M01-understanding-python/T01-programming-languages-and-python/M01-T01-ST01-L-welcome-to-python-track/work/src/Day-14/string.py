s1 = ' '
res = bool(s1)
print(res)


# methords in strings are ----
# id----will give the unique address of the string

s1 = "Python"
s2 = "Python"

print(s1, id(s1))
print(s2, id(s2))
print(s1 is s2)
print(s1 == s2)


# upper()	Converts all letters to uppercase
# lower()	Converts all letters to lowercase
# capitalize()	Makes only the first character uppercase
# title()	Makes the first letter of every word uppercase
# swapcase()	Changes uppercase to lowercase and lowercase to uppercase

s = "kodNest Technologies 123 "

print("Original String:", s)

print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())


# Searching & counting
print("find('Tech'):", s.find("Tech"))
print("count('o'):", s.count("o"))

# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))

# Start & End check
print("startswith(' kod'):", s.startswith(" kod"))
print("endswith('123 '):", s.endswith("123 "))

# Split & Join
words = s.split()
print("split():", words)
print("join():", "_".join(words))

# Strip spaces
print("strip():", s.strip())
print("lstrip():", s.lstrip())
print("rstrip():", s.rstrip())

# Checking methods
print("isalpha():", s.isalpha())
print("isdigit():", s.isdigit())
print("isalnum():", s.isalnum())

# Length
print("Length of string:", len(s))

