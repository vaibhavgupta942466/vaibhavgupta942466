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

mylist = [1,2,3]
anotherlist = ["Vaibhav",1,2,3,4,23,1.5,True,"asdf",[1,2,3]]

print(mylist)
print(anotherlist)
print(len(anotherlist))
print(anotherlist[3:])
print(anotherlist[:3])
anotherlist[0] = 'Pooja'
print(anotherlist)
mylist.append('Hello')
print(mylist)
mylist.extend(['a','b','c'])
print(mylist)
lastitem = mylist.pop(2)
print(mylist)
print(lastitem)
mylist.reverse()
print(mylist)
seclist = [32,23,45,12,1,0]
seclist.sort()
print(seclist)
anotherlist = ["Vaibhav",1,2,3,4,23,1.5,True,"asdf",[1,2,3]]
print(anotherlist[9])
print(anotherlist[9][2])

twoDarray = [[1,2,3],[4,5,6],[7,8,9]]
#LIST COMPREHENSION
first_col = [row[0] for row in twoDarray]
print(first_col)

my_stuff = {
    "key1": "Value",
    "key2": "VAlue2",
    "key3": {"key4": [1,2,3]}
}
print(my_stuff["key2"])
my_stuff["key2"] = "2nd Value"
print(my_stuff["key2"])
print(my_stuff)
print(my_stuff["key3"]['key4'][2])

t = (1,2,3)
print(t[0])

t = ('a',True,1,4)
print(t[1])

# t[0] = "b"
print(t)

x = set()

x.add("a")
x.add(1)

print(x)


if 1>2:
    print('Hello')
else:
    print('last')

seq = [1,2,3,4,5,6]
for item in seq:
    print(item)

mypairs = [(1,2),(3,4),(5,6)]
for tup1,tup2 in mypairs:
    # print(item)
    print(tup1)
    print(tup2)

i = 1
while i<5:
    print("i is : {}".format(i))
    i= i+1

x = [1,2,3,4,5]
# out = []
# for num in x:
#     out.append(num**2)
# print(out)

out = [num**2 for num in x]
print(out)

def my_func(a=1):
    """
    THIS IS THE DOCSTRING
    
    """
    print("My First Function")

my_func()

def hello():
    return("Hello")
result = hello()
print(result)

def addnum(num1,num2):
    return num1+num2
result = addnum(4,9)
print(result)

#Lambda Expression
mylist = [1,2,3,4,5,6,7,8]

# def even_bool(num):
#     return num%2  == 0

# evens = filter(even_bool(),mylist)

evens  = filter(lambda num:num%2 == 0,mylist)
print(list(evens))

