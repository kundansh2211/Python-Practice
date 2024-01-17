## Calculator using return and match_case

def add(a,b):
    res=a+b
    return res

def sub(a,b):
    res=a-b
    return res

def mul(a,b):
    res=a*b
    return res

def div(a,b):
    res=a/b
    return res

while True:
    a=int(input('Enter First Number: '))
    b=int(input('Enter Second Number: '))

    ch=int(input('**** MENU ****'\
                 '\n1. addition'\
                 '\n2. subtraction'\
                 '\n3. multiplication'\
                 '\n4. division'\
                 '\n5. EXIT'\
                 '\nEnter your choice: '))
    match ch:
        case 1:
            print('Addition is: ',add(a,b))
        case 2:
            print('Difference is: ',sub(a,b))
        case 3:
            print('Product is: ',mul(a,b))
        case 4:
            print('Division is: ',div(a,b))
        case 5:
            break
        case _:
            print('Enter Valid Input')

        
