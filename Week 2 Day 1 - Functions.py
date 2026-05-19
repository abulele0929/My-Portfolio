##functions:
# are reusable pieces of code that perform a specific task. 
# they let you wrap code in a label and reuse it anywhere, as many times as you want.
# Think of it like this — instead of writing the same instructions every time, you write them once, give them a name, and just call that name whenever you need them.
# defining a function

#def greet():
#    print("Hello, welcome to the world of functions!")

# def tells Python you're defining a function
# greet is the name you give it
# The indented block is what runs when you call it

#greet()  # calling the function to execute its code

# this will print: Hello, welcome to the world of functions!


#functions with parameters:
# these are like placeholders that allow you to pass information into the function when you call it.
# For example:

#def greet(name):
#    print(f"Hello, {name}! Welcome to the world of functions!")

#greet("Abulele") # This will print: Hello, Abulele! Welcome to the world of functions!

# functions can also return values, which means they can give back a result after performing their task.
# For example:

#def add(a, b):
#    return a + b   

#result = add(5, 3)  # This will return 8
#print(result)  # This will print: 8

# to explain this, the add function takes two parameters, a and b, adds them together, and returns the result.
# When we call add(5, 3), it computes 5 + 3 and gives us back 8, which we then print.

def introduce(name, job, city):
    print(f"Hi, I'm {name}, a {job} living in {city}.")
    
intro = introduce("Abulele", "Python Developer", "Cape Town")
print(intro)  # This will print: Hi, I'm Abulele, a Python Developer living in Cape Town.
