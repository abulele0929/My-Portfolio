# String methods in Python are built-in functions that allow you to manipulate and work with strings. Here are some commonly used string methods:

#name = "abulele madikizela"

#print(name.upper())          # ABULELE MADIKIZELA
#print(name.lower())          # abulele madikizela
#print(name.title())          # Abulele Madikizela
#print(name.replace("a", "o")) # obuleleModikilzelo
#print(len(name))             # counts the characters

#bio = "i am a python developer based in cape town "
#print(bio.strip()) # removes extra spaces from the beginning and end of the string
#print(bio.strip().title()) # removes extra spaces and converts the first letter of each word to uppercase
#print(bio.strip().title().replace("Python", "Python🐍")) 

skills = "Python, Flask, HTML, CSS"

skills_list = skills.split(", ")
print(skills_list)

for skill in skills_list:
    print(f"I know {skill}")

skills = ("Python", "Flask", "HTML", "CSS")
print(f"My skills are: {', '.join(skills)}")