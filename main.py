class Student:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

studenti1 = Student("Blend", 17)

print("Name:",studenti1.get_name())

studenti1.set_name("Darsej")
print("Emri i perditsuar", studenti1.get_name())

print("Mosha ime eshte", studenti1.get_age())
studenti1.set_age(18)
print("Sot i mbusha plot", studenti1.get_age(), "vjet")