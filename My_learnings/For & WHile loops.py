# For loops are used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.
# Example of a for loop
fruits = ("apple", "banana", "cherry", "date", "elderberry")
for fruit in fruits:
    print(fruit)
# In this example, the for loop iterates over each item in the fruits list and prints it. 
# The variable fruit takes on the value of each item in the list during each iteration of the loop.

# While loops are used to execute a block of code repeatedly as long as a certain condition is true.
# Example of a while loop

Count = 1
while Count < 6:
    print(Count)
    Count += 1
print("Blast off!")
# In this example, the while loop continues to execute as long as the variable Count is less than 6.
# Inside the loop, it prints the current value of Count and then increments it by 1.
# Once Count reaches 6, the loop condition becomes false, and the loop terminates, printing "Blast off!".

Countdown = 5
while Countdown > 0:
    print(Countdown)
    Countdown -= 1
print("Blast off!")
# In this example, the while loop continues to execute as long as the variable Countdown is greater than 0.
# Inside the loop, it prints the current value of Countdown and then decrements it by 1.
# Once Countdown reaches 0 , the loop condition becomes false, and the loop terminates, printing "Blast off!".

#loop with a number range
for number in range(1, 6):
    print(number)
# In this example, the for loop uses the range() function to generate a sequence of numbers from 1 to 5 (the end value is exclusive).
# The loop iterates over each number in the range and prints it.

