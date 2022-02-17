# Python does not require a key word to declare a value as a variable.
first_name = "Sebastian"
print(first_name)

# Strings can be set with single or double quotes.
last_name = 'Banks'
print(last_name)

# Note, like JavaScript, Python variables can change type.
last_name = 69
print(last_name)
print(f"Hello, {first_name}")
# Use the type function to see the type of a given value.

age = 21
bank_account = 400.35
loves_code = True

print(type(age))

# Comments are set with the octothorpe (pound, hashtag).

# If Statements

if age >= 18:
  print("Congrats you're an adult!")
elif age >= 13:
  print("Sorry, you're a teenager...")
else:
  print("Lucky, you're still a kid")


# If-else Statements



#If-elif-else


## Note: above code would break if you had two blank lines in between code.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For-In-Loop (similar to JavaScript for-loop)

for num in numbers:
  print(num)

# Another example of for-in loop, also demonstrating creation of array and use of a built in method, just like you would do in JavaScript.
open_file = open("FinalGrades.csv")

# for grade in open_file:
#   print(grade)

# for row in open_file:
#   row = row.split(',')
#   for value in row:
#     if value.startswith('J'):
#       print(value)

total_a = 0
total_b = 0
total_c = 0

for row in open_file:
  item = row.rstrip('\n').split(',')
  for value in item:
    if value == "A":
      total_a += 1
    elif value == "B":
      total_b += 1
    elif value == "C":
      total_c += 1

print(f"A: {total_a}")
print(f"B: {total_b}")
print(f"C: {total_c}")
    



open_file.close()
# Handling Data with Python


# A more complicated look at what we can do with the data.



