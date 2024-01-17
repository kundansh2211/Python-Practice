# Mini bank application using return statement

balance=1000

def deposit(amt):
    bal=balance+amt
    return bal

def withdraw(amt):
    
    if amt<=balance:
        bal=balance-amt
        return bal
    else:
        print('Insufficient fund')

def check_balance():
    print('Your account balance is',balance)


while True:
    ch=int(input('***** Menu *****'\
          '\n1. DEPOSIT'\
          '\n2. WITHDRAW'\
          '\n3. CHECK BALANCE'\
          '\n4. EXIT'\
          '\nEnter your choice: '))

    if ch==1:
        amt=float(input('Enter amounr to deposite: '))
        balance=deposit(amt)   # overriding the updeted balance 

    elif ch==2:
        amt=float(input('Enter amunt to withdraw: '))
        balance=withdraw(amt)

    elif ch==3:
        check_balance()

    elif ch==4:
        break

    else:
        print('Enter valid input')
