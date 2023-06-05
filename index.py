from main import Fruit, Car, Student, Teacher, Principal

# Start creating fruits out of the Fruit class
first_fruit = Fruit("Yellow", "Oval", "200g", "Sweet")
second_fruit = Fruit("Orange", "Spherical", "150g", "Sour")

print(first_fruit.colour)


first_Car = Car("BMW", "KDG002A", "Blue", "ksh 2,000,000")
second_Car = Car("Lexus", "KDK003A", "black", "Ksh 1,800,000")

second_Car.accelerate()
print(first_Car.price)



principal_one = Principal("Mrs. Esther", "esther@gmail.com", "123")

principal_one.register()