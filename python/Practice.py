s = "Django"

print(s[:1])
print(s[5:])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

l = [3,4,[1,4,'hello']]
l[2][2] = "goodbye"
print(l[2][2])

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
mylist = set(mylist)
print(mylist)

age = 4
name = "Sammy"
x = "Hello my dog name is {name} and he is {age} years old".format(age = 4,name = "Sammy")
print(x)