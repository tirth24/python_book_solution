#Exe 5.1 and 5.2

cars = ['audi','bmw','mustang','ford','mecidiz','suzuki','hundai','suburu','farari','lincon']
for car in cars:
    if car == 'audi':
        print('This is my favourite car')
    if car == 'mustang':
        print('Is it a car though?')
print()

age = 24
print(age == 23)
print(age >= 22)
print(age <= 24)
print(age > 30)
print(age < 25 )
print()

banned_users = ['patel_23', 'Shah', 'deE_23' ]
user = 'Patel_23'
if user not in banned_users:
    print(str(user) + ', You can comment now')
if user.lower() in banned_users:
    print(str(user) + ', Nice Try')
print()

a_1 = 23
a_2 = 20
print(a_1 > 20 and a_2 < 30)
print(a_1 == 22 or a_2 == 19)
print()

#not from execercise
person = 72 #change the value of person to check the right to vote
if person >= 18:
    print('You can vote')
    print('Please register yourself')
else:
    print('You are not allowed to vote')
    print('Wait untill you turn 18')
print()

#exe 5.3

alien_color = ['green','red','yellow']
for color in alien_color:
    if color == 'green':
         print('You just earned 5 points!!')
    if color != 'green':
        print('Zero Point')

#Exe 5.4

print()
for color in alien_color:
    if color == 'green':
        print('Your have earned 5 points')
    else:
        print('You have earned 10 points')
print()

if alien_color == 'green':
    print('5 points')
print()

#Exe 5.5

alien_colours = 'orange'
if alien_colours == 'green':
    print('You have earned 5 points')
elif alien_colours == 'yellow':
    print('You have earned 10 points')
elif alien_colours == 'red':
    print('You have earned 15 points')
else:
    print('You havent earned anything!! Sorry')
print()

#Exe 5.6

age = 100
if age < 2:
    print(str(age) + ' year old person is a baby')
elif age < 4:
    print(str(age) + ' year old person is a toddler')
elif age < 13:
    print(str(age) + ' year old person is a kid')
elif age < 20:
    print(str(age) + ' year old person is a teenager')
elif age < 65:
    print(str(age) + ' year old person is an adult')
else:
    print('the person is an elder' + '\n')

#Exe 5.7

favourite_fruits = ['banana', 'orange', 'grape']
if 'banana' in favourite_fruits:
    print('I really like banana!!')
if 'grape' in favourite_fruits:
    print('I really like grape!!')
if 'apple' in favourite_fruits:
    print('I really like apple!!')
if 'pinaple' in favourite_fruits:
    print('I really like pinaple!!')
if 'guawa' in favourite_fruits:
    print('I really like guawa!!')
print()

#Exe 5.8

usernames = ['admin', 'tirth', 'raja','dakar','shreeji']
for user in usernames:
    if user == 'admin':
        print('Welcome Admin')
    else:
        print('Welcome User, ' + str(user).title())
print()

#Exe 5.9

updated_list = []
if updated_list:
    print('Nice!!')
else:
    print('Need more user')
print()

#Exe 5.10

current_users = ['admin', 'tirth', 'raja','dakar','shreeji']
new_users = ['Shreeji','tirth','akshay','john','marsh']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(str(new_user) + ', Already Exits!!')
    else:
        print(str(new_user).lower() + ' ,The username is availabe!!')
print()

#Exe 5.11

L1 = []
for number in range(1,10):
    L1.append(number)
for item in L1:
    if item == 1:
        print(str(item) + 'st')
    elif item == 2:
        print(str(item) + 'nd')
    elif item == 3:
        print(str(item) + 'rd')
    else:
        print(str(item) + 'th')




