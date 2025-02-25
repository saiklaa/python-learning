##String formatting
name = "John"
age = 23
print ("%s is %d years old" %(name, age))

mylist = [1,2,3]
print ("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

##Basic String Operators

astring = "Hello world!"
print(len(astring))
print(astring.count("l"))
print(astring[3:8:2])
print(astring[::-1])
print(astring.lower())
print(astring.upper())
print(astring.startswith("Hello"))
print(astring.endswith("89"))
afewwords = astring.split(" ")
print (afewwords)

##Conditions

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
