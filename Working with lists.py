# Exe. 4.1

pizzas = ['cheese', 'mushroom', 'onion', 'chicken', 'garlic']
for pizza in pizzas:
    print(pizza.upper())
print()
for pizza in pizzas:
    print('This is ' + pizza.title() + ' pizza.')
print()
print('I love fuckin pizzas' + '\n')

# Exe 4.2

animals = ['cow', 'chicken', 'tiger', 'lion']
for animal in animals:
    print(animal.title())
print()

for animal in animals:
    print('A ' + animal.title() + ' would make a great pet!!')
print('Any of this animal make a great pet')
print()

#Exe 4.3

for number in range(1,21):
    print(number)

#Exe 4.4

numbers = []
for number in range(1,1000000):
    numbers.append(number)
print(numbers)
print()

#Exe 4.5

maximum_number = max(numbers)
print('The maximum number is: ' + str(maximum_number) + '\n')
minimum_number = min(numbers)
print('The maximum number is: ' + str(minimum_number) + '\n')
sum_total = sum(numbers)
print('The total is: ' + str(sum_total) + '\n')

#Exe 4.6

odd_numbers = []
for number in range(1,21,2):
    odd_numbers.append(number)
print('The list of odd number is: ' + str(odd_numbers))

#Exe 4.7

multiples = []
for multiple in range(3,31,3):
    multiples.append(multiple)
print('\n' + 'The list of multiple of 3 is: ' + str(multiples))

#Exe 4.8

cubes = []
for cube in range(1,11):
    b = cube ** 3
    cubes.append(b)
print('\n' + 'The list of cubes is:' + str(cubes))

#Exe 4.9

print()
cubes_of_comprehension = [cube ** 3 for cube in range(1,11)]
print(cubes_of_comprehension)

#Exe 4.10

print('\n' + 'The first three items in the list are: ' + str(pizzas[0:3]) + '\n')
print('The three items from the middle of the list are: ' + str(pizzas[1:4]) + '\n')
print('The last three items in the list are: ' + str(pizzas[-3:]) + '\n')

#Exe 4.11

print('***********************')
friend_pizzas = pizzas[:]
friend_pizzas.append('tomato')
pizzas.append('pork')
for pizza in pizzas:
    print('My favourite pizzas are: ' + pizza.title())
print('***********************')
for pizza in friend_pizzas:
    print("My friend's favourite pizza are: " + pizza.title())
print()

#Exe 4.13

menu = ('Chicken Kabab', 'Dalfry' ,'Chapati roti' ,'Biryani' ,'Dosha')
for item in menu:
    print(item)
print()
menu = ('Mutton Kabab', 'Dalfry-tadka' ,'Chapati roti' ,'Biryani' ,'Dosha')
for item in menu:
    print(item)
