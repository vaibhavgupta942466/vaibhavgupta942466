# import packages as mm

# mm.func_in_module()

import packages

print("Top Level test.py")

packages.func()

if __name__ == '__main__':
    print("Test.py being run directly")

else:
    print("Test.py is being imported")

