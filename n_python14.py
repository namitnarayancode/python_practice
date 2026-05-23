import re
email = input("Enter your email: ").strip()
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.gmail\.com$", email):
if re.search(r"^\w+@\w+gmail\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("valid email")
else:    
    print("Invalid email")
