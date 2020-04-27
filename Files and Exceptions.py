#Exe 10.1

f_name = 'learning_python.txt'

with open(f_name) as file:
    c_1 = file.readlines()
    print(c_1)
    print('\n')

    for line in c_1:
        print(line.strip())

    print()

e = ''
for lines in c_1:
    e += lines.strip()
print(e)
print()

#Exe 10.2

with open(f_name) as repls:
    for lne in repls.readlines():
        x = lne.replace('Python','C')
        #print(lne.replace('Python','C'))
        print(x)

#Exe 10.3

f_name1 = 'guest.txt'
name = input("Please enter your name: ")
with open(f_name1,'w') as guestfile:
    guestfile.write(name)
print()

#Exe 10.4

f_name2 = 'guest_book.txt'
guest = input("What's your name? ")
with open(f_name2,'w') as gst:
    while True:
        print("Thank you for comming " + guest)
        gst.write(guest)
        break
print()

#Exe 10.5

f_name3 = 'response.txt'
while True:
    with open(f_name3,'w') as f_3:
        responder = input('What is your name?')
        if responder != 'q':
            responses = input('Why do you likt programming?')
            x = responder + ' reason to code: ' +responses
            f_3.write(x)
            print('Please enter q to exit')
        else:
            break
print()

#Exe 10.6/10.7

while True:
    x = input('Enter first-number: ')
    y = input('Enter second-number: ')
    try:
        answer = int(x)/int(y)
    except ValueError:
        print('**Please enter number**')
    else:
        print(str(answer))
print()

#Exe 10.8/10.9

f_1 = 'clg.txt'
f_2 = 'masters.txt'

def read_file(filename):
    try:
        with open(filename) as names:
            name = names.read()
            print(name)
    except FileNotFoundError:
        print('Check the file')
        #pass
read_file(f_1)
read_file(f_2)

#Exe 10.10

def read_word(filename,word):
    with open(filename,'r') as file:
        v = file.read()
        r = v.lower().split()
        z = r.count(str(word))
        print(z)

#Exe 10.11

import json
#y = input("tell me your favourite number!! ")
f_1 = 'user_input.json'
with open(f_1,'w') as file:
    json.dump(y,file)
    print("I'll remmber that")
#with open(f_1) as file:
#    shree = json.load(file)
#    print("I'll remmber that" + str(shree))

#Exe 10.12

import json
try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I know your fav num: " + str(number))

#Exe 10.13

import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()




