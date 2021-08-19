# file = open("Practice.py", 'r')

# for i in file:
#     print(i)

# print("Hello)

# print(mylist)
# try:
#      f = open("tesy.py", 'w')
#      f.write("Test write to simple text!")

# except:
#     print("Error: Could not find file or read data!")
# else:
#     print("SUCCESS!")
#     f.close()
# print("Hello World")
try:
     f = open("tesy.py", 'w')
     f.write("Test write to simple text!")

except:
    print("Error: Could not find file or read data!")
finally:
    print("I Always Work No Matter What!")
