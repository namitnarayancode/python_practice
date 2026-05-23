import random


class Hat:
    houses=["griffindor","hufflepuff","ravenclaw","slytherin"]
    
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(name , "is in",house)


Hat.sort("Harry")