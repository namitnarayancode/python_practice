class Student:
    def __init__(self,name,house):
        # if not name:
        #     raise ValueError("missing name")
        # if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
        #     raise ValueError("Invalid house")
        self.name= name
        self.house= house
        # self.patronus= patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("missing name")
        self._name= name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house= house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
    
    # def charm(self):
    #     match self.patronus:
    #         case "stag":
    #             return "🐎"
    #         case "otter":
    #             return "🦦"
    #         case "jack russell terrier":
    #             return "🐕"
    #         case _:
    #             return "🪶"



def main():
    student = Student.get()
    # student.house = "hrvjhyurfbyib"
    print(student)
    # print("Expectro Patronum!")
    # print(student.charm())
    # print(f"{student.name} is from {student.house}")
    # print(f"{student.name}'s patronus is {student.patronus}")
    # print(f"{student['name']} from {student['house']}")
    # name,house = get_student()
    # print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# def get_student():
#     return Student(input("Name: "),input("House: "))
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student
    # name= input("Name: ")
    # house= input("House: ")
    # # return name,house
    # return (name,house)
    # return {"name":input("Name: "),"house":input("House: ")}


if __name__ == "__main__":
    main()
