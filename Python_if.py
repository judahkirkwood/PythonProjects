

num1 = 12

if isinstance(num1, int):
    key = bool(num1 % 2 == 0)

    if num1 == 12:
        if key:
            print ('Num1 is equal to Twelve and has the key')
        else:
            print ('Num1 is equal to Twelve and does not have the key')
    elif num1 < 12:
        print ('Num1 is less than Twelve')
    else:
        print ('Num1 is not equal to Twelve')
else:
    print ('Num1 is not an integer')
    
