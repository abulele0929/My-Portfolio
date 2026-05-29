# default arguments for functions: these are values that a function uses if no argument is provided for that parameter when the function is called.

#def greet(name, city="Cape Town"):
#    print(f"Hello, {name}, welcome to {city}!")

#greet("Abulele")  # This will print: Hello, Abulele, welcome to Cape Town!
#greet("Abulele", "Johanneburg")  # This will print: Hello, Abulele, welcome to Johanneburg!

# RETURNING VALUES: functions can return values, which means they can give back a result after performing their task.

#def full_name(first_name, last_name):
#    return f"{first_name} {last_name}"

#name = full_name("Abulele", "Madikizela")
#print(name)  # This will print: Abulele Madikizela
#print(f'Welcome to my portfolio, {name}!')  # This will print: Welcome to my portfolio, Abulele Madikizela!

# RETURN sends the results back so you can store it, print it or pass it into another function.

def portfolio_summary(full_name, job_title, city, available= False):
    status = "Open to work" if available else "Not available for work"
    return f"{full_name} - {job_title} | {city} | {status}."

portfolio = portfolio_summary("Abulele Madikizela", "Python Developer", "Cape Town")
print(portfolio)