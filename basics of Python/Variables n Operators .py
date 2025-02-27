##Variables

myint = 2
myfloat = 1.0 ##float(1)
mystring="hello"
print(myfloat, myint, mystring)

##Lists

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
for i in mylist:
    print (i)
    
##Basic operators 

##Arithmetic operators

number = 1 + 2 * 3 / 4
print(number)
remainder = 11 % 3
print(remainder)
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

##Using Operators with Strings 

helloworld = "hello" + " " + "world"
print(helloworld)
lotsofhellos= "hello" * 10
print (lotsofhellos)

##Using operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
print([1,2,3] * 3)
