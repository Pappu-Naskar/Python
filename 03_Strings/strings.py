chai = "Lemon Chai"
print(chai)
print(type(chai))


 string sliceing

chai = "Masala Chai"
chai = "  Masala Chai   "
first_chr = chai[0]
# print(first_chr)
slice_chai = chai[0 : 6]
print(slice_chai)
number_list = "0123456789"
print(number_list[:])
print(number_list[3:])
print(number_list[:7])
print(number_list[:7:2])
print(number_list[0:7:2])

Python Method

print(chai)
print(chai.lower())
print(chai.upper())
print(chai.strip())

chai = "Lemon Chai"
print(chai.replace("Lemon","Ginger"))

chai = "Lemon , Ginger, Masala , Mint"
print(chai.split(", "))

chai = "Masala Chai"
print(chai.find("Chai"))

chai = "Masla Chai Chai Chai"
print(chai.count("Chai"))


chai_type = "Masala"
quantity = 2
order = "I Ordered {} cups of {} chai"

print(order.format(quantity,chai_type))

chai_variety = ["Lemon","Masala","Ginger"]
print(chai_variety)
print(", ".join(chai_variety))

chai = "Masala Chai"
print(len(chai))

for letter in chai:
    print(letter)

chai = "He said , \" Masala chai is awesome\" "
print(chai)

chai = "Masla\nChai"
chai = r"Masala\nChai"
print(chai)

path = r"c:\user\pwd"
print(path)

chai = "Masala Chai"
print("Masala" in chai)
