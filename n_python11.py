# with open("n_python11.txt", "a") as file:
#     name = input("Enter your name: ")
#     file.write(name + "\n")
# name=[]

# with open("n_python11.txt", "r") as file:
#     for line in file:
#         name.append(line.strip())

# for name in sorted(name):
#     print(f"Hello, {name}!")

# with open("n_python11.txt", "r") as file:
#     for line in sorted(file, reverse=True):
#         print(f"Hello, {line.strip()}!")
import csv
students = []
with open("n_python11.csv") as file:
    # names = []
    # for line in file:
    #     name, home = line.strip().split(",")
    #     student={"name": name, "home": home}
    #     students.append(student)
    # reader = csv.reader(file)
    # for name, home in reader:
    #     student={"name": name, "home": home}
    #     students.append(student)

    reader = csv.DictReader(file)
    for row in reader:
        student={"name": row["name"], "home": row["home"]}
        students.append(student)
        # print(f"{name} is in {home}.")
    #     names.append(name)
    # for name in sorted(names):
    #      print(f"Hello, {name}!")

# def get_name(student):
    # return student["name"]
# 
# for student in sorted(students,key=get_name,reverse=False):
    # print(f"{student['name']} is in {student['home']}.")


for student in sorted(students,key=lambda student: student["name"],reverse=False):
    print(f"{student['name']} is from {student['home']}.")