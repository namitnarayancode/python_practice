import csv
# Now append data
# for i in range(3):
#     name = input("Enter your name: ")
#     home = input("Enter your home: ")

#     with open("n_python12.csv", "a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([name,home])

name = input("Enter your name: ")
home = input("Enter your home: ")

with open("n_python12.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})



