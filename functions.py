def wish():
    return 'Gm'

print(wish())  # while using the return statement we need to print the caller to see the result.

def name_wish(name):
    return f'{name}, Good Morning!'

print(name_wish('Kundan'))
print(name_wish('Deepak'))

def square_it(n):
    return n**2
print(square_it(6))

# return statement - used to return a value out of a function to its caller. by default it returns NONE>
def f1():
    print("Hello")

x = f1()
print(x)

# WAP to find factorial of a given number.
def factorial(n):
    res = 1

    while n > 1:
        res = res* n
        n = n-1
    return res
    
result = factorial(6)
print(result)

# Returning multiple values from a function.: Actually a single tuple containing multiple values is returned.

def calc(a,b):
    sum = a+b
    dif = a-b
    mul = a*b
    div = a/b
    return sum, dif, mul, div
t = calc(100,50)
print(t,type(t))
s, d, p, q = t
print(s, d, p, q)


# Lambda Function: lambda input_arguments: expression
s = lambda n: n*n
print(s(4))

sum = lambda x,y : x+y
print(sum(10,20))

c = lambda x,y: x if x>y else y
print(c(10,20))

bigger = lambda x,y,z: x if x>y and x>z else y if y>z else z
print(bigger(10,20,30))
print(bigger(2,4,6))


# filter function: used to filter elements out of given sequence based on function's requirement. [filter(fn,sequence)]
l = [1,2,3,4,5,6,7,8,9,10]
# filter the odd numbers from above list
l1 = list(filter(lambda n: n%2 != 0, l))
print(l1)

students = ['Kundan', 'Deepak', 'Aakash', 'Gaurav', 'Shubham', 'Sapna']
# filter the name from students whose name startswith S

startswithS = list(filter(lambda name: name[0]=='S', students))
print(startswithS) 

# # filter task
# take string input = 'abcdefghijklmn'
# 1. function that filters vowels ['a','e','i','o', 'u']

str = 'abcdefghijklmn'
vowels_list = list(filter(lambda x: x in 'aeiou', str))
print('vowels_list')

# take list input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2. a list contains both even and odd numbers # 2 programs 2 lists

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda n: n%2 == 0, list_1))
print(even_list)

odd_list = list(filter(lambda n: n%2 != 0, list_1))
print(odd_list)

# 3. ['cat', 'mat', 'bat', 'bbb', 'ccc', 'ddd'] # filter having 'a'
list_2 = ['cat', 'mat', 'bat', 'bbb', 'ccc', 'ddd']
list_having_a = list(filter(lambda x: 'a' in x,list_2))
print(list_having_a)


# 4. Using the filter function, find the values that are common to the two lists below
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
list_common_values = list(filter(lambda x: x in b ,a))
print(list_common_values)

# 5.myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
# output: ['madam', 'salas', 'PHP']

myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
output = list(filter(lambda s: s == s[::-1], myStrings))
print(output)


# Map Function:

# 1.Double all numbers using map and lambda # l = [20,30,40,50]
l = [20,30,40,50]
doubled_l = list(map(lambda x: x * 2,l)) 
print(doubled_l)

# 2.Add two lists using map and lambda #  
l1 = [10,20,30,40]
l2 = [1,2,3,4]
added_l1_l2 = list(map(lambda x,y: x + y,l1,l2))
print(added_l1_l2)

# 3.'Data Science Academy offers the best data analysis courses in Brazil'
# expected out:
# ['DATA', 'data', 4]
# ['SCIENCE', 'science', 7]
# ['ACADEMY', 'academy', 7]
# ['OFFERS', 'offers', 6]
# ['THE', 'the', 3]
# ['BEST', 'best', 4]
# ['DATA', 'data', 4]
# ['ANALYSIS', 'analysis', 8]
# ['COURSES', 'courses', 7]
# ['IN', 'in', 2]
# ['BRAZIL', 'brazil', 6] by using map

s = 'Data Science Academy offers the best data analysis courses in Brazil'
expected_output =list(map(lambda x : [x.upper(), x.lower(), len(x)],s.split()))
print(expected_output)
for x in expected_output:
    print(x)



# Reduce Function: 

# Find the sum of first 100 natural numbers.
from functools import reduce
sum_of_natural_no = reduce(lambda x,y: x+y,range(1,101))
print(sum_of_natural_no)


# 1. using reduce to compute sum of list [1,2,3,4,5]
list_1 = [1,2,3,4,5]
sum_l1 = reduce(lambda x,y: x+y,list_1)
print(sum_l1)

# 2. ['cat', 'mat', 'bat', 'bbb', 'ccc', 'ddd'] # reduce 'cat mat bat bbb ccc ddd'
l_s= ['cat', 'mat', 'bat', 'bbb', 'ccc', 'ddd']
reduced_op = reduce(lambda x,y: x+' '+y,l_s)
print(reduced_op)

# 3. using reduce multiply all elements of list [1,2,3,4,5]
l = [1,2,3,4,5]
reduced_opt = reduce(lambda x,y: x*y,l)
print(reduced_opt)