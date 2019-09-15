num = int(input('give me a number:'))

check = int(input('give me a number to divide by:'))

if num % 4 == 0:
    print ( str(num) +' is a multiple of 4.')

elif num % 2 ==0:
    print (str(num) +' is an even number.')

else:
    print (str(num) +' is an odd number.')

if num % check ==0:
    print (str(num) +' can be divided by ' + str(check))

else:
    print (str(num) + ' can not be divided by '+ str(check))

    

    
