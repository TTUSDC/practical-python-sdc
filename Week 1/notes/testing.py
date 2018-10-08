print("Hello World")

pizza = 3
print(pizza)

pizza = 3.3
print(pizza)

pizza = "i like pizza"
print(pizza)

pizza = 333333333333
print(pizza)

# + - / ** * // %
x = 3
y = 5
print(x - y)
print(x + y)
print(x // y)
print(x * y)
print(x ** y)
print(30 % 11)


# True, False
# and, or, is, not
print(True is True)
print(True is False)
print(False is False)
print(True is not False)
print(False is not True)
print(True or False) # True
print(True and False) # False

# <=, ==, >=, !=
greeting1 = 'Hello'
greeting2 = 'Helloo'
print("The id of the first Hello is", id(greeting1))
print("The id of the second Hello is", id(greeting2))

print(1 < 2 > 3)
print(1 != 1)

if 1 == 2:
    print("Hello")        
elif 1 != 1 or 1 > 0:
    print("What's up")

for x in range(5):
    x = x + 1
    print(x)
i = 0
while i <= 5:
    print("Hi")
    i += 1 # Same: i = i + 1

# f(x, y) = x + y

def f(x, y):
    def z(x, y):
        print("Inside function z:", x, y)
    
    print("Inside function f:", x, y)
    x -= 1 
    y -= 1
    z(x, y)
    return x, y 

x, y = f(1, 2)
print("Outside function f:", x, y)


my_list = [1, 2, "string", 4, False]
print("Before loop:", my_list)
for x in range(len(my_list)):
    my_list[x] = my_list[x] * 5

print("After loop:", my_list)

my_dict = {"key1":[1, 2, 3, 4], "key2": 2 ,"key3": 3, "key4": 4, "key5": 5 }

"""
dict
list
int
str
float
"""

for x in my_dict.items():
    print(x)