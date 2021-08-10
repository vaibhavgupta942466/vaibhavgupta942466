print("Hello World")
print(2+10*10+3)
a=5
print(a+a)
a=a*5
print(a)

my_income = 100
tax_rate = 0.1 # 10%
my_taxes = my_income*tax_rate
print(my_taxes)

my_string = "abcdefg"
print(my_string[-2])
print(my_string[2:]) #slicing
print(my_string[:2])
print(my_string[1:6])

print(my_string[:])
print(my_string[::1])
print(my_string[::2])

x = my_string.upper()
print(x)

y = my_string.lower()
print(y)

z = my_string.capitalize()
print(z)

x = "My Name is vaibhav gupta i am spliting"
print(x.split())
print(x.split("a"))

x = "Insert anothr string here: {}".format("insert me!")
print(x)

x = "Item one: {} Item Two: {}".format('dog','cat')
print(x)

x = "Item one: {y} Item Two: {x}".format(x = 'dog',y = 'cat')
print(x)
