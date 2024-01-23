fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
req_op = list([fruit.upper() for fruit in fruits])
print(req_op)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
lst = list([fruit for fruit in fruits if len(fruit)>5])
print("fruit with more than 5 characters", lst)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
lst = list([fruit for fruit in fruits if len(fruit)==5])
print("fruit with exactly 5 characters", lst)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
lst = list([fruit for fruit in fruits if len(fruit)<5])
print("fruit with less than 5 characters", lst)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
lst = list([len(fruit) for fruit in fruits ])
print("the number of characters in each fruit", lst)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print("list of only the fruits that contain the letter 'a' ",fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = list([num for num in numbers if num%2==0])
print("the even numbers",even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = list([num for num in numbers if num%2!=0])
print("the odd numbers",odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = list([num for num in numbers if num>0])
print("the positive numbers",positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = list([num for num in numbers if num<0])
print("the negative numbers",negative_numbers)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = list([num**2 for num in numbers])
print("the squared numbers",numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = list([num for num in numbers if num<0 and num%2!=0])
print("the numbers that are both odd and negative", odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = list([num+5 for num in numbers])
print("list containing each number plus five", numbers_plus_5)
