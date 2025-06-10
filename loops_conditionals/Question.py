# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_Count = 0

for num in numbers:
   if num > 0:
      positive_number_Count += 1
print("Final Count of positive number is : ", positive_number_Count)

--------------------------------------------------------------------------------------

# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 10
sum_even = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum_even+= 1

print("Sum of even number is  : ",sum_even)

--------------------------------------------------------------------------------------------
# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 3

for i in range(1,11):
    if i == 5:
        continue
    print(number, 'x',i, '=',number*i)

-----------------------------------------------------------------------------------------------------
# 4. Reverse a String
# Problem: Reverse a string using a loop.

input_str = "Python"
reversed_str = ''

for char in input_str:
    reversed_str = char + reversed_str 
print(reversed_str)

# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

str = input("enter value : ")
# str= "teeteracdacd"

for char in str:
    print(char)
    str.count(char)
    if str.count(char)==1:
        print("Char is : ",char)
        break

# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

fac_num = int(input("enter the number : "))

factorial = 1

while fac_num >=1:
    factorial = factorial * fac_num
    fac_num -= 1

print("Factorial : ",factorial)     

# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number=int( input("enter value between 1 - 10 : "))
    if 1<= number <= 10:
      print("Thanks")
      break
    else:
     print("Invalid number , try again")
  

# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("Enter the number : "))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)


# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate : ",item)
        break
    unique_item.add(item)

# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt",attempts +1,"wait_time",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts += 1

11. write a program to find the factors of a number.

n=int(input("enter a number which you want a factors: "))
print("The factors of",n,"are:")
for i in range(1,n+1):
    if n%i == 0:
        print(i)

# 12.Write a program to print inverted star pattern.
*****
****
***
**
*

n=int(input("enter the number of rows : "))
for i in range(n,0,-1):
    print((n-i)* '' +i * '*')


