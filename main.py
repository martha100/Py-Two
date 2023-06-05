class Fruit:
    # this a constructor
    def __init__(self, colour, shape, size, taste):
        self.colour = colour
        self.shape = shape
        self.size = size
        self.taste = taste


class Car:
    def __init__(self,model, reg_no, colour, price):
        self.model = model
        self.reg_no = reg_no
        self.colour = colour
        self.price = price

    def brake(self):
        print("Yeah, I can brake")

    def accelerate(self):
        print("Yeah, I can accelerate")

class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print("You registerd with email", self.email, "and password")

    def login(self):
        # let's assume the user had already registered
        if self.email =="example@gmail.com" and self.password =="123":
           print("you logged in successfully")
        else:
            print("Wrong username or password")


class Teacher(Student):
    def suspend_student(self):
        print("Yeah, I can suspend a student")

    def submit_results(self):
        print("Yeah, I can submit results")

class Principal(Teacher):
    def suspend_teacher(self):
        print("Yeah, I can suspend a teacher")

    def schedule_meeting(self):
        print("Yeah, I can schedule a meeting")