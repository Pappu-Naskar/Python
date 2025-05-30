# 1. Basic Class and Object
# Problem: Create a car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
       self. brand = brand
       self. model = model


       

my_car = Car("Toyota","Corolla")
print(my_car.brand)

my_new_car = Car("TAta","safari")
print(my_new_car.model)



# 2.Class Method and self
# Problem: Add a method to the car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
       self. brand = brand
       self. model = model

    def fullName(self):
        return f"{self.brand} {self.model}"   
    

my_new_car = Car("Tata","Safari")
print(my_new_car.fullName())


# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
       self. brand = brand
       self. model = model

    def fullName(self):
        return f"{self.brand} {self.model}"   


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","MOdel S","85KWh")
print(my_tesla.model)



# 4. Encapsulation
# Problem: Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
       self. __brand = brand
       self. model = model
    def get_brand(self):
        return self.__brand + "!" 
    def fullName(self):
        return f"{self.__brand} {self.model}"   


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","MOdel S","85KWh")
print(my_tesla.get_brand())


# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
       self. __brand = brand
       self. model = model
    def get_brand(self):
        return self.__brand + "!" 
    def fullName(self):
        return f"{self.__brand} {self.model}" 
    def fuel_type(self):
        return "Petrol or Diesel"  


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"      

my_tesla = ElectricCar("Tesla","MOdel S","85KWh")

print(my_tesla.fuel_type())

safari = Car("Tata","Safari")

print(safari.fuel_type())

# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:

    total_car = 0
 

    def __init__(self, brand, model):
       self. __brand = brand
       self. model = model
       Car.total_car += 1
    def get_brand(self):
        return self.__brand + "!" 
    def fullName(self):
        return f"{self.__brand} {self.model}" 
    def fuel_type(self):
        return "Petrol or Diesel"  


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge" 

# safari = Car("Tata","Safari")
# my_tesla = ElectricCar("Tesla","MOdel S","85KWh")
Car("Tata","safari")
Car("Tata","Nexon")

print(Car.total_car)

# 7. Static Method
# Problem: Add a static method to the car class that returns a general description of a car.

class Car:

    total_car = 0
 

    def __init__(self, brand, model):
       self. __brand = brand
       self. model = model
       Car.total_car += 1
    def get_brand(self):
        return self.__brand + "!" 
    def fullName(self):
        return f"{self.__brand} {self.model}" 
    def fuel_type(self):
        return "Petrol or Diesel"  
    @staticmethod
    def general_description():
        return "Cars are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge" 

safari = Car("Tata","Safari")
my_tesla = ElectricCar("Tesla","MOdel S","85KWh")
Car("Tata","safari")
Car("Tata","Nexon")

my_car = Car("Tata","Safari")
Car("Tata","Nexon")

print(my_car.general_description())
print(Car.general_description())

# 8. Property Decorators
# Problem: Use a property decorator in the car class to make the model attribute read-only.

class Car:

    total_car = 0
 

    def __init__(self, brand, model):
       self. __brand = brand
       self. __model = model
       Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!" 
    
    def fullName(self):
        return f"{self.__brand} {self.__model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel" 
     
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge" 
    

my_car = Car("Tata","Safari")
# my_car.model = "City"
Car("Tata","Nexon")

print(my_car.model)

# 9. Class Inheritance and isinstance() function.
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:

    total_car = 0
 

    def __init__(self, brand, model):
       self. __brand = brand
       self. __model = model
       Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!" 
    
    def fullName(self):
        return f"{self.__brand} {self.__model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel" 
     
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge" 
    

my_tesla = ElectricCar("Tesla","MOdel S","85KWh")

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))


# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.



class Car:

    total_car = 0
 

    def __init__(self, brand, model):
       self. __brand = brand
       self. __model = model
       Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!" 
    
    def fullName(self):
        return f"{self.__brand} {self.__model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel" 
     
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge" 
    

# my_tesla = ElectricCar("Tesla","MOdel S","85KWh")

class Battery:
    def battery_info(self):
        return "this is Battery"

class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricTwo("Tesla","Model s")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())