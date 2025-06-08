# What is the difference between global and local scope?

# 1. Local Scope
# Variables declared inside a function.

# They are only accessible within that function.

# They are created when the function is called and destroyed when the function exits.

def my_func():
    x=19
    print(x)
my_func()

# 2. Global Scope

# Variables declared outside all functions.

# They are accessible from anywhere in the code, including inside functions (if not redefined).

x = 5  # Global variable

def my_func():
    print(x)  # Accessing global variable

my_func()
print(x)  # Also works outside the function
