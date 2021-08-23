# def func_in_module():
#     print("I am inside the module")


def func():
    print("Func() in packages.py")

print("Top Level Packages.py")

if __name__ == '__main__':
    print('One.py is being run directly')
else:
    print("Packeges.py has benn imported")