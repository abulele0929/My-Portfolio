# slicing = a range of characters in a string, specified by a start and end index
# indexing [] or slice() function
# [start:stop:step]

#Indexing

full_name = "Abulele Madikizela"

First_name = full_name[0:7] # Output: "Abulele". Extracts characters from index 0 to index 6 (7 is exclusive).
Last_name = full_name[8:18] # Output: "Madikizela". Extracts characters from index 8 to index 17 (18 is exclusive).
Nick_name = full_name[:18:3] # Output: "Aeake". Extracts characters from the beginning to index 17, taking every third character.

print(First_name)
print(Last_name)
print(Nick_name)

# Slicing

website = "https://www.google.com"

slice = slice(12, -4) # Output: "google". Extracts characters from index 12 to index -5 (the last 4 characters are excluded).
print(website[slice])