import re
name=input("Enter your name: ").strip()
if matches:= re.search(r"^(.+), *(.+)$",name):
    last,first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")


