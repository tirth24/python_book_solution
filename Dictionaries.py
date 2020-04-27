#Exe 6.1

info = {'name':'sahik', 'location':'thasta', 'zip':'30082', 'color':'black'}
print(info['name'])
print(info['location'])
print(info['zip'])
print(info['color'])

#Exe 6.2

num = {'tirth': 24, 'shreeji': 3, 'dk': 18, 'ab': 7}
print('\n' + "Tirth's fav. num is: " + str(num['tirth']))
print("Shreeji's fav. num is: " + str(num['shreeji']))
print("Dk's fav. num is: " + str(num['dk']))
print("ab's fav. num is: " + str(num['ab']))

#Exe 6.3
glossary = {
    'variable' : 'it holds value',
    'list' : 'holds objects',
    'loop' : 'perform repitative task',
    'whitespacing' : 'extra spaece in code',
    'if statement' : 'condition test',
}
#print('\n' + 'Variable is, ' + str(glossary['variable']))
#print('List is, ' + str(glossary['list']))
#print('Loop is, ' + str(glossary['loop']))
#print('Whitespace is, ' + str(glossary['whitespacing']))
#print('If statement is, ' + str(glossary['if statement']) + '\n')

#Exe 6.4

print()
for k, v in glossary.items():
    print('The meaning of term: ' + k.title()  + ' is ' + v.lower() + '.')
print()

#Exe 6.5

rivers = {'nile':'egypt' , 'ganga':'india', 'hudson':'uk'}
for key,value in rivers.items():
    print('The ' + key.title() + ' river runs from the ' + value.title() + ' country.')
print('\n' + 'The name of the rivers are: ')
for k in rivers.keys():
    print(k.title())
print('\n' + 'The name of the countries are: ')
for v in rivers.values():
    print(v.title())
print()

#Exe 6.6

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
ppls = ['tirth', 'shreeji', 'sarah', 'phil']

for ppl in ppls:
    if ppl in favorite_languages:
        print('Thanks for responding ' + ppl.title() + '.')
    else:
        print('Please take a pole ' + ppl.title() + '.')
print()

#Exe 6.7 **WRONG OUTPUT**

people = []
info = {'name':'sahik', 'location':'thasra', 'zip':'30082'}
people.append(info)
info = {'name':'hk', 'location':'utica', 'zip':'13501'}
people.append(info)
info = {'name':'jay', 'location':'miami', 'zip':'18514'}
people.append(info)
for data in people:
    full_name = info['name'].title()
    place = info['location'].lower()
    code = info['zip'].upper()

    print(str(full_name) + ' ' + str(place) + ' ' + str(code))

#Exe 6.8

d_1 = {'dog':'tirth', 'lion':'king'}
d_2 = {'cat':'nk', 'rat':'harsh'}
d_3 = {'parrot':'shreeji', 'deer':'shail'}
pets = [d_1,d_2,d_3]
for pet in pets:
    print('The list of the owner is: ')
    for key,value in pet:
        print('\t' + key + ' : ' + value)
