from functools import reduce
#Dictionary

books = {
    'Гарри Поттер и философский камень' : 'Джоан Роуглинг' ,
    'Убить пресмешника' : 'Харпер Ли'
}
print (books)

#List comprehension

#new_list = [expression for item in iterable if condition]

numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)

users= [{'name' : 'Alice' , 'active' : True}, {'name' : 'Bob', 'active' : False}]
active_users=[user['name'] for user in users if user['active']]
print (active_users)

#Dict comprehension

#new_dict = {key_expression: value_expression for item in iterable if condition}

squares = { x: x**2 for x in range(10)}
print(squares)

config = {'host': 'localhost', 'port': '8080', 'debug': True}
config_upper = {k.upper(): v for k, v in config.items()}
print(config_upper)



#Set comprehension

unique_numbers = {x % 3 for x in range(10)}
print(unique_numbers)

emails = {'a@example.com' , 'b@example.com', 'a@example.com'}
unique_emails={email for email in emails}
print (unique_emails)


#Creating own iterators 
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

countdown = Countdown(5)
for number in countdown:
    print(number)
    
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

file_iter = FileIterator('log.txt')
for line in file_iter:
    print(line)
    
#map() filter() reduce()
numbers = [1,2,3,4]
squared = list(map(lambda x: x**2, numbers))
print(squared)
#map() is used to transform all elements in a sequence 
#filter() leaves only elements that satisfy condition 
even_numbers = list(filter(lambda x: x %2 == 0, numbers))
print(even_numbers)
#reduce() collapses the sequence into a single value 
sum_numbers = reduce(lambda x, y: x + y , numbers)
print(sum_numbers)