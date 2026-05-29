# Expressions inside f-strings are evaluated at runtime and then formatted using the __format__ protocol.
# You can put any expression directly inside the {}:

age = 22
print(f"In 5 years, I will be {age + 5} years old.")
print(f"Double my age is {age * 2}.")

# Formatting numbers with f-strings:
pi = 3.14159
print(f"Pi rounded to 2 decimal places is {pi:.2f}.")


#Multi-line f-strings: f-strings can also span multiple lines, which is useful for creating formatted text blocks. You can use triple quotes (""" or ''').
name = "Abu"
Job = "Python Developer"
City = "Cape Town"
skills = ("Python", "Flask", "HTML", "CSS")

summary = f"""
Name : {name}
Job : {Job}
City : {City}
Skills : {', '.join(skills)}
"""
print(summary)

def generate_bio(full_name, job, city, years_of_coding, skills):
    return f"""
=====================================
{full_name}
{job} | {city}
Years of coding: {years_of_coding}
Skills: {", ".join(skills)}
=====================================
"""

print(generate_bio("Abulele Madikizela", "Python Developer", "Cape Town", 1, ["Python", "Flask", "HTML", "CSS"]))

