# #Advantage of using multiple classes
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100

#     def get_grade(self):
#         return self.grade


# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()

#         return value / len(self.students)


# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)

# print(course.get_average_grade())


# #Advance object oriented
# #Inheritance in object oriented ... a class called dog and Cat
# class Pet:#Clas Generalization this is the parent class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")

#     def speak(self):
#         print("I don't know what to say")

# class Cat(Pet):#Class inheritance of the clas  pet which are the child class
#     def __init__(self, name, age, color):
#         super().__init__(name, age)#reference the super cat that is being inherited which is the class pet
#         self.color = color
#     def speak(self):
#         print("Meow")


# class Dog(Pet):#Class inheritance whci is a child to the parent class pet
#     def speak(self):
#         print("Bark")
# class Fish(Pet):
#     pass

# p = Pet("Tim", 19)
# p.speak()
# c = Cat("Bill", 34)
# c.speak()
# d = Dog("Jill", 25)
# d.speak
# f = Fish("Bubbles", 10)
# f.speak()
#


#class attributes which are specific to that class
# class Person:
#     number_of_people = 0 # this is a class attribute which is defined for the entire class it is the same for each instance of the class
#     GRAVITY = -9.8
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()

#     # claass methods
#     #use of a decolator
#     @classmethod #thiss method is to be called to the class itself
#     def number_of_people_(cls):
#         return cls.number_of_people
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("Tim")
# p2 = Person("Jill")
# print(Person.number_of_people_())
# print(Person.number_of_people)
# print(Person.GRAVITY)

# when you have a bunch of function you realy need to organize them in a class for usability
#we use static methods
class Math:
    @staticmethod#Not changing
    def add5(x):
        return x + 5
    
    def pr():
        print("run")
print(Math.add5(5))
print(Math.pr())    

