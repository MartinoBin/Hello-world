import random

List_a=random.sample(range(30),10)
List_b=random.sample(range(30),10)
List_c=[]

print ('Generate two lists randomly from 0 to 30, 10 numbers:')
print (List_a)
print (List_b)

for x in List_a:
    if x in List_b:
        List_c.append(x)

print ('The common elements are:')
print (List_c)












































