#Exe 7.1

#car = input("What kind of car you would like? : ")
#print('\nLet me check if i have the ' + str(car) + ' car,')

#Exe 7.2

#restaurant_seating = input("How many people are in your dinner group? ")
#restaurant_seating = int(restaurant_seating)
#if restaurant_seating > 8:
#    print("Sorry, you have to wait for some time")
#else:
#    print("Your table is ready")

#Exe  7.3

#number = input("Give me a number: ")
#number = int(number)
#if number % 10 == 0:
#    print("Your number is multiple of 10")
#else:
#    print("It's not")

#Exe 7.4

#propmp = "              ###Toppings Adder###                "
#propmp += "\n\ntype 'ok' to quit"
#propmp += "\nPlease add your topping: "

#active = True
#while active:
#    message = input(propmp)

#    if message == 'ok':
#       active = False
#    else:
#        print("We will add " + message.upper() + ' topping for you')

#Exe 7.5

#promp = "Tell me your age: "
#promp += "\n type quit to quit"

#active = True

#while active:
#    age = input(promp)

#    if age == 'quit':
#        break

#    age = int(age)

#    if age < 3:
#       print("Ticket is free")
#    elif age <= 12:
#        print("Ticket cost is 10$")
#    else:
#        print("Ticket cost is 15$")

#Exe 7.6

#x = 0
#while x < 10:
#    x += 1
#    if x % 2 == 0:
#        continue

#    print(x)

#Exe 7.8

#unconfirmed_users = ['alicia','tony','alex']
#confirmed_users = []
#while unconfirmed_users:
#    users = unconfirmed_users.pop()
#    print("Verified User: " + users.title())
#    confirmed_users.append(users)
#print("\nThe following users have been added: ")
#for users in confirmed_users:
#    print(users.title())

#Exe.7.8 + 7.9

chicken_dishes = ['tikka','kabab','biryani','tangdi','biryani']
unfinished_dishes = []
print("    We are runing out of biryani" + '\n')

while 'biryani' in chicken_dishes:
    chicken_dishes.remove('biryani')
print()
while chicken_dishes:
    dish = chicken_dishes.pop()
    unfinished_dishes.append(dish)
    print("     You have ordered: " + dish)

print('\n' + "----------The unfinished dishes----------" + '\n')
for dish in unfinished_dishes:
    print('\t\t\t\t' + dish)
print('\n'+'\n'+'\n')

#Exe 7.10

dream = {}

active = True

while active:
    name = input("Please enter your name: ")
    destination = input("Which is the one place you would love to go before you die?: ")

    dream[name] = destination

    another_destination = input("Would you like to enter more places?")

    if another_destination.lower() == 'no':
        active = False

print('\n' + "##----------The Poll----------##")

for key, value in dream.items():
    print("Mr." + key + " would like to visit " + value + '.')


