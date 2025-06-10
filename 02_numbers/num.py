x = 2
y = 3
z = 4

a = x +( y * z)
print(a)

a = 'pappu'
b = a + 3
print(b)
# 💀 this code can return - TypeError: can only concatenate str (not "int") to str

a = 2.23
print(int(a))

b = 40
print(float(b))

print('pappu' + 'naskar')

a = (x+2,y*2)
print(a)

b = y % 2
print(b)

# read about repr(), str() , print()

print(1<2)
print(5.0 == 5.0)
print(4.0 != 5.0)

print(x<y<z)
print(x<y and y<z)

print(1 == 2 <3)

import math
print(math.floor(3.5))
print(math.floor(-3.5))

print(math.trunc(2.8))
print(math.trunc(-2.8))

print((2+1j)*3)

Octal numbers

print(0o20)

hex numbers
print(0xFF)

Binary numbers
print(0b1000)

convert numbers

print(oct(64))
print(hex(64))
print(bin(64))

import random

print(random.random())
print(random.randint(0, 10))

l1 = ['lemon','masala','ginger','mint']
print(random.choice(l1))

print(random.shuffle(l1))
print(l1)
print(random.shuffle(l1))
print(l1)


print(0.1+0.1+0.4)
print(0.1+0.1+0.1-0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))


from fractions import Fraction
print(Fraction(2,7))


>>> setone = {1,2,3,4}
>>> setone
{1, 2, 3, 4}
>>> setone & {1, 3}
{1, 3}
>>> setone
{1, 2, 3, 4}
>>> setone - {1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>> type(true)
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    type(true)
         ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> True is 1
<python-input-7>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  True is 1
False
>>> True + 4
5
>>> 
