#Exe 8.1

def display_message():
    """This is the function to display the message"""
    print('I am learning about functions in this chapter')

display_message()
print()

#Exe 8.2

def favourite_book(title1):
    """This function print the message of fav. book"""
    print('One of my favourite books is ' + title1.upper() + '\n')

favourite_book('the_principle')

#Exe 8.3

def make_shirt(size, message):
    """This function will provide the info about the message on your t-shit and size of your t-shirt"""
    print('The size of your t-shirt is: ' + size)
    print('The message on you t-shirt is: ' + message.upper())

make_shirt(size='XL',message='Real Nigga')

#Exe 8.4

def make_shirt1 (size = 'XL', message = 'I love Python'):
    print('\nYour shirt size is: ' + size + ', \nYour message is: ' + message.title())

make_shirt1()
make_shirt1('M')
make_shirt1('L','Be a Hero')

#Exe 8.5

print()
def describe_city(name, country = 'India'):
    """This fu'n will print a message"""
    print(name.title() + ' is in ' + country.title() + '.')

describe_city('amdavad')
describe_city('ladakh')
describe_city('New York', country='America')

#Exe 8.6

print()
def city_country(name,country):
    """This is the print test"""
    user_input = '"' + name.title() + ', ' + country.title() + '"'
    return user_input

v_1 = city_country('abu dhabi','uae')
print(v_1)
v_1 = city_country('barcelona','spain')
print(v_1)
v_1 = city_country('wuhan','china')
print(v_1+'\n')

#Exe 8.7+8.8

def make_album(artist,album,track=''):
    """Dictionary which has music album info"""
    if track:
        user_input1 = {'artist name':artist,'album tital':album, 'track':track}
    else:
        user_input1 = {'artist name':artist,'album tital':album,}
    return user_input1
v_1 = make_album('eminem','afraid')
print(v_1)
v_1 = make_album('a.r.raheman','swadesh',4)
print(v_1)
v_1 = make_album('enrique','bailando')
print(v_1)
print('\n')

while True:
    print("Please fill the following details: "
        "Please Enter 'q' to exit")
    singer_name = input('artist name: ')
    if singer_name.lower() == 'q':
        break
    album_name = input('Name of album: ')
    if album_name.lower() == 'q':
        break
    number_of_track = input('Number of Track: ')
    if number_of_track == 'q':
        break

    zakkas = make_album(singer_name,album_name,number_of_track)
    print(zakkas + '\n')

#Exe 8.9

def show_magicians (magician):
    print("This is the names in list of Magicians:")
    for magician in magicians:
        print('\t'+magician.title())
magicians = ['kelal','dynemo','namita']
show_magicians(magicians)
print()

#Exe 8.10 & 8.11

great_magicians=[]
def make_great(magicians,great_magicians):
    while magicians:
        v_2 = magicians.pop()
        great_magicians.append(v_2 + ", The Great!!")

        if len(great_magicians) == 3:
            print("This is the updated list of magicians with greetings: ")
            print(great_magicians)
#def make_great2(great_magicians):
#    for magician in great_magicians:
#        print(great_magicians)
make_great(magicians[:],great_magicians)

print("\nThe original list of magician: ")
print(magicians)
#make_great2(great_magicians)
#print("\nThe original list of magicians: ")
#print(magicians)

#Exe 8.12

def sandwich(*types):
    print("\nYou have ordered following sandwiches:")
    for type in types:
        print(" - " + str(type))

sandwich('potato','onion','rajma')

#Exe 8.13

print()
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Tirth','Patel',age = '24', location = 'smyrna', hobby = 'A.M')
print(user_profile)

#Exe 8.14

print()
def car(manufacturer, model_name, **other):
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['model_name'] = model_name
    for key,value in other.items():
        cars[key] = value
    return cars

m = car('Hyundai','Honda Citi', year='2020', tow_package=True)
print(m)
print()

#Exe 8.15


