#Exe 9.1

class Restaurant():
    """This is restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name of the restaurant is: "+ self.restaurant_name + '\n' + 'Cuisine type: '+self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is open")

restaurant = Restaurant('Harprit','Punjabi')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print('\n')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('\n')

#Exe 9.2

i_1 = Restaurant('Micasa','Spanish')
i_2 = Restaurant('Dennys','American')
i_3 = Restaurant('Taj','Indian')
i_1.describe_restaurant()
i_2.describe_restaurant()
i_3.describe_restaurant()
print('\n')

#Exe 9.3

class User():
    def __init__(self, first_name, last_name, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.zip = zip
    def describe_user(self):
        print("The following is the summary of user: ")
        print(' * First name: ' + self.first_name)
        print(' * Last name: ' + self.last_name)
        print(' * Location: ' + self.zip)
    def greet_user(self):
        print("Hello, " + self.first_name + ", How's it going??")

i_11 = User('shreeji','patel','india')
i_22 = User('shail','bakchod','uk')
i_33 = User('ak','bhoite','usa')

i_11.describe_user()
i_11.greet_user()
i_22.describe_user()
i_22.greet_user()
i_33.describe_user()
i_33.greet_user()
print('\n')

#Exe 9.4

class Restaurant():
    """This is restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("The name of the restaurant is: "+ self.restaurant_name + '\n' + 'Cuisine type: '+self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is open")
    #def numbers(self):
        m = self.number_served
        print(m)
    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self, number):
        self.number_served += number
        print(self.number_served)


i_41 = Restaurant('Harprit','Indian',)
#i_41.number_served = '20000'
#i_41.numbers()

i_41.set_number_served(100)
i_41.increment_number_served(248)
print('\n')

#Exe 9.5

class User():
    def __init__(self, first_name, last_name, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.zip = zip
        self.login_attempts = 0
    def describe_user(self):
        print("The following is the summary of user: ")
        print(' * First name: ' + self.first_name)
        print(' * Last name: ' + self.last_name)
        print(' * Location: ' + self.zip)
    def greet_user(self):
        print("Hello, " + self.first_name + ", How's it going??")
    def increment_login_attampt(self):
        self.login_attempts += 1
    def reset_login_attampt(self):
        self.login_attempts = 0

shreeji = User('shreeji','patel','india')
shreeji.increment_login_attampt()
shreeji.increment_login_attampt()
shreeji.increment_login_attampt()
print("Number of login attampts: " + str(shreeji.login_attempts))
shreeji.reset_login_attampt()
print("Reseting check: " + str(shreeji.login_attempts))
print('\n')

#Exe 9.6

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = ['pinaple','banana','chocolate']
    def flavours(self):
        print('The list of availabe flavours are: ')
        for icefla in self.flavour:
            print(icefla)
        #print(str(self.flavour))
i_61 = IceCreamStand('Harprit','Indian',)
i_61.flavours()
print('\n')

#Exe 9.7

class Admin(User):
    def __init__(self,first_name, last_name, zip):
        super().__init__(first_name, last_name, zip)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privilege(self):
        print("The addmin can do following thigns: ")
        for sen in self.privileges:
            print(sen)
i_71 = Admin('tirth','patel','30082')
i_71.show_privilege()
print('\n')

#Exe 9.8&9.9

#*** Need to do more research ***

#Exe 9.10/11/12
# straight forward exercise and all program in the same file

#Exe 9.13

from collections import OrderedDict
glossary = OrderedDict()
glossary = {}
glossary['variable'] = 'it holds value'
glossary['list'] = 'holds objects'
glossary['loop'] = 'perform repitative task'
glossary['whitespacing'] = 'extra spaece in code'
glossary['if statement'] = 'condition test'

for k, v in glossary.items():
    print('The meaning of term: ' + k.title()  + ' is ' + v.lower() + '.')
print()

#Exe 9.14

from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)




