#Mini calculator project (Menu driven using function and conditional statements)

def add(a,b):
    res=a+b
    print('Addition is: ',res)

def sub(a,b):
    res=a-b
    print('Difference is: ',res)

def mul(a,b):
    res=a*b
    print('Product is', res)

def div(a,b):
    res=a/b
    print('Division is: ',res)

def f_div(a,b):
    res=a//b
    print(' Floor Division is: ',res)

def mod(a,b):
    res=a%b
    print('Modulous is: ',res)

def exp(a,b):
    res=a**b
    print('power is: ',res)

    
while True:

    a=int(input('Enter First number: '))
    b=int(input('Enter Second number: '))

    ch= int(input('***** MENU *****'\
                  '\n1. Addition'\
                  '\n2. Subtraction'\
                  '\n3. Multiplication'\
                  '\n4. Division'\
                  '\n5. Floor Division'\
                  '\n6. Modulous'\
                  '\n7. Exponential'\
                  '\n8. BREAK'\
                  '\n9. Enter Your Choice: '))

    if ch==1:
        add(a,b)
    elif ch==2:
        sub(a,b)
    elif ch==3:
        mul(a,b)
    elif ch==4:
        div(a,b)
    elif ch==5:
        f_div(a,b)
    elif ch==6:
        mod(a,b)
    elif ch==7:
        exp(a,b)
    elif ch==8:
        break
    else:
        print('Invalid input')
          
