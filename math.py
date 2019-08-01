import random

array1=[]
for i in range(1,6):
    for j in range(10):
        array1.append("{} X {} =".format(str(i),str(j)))


def sum1(value, amount):
    if amount == 0:
        value = value + " ="
        return value
    if random.randrange(20) % 2 == 0:
        plus="+"
    else:
        plus="-"
    num=str(random.randrange(1,20))
    newval=value + " " + plus + " " + num
    if 0 <= eval(newval)<= 25:
        amount -= 1
        return sum1(newval,amount)
    else:
        return sum1(value,amount)

array11=[]
while len(array11) != 12:
    newone=array1[random.randrange(len(array1))]
    if newone not in array11:
        array11.append(newone)


array2=[]
while len(array2) != 12:
    d = sum1(str(random.randrange(1,20)),random.randrange(2,4))
    if d not in array2:
        array2.append(d)


for i in array2 + array11:
    print(i+"\n")
