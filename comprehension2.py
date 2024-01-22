# 1. Given a list of numbers, remove all odd numbers from the list:

numbers = [3,5,45,97,32,22,10,19,39,43]
odd_no_list = list([num for num in numbers if num % 2 != 0])
print(odd_no_list)

# 2. Find all of the numbers from 1-1000 that are divisible by 7
nub_div_by_7 = list([ n for n in range(1,1001) if n%7 == 0 ])
print(nub_div_by_7)

# 3. Count the number of spaces in a string . 
s = 'aa bb cc'
print(s.count(" "))
num_of_spaces = len(list([i for i in s if i==" "]))
print(num_of_spaces)

# 4. Find all of the words in a string that are less than 4 letters 
l = ['pppp', 'aaa', 'bbb', 'cccc', 'ddd']
req_op = list([i for i in l if len(i)<4])
print(req_op)

# 5. Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
req_op = list([i for i in range(1200,2000,130)])
print(req_op)

# 6. Use list comprehension to construct a new list but add 6 to each item. lst1=[44,54,64,74,104]
lst1=[44,54,64,74,104]
lst2 = list([i+6 for i in lst1])
print(lst2)

# 7. Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.  lst1=[2, 4, 6, 8, 10, 12, 14]
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2 = list([x for x in lst1 if x**2>50])
print(lst2)


# 8. Given dictionary is consisted of vehicles and their weights in kilograms. 
# Construct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
lst = list([(k.upper(),v)for k,v in dict.items() if v<5000])
print(lst)

# 9.     l = ['m', 'na', 'i','ke']
#        l1 = ['y','me','s','lly']
# output:
# l = ['my','name','is','kelly']
l = ['m', 'na', 'i','ke']
l1 = ['y','me','s','lly']
output = list([i+j for i,j in zip(l,l1)])
print(output)

# 10.  l = [1,2,3,4]
#     l1 = ['one','two','three','four']
# 	d = {1:'one', 2:'two', 3:'Three', 4:'Four'}
l = [1,2,3,4]
l1 = ['one','two','three','four']
d = {k:v.title() for k,v in zip(l,l1)}
print(d)

# 11.     state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# 	capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
# Output Dictionary using for loop: {'Gujarat': 'Gandhinagar',
#                                    'Maharashtra': 'Mumbai', 
#                                    'Rajasthan': 'Jaipur'}

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
d={}
for key, value in zip(state,capital):
    d[key]=value
print(d)
