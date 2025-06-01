# 1. Age Group Categorization(Classify a parson's age group Child(<13),Teenager(13-19),Adult(20-59),Senior(60+).)

age = 64

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")          


# 2. Movie Ticket Pricing
# Problem:Movie tickets are priced based on age:$12 for adults(18 and over),$8 for children. Everyone gets a $2 discount on Wednesday.

age = 25
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price=price-2

print("Ticket price for you is $",price)


# 3. Grade Calculator
# Assign a letter grade based on a student's score: A(90-100),B(80-89),C(70-79),D(60-69),F(below 60)

Score = 85

if Score >= 101:
    print("Please verify your grade again")
    exit()

if Score >= 90 :
    print("A")
  
elif Score  >= 80:
    print("B")
elif Score >= 70:
    print("C")
elif Score >=60:
    print("D")
else:
    print("F") 


# 4. Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe, or unripe based on its color.(e.g., Banana: Green- Unripe,
# Yellow- Ripe, Brown - Overripe)

fruit = "Banana"
color="Brown"

if fruit == "Apple":
    if color=="Green":
        print("Unripe")  
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")        
elif fruit == "Banana":
    if color=="Green":
        print("Unripe")  
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe") 
else:
    print("please enter the fruit name")    


# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny-Go for walk, Rainy - Read a book,Snowy-Build a Snowman).

Weather = "Sunny"

if Weather=="Sunny":
    activity="Go for walk"
elif Weather=="Rainy":
    activity="Read a book"
elif Weather=="Snowy":
    activity="build a Snowman"      

print(activity)


# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g. <3km:Walk,3-15 km:Bike,>15 km:Car)
 
distance = int(input("Enter distance: "))
if distance<3:
    transport = "Walk"
elif distance <= 15:
    transport="Bike"
else:
    transport="Car"        


print("AI recommends you the transport of:",transport)


# 7. Coffee Customization
# Problem: Customize a coffee order: "Small","Medium",or "Large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra short "
else:
    coffee = order_size + "coffee"

print("order: ", coffee)

# 8. Password Strength Checker
# Problem: Check if a password is "Weak","Medium",or "Strong" . Criteria: <6 chars (Weak), 6-10 chars (Medium), >10chars (strong).

user_password = input("Enter your password hear : ")
password_len = len(user_password)

if password_len < 6 :
    password_type = "Weak"
elif password_len <= 10:
    password_type = "Medium"
else:
    password_type="Strong"

print(password_type)

# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter year : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print (year ,"is a leap year") 
else :
    print(year, "is not leap year")    

# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

type_of_pet = str(input("enter your pet type : "))
age = int(input("Enter your pet age : "))

if type_of_pet.lower() == "dog" and age < 2 :
    food = "Puppy food"
elif type_of_pet.lower() == "cat" and age > 5:
    food = "Senior cat food"    
else : 
    food = "you enter wrong pet" 

print(food)

