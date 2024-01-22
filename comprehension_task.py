# List Comprehnsion : An easy way of creating list objects.
# Syntax:  l = [expression for each_element in sequence if condition]
## Nested for loop in comprehension: 
# result = [expression for outer_variable in outer_sequence for inner_variable in inner_sequence]


# 1. Strings to Integers
# You are given a list of numeric strings.

# lis = ["1", "2", "3", "4", "5"]
# Write a list comprehension to convert all the string numbers to integers. Assume every element in the list can be converted into integers without error. Expected output:

# [1, 2, 3, 4, 5]

lis = ["1", "2", "3", "4", "5"]
list_of_integers = [int(x) for x in lis]
print(list_of_integers)

# 2. Numbers greater than 10
# You are given a list of integers.

# lis = [1,5,13,4,16,7]
# Write a list comprehension to extract all integers in this list that are greater than 10. Expected output:

# [13, 16]

lis = [1,5,13,4,16,7]
no_gt_10 = [x for x in lis if x > 10]
print(no_gt_10)

# 3. Greater than 10 AND divisible by 3
# You are given a list of integers.

# lis = [1,12,13,14,15,2,3]
# Write a list comprehension to extract all integers in this list that are greater than 10 AND that are divisible by 3. Expected output:

# [12, 15]

lis = [1,12,13,14,15,2,3]
required_op = [x for x in lis if x > 10 and x%3 == 0]
print(required_op)

# 4. Adding 1 to even numbers only
# You are given a list of integers.

# lis = [1,2,4,5,7]
# Write a list comprehension that adds 1 to even numbers but keeps odd numbers as they are.
#  Hint — use the ternary operator. Expected output:

# [1,3,5,5,7]

lis = [1,2,4,5,7]
expected_op = [x+1 if x%2==0 else x for x in lis ]
print(expected_op)

# 5. Numbers containing digit 1
# Write a list comprehension that returns all numbers between 1 and 100 (inclusive) that contains the digit 1. Expected output:

# [1,10,11,12,13,14,15,16,17,18,19,21,31,41,51,61,71,81,91,100]

expected_output = [x for x in range(1,101) if '1' in str(x) ]
print(expected_output)

# 6. Combining 2 lists
# You are given 2 lists of the same length — fruits and prices.

# fruits = ["apple", "orange", "pear"]
# prices = [4,5,6]
# Write a list comprehension to create a list of (fruit, price) tuples. Hint — use the zip function. Expected output:

# [("apple",4), ("orange",5), ("pear",6)]

fruits = ["apple", "orange", "pear"]
prices = [4,5,6]
expected_output = [x for x in zip(fruits,prices)]
print(expected_output)

# 7. Sorting dictionary keys and values
# You are given a dictionary containing fruits and numbers.

# d = {"apple":5, "orange":2, "pear":7, "durian":6}
# Each number represents the price of the fruit. Write a list comprehension that sorts this dictionary by price.
#  Hint — use the sorted function. Expected output:

# [("orange",2), ("apple",5), ("durian",6), ("pear",7)]

d = {"apple":5, "orange":2, "pear":7, "durian":6}
new_li = list(d.items())
print(new_li)
expected_output = []
print(expected_output)


# 8. Combinations from 2 lists
# You are given 2 lists fruits and recipes.

# fruits = ["apple", "orange", "pear"]
# recipes = ["pie", "juice"]
# Write a list comprehension that generates all combinations across fruits and recipes. 
# Hint — you need a nested for loop. Expected output:

# [
#     ("apple", "pie"), ("apple", "juice"),
#     ("orange", "pie"), ("orange", "juice"),
#     ("pear", "pie"), ("pear", "juice")
# ]
fruits = ["apple", "orange", "pear"]
recipes = ["pie", "juice"]
l=[]
for item in fruits:
    for recp in recipes:
        k=(item,recp)
        l.append(k)
print(l)
# using comprehension
li = [(f,r) for f in fruits for r in recipes]
print(li)


# 9. Unique combinations of 2 numbers that add up to a multiple of 3
# You are given 1 list of integers.

# lis = [1,6,2,4,7]
# Find all unique combinations of 2 numbers inside this list that add up to a multiple of 3. 
# Hint — once again, you need to use a nested for loop. Expected output:

# [(1,2), (2,4), (2,7)]
lis = [1,6,2,4,7]
l = []
for i in range(len(lis)-1):
    for j in range(i+1, len(lis)):
        if (lis[i]+lis[j]) % 3 ==0:
            k = (i,j)
            l.append(k)
print(l)
expected_op = [(i,j) for i in lis for j in lis if (i+j)%3 == 0]
print(expected_op)


# 10. Converting storage space to integers
# You are given a list of strings representing storage space.

# lis = ["128GB", "256GB", "512GB", "1TB"]
# Write a list comprehension to convert these storage spaces into integers (in terms of GB). Note — 1 TB is equal to 1024 GB. Assume that the list only contains the units GB and TB. Expected output:

# [128, 256, 512, 1024]

lis = ["128GB", "256GB", "512GB", "1TB"]
expected_op = [int(i[:-2:]) if(i.endswith('GB')) else(int(i[:-2:])*1024) for i in lis ]
print(expected_op)