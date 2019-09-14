number=int(input('Give me a number:'))
re= number % 2
re4=number % 4

if re > 0:
      print (str(number) + ' is an odd number.')
if re4==0:
    print (str(number)+' is a multiple of 4')
if re==0:
      print (str(number) + ' is an even number.')
