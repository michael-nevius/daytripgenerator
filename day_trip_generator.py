import random

dest = ['Texas', 'South Africa', 'New Jersey', 'Mexico', 'Florida']
restaraunt = ['Chix on the Beach', 'China One', 'Chilis', 'Texas Roadhouse', 'Dinos']
transport = ['Plane', 'Trex', 'Bicycle', 'Car', 'Ship']
entertain = ['Dancing', 'Horseback', 'Feed Gators', 'Scuba Diving', 'Karaoke']
name = input('Please type your first name.: ')

def generateRandomOption(someArray):
    random_option = random.choice(someArray)
    return random_option
def placegeneration(place):
    place = generateRandomOption(dest)
    user_input = input(f'We have selected {place} does this work for you? y/n: ')
    while user_input != 'y':
          print(f'We have selected {place} does this work for you? y/n: ')
    print(f'Lets move onto your restaraunt selection!')

# def  foodgeneration(food):
#      food = generateRandomOption(restaraunt)
#      user_input = input(f'We have selected {food} does this work for you? y/n: ') 
#      return user_input
# def  transpgeneration(vehicle):
#      vehicle = generateRandomOption(transport)
#      user_input = input(f'We have selected {vehicle} does this work for you? y/n: ')
#      return user_input
# def  entertaingeneration(fun):
#      fun = generateRandomOption(entertain)
#      user_input = input(f'We have selected {fun} does this work for you? y/n: ')
#      return user_input


# place = placegeneration(dest)
# user_input = input(f'We have selected {place} does this work for you? y/n: ')

# food = generateRandomOption(restaraunt)
# user_input = input(f'We have selected {food} does this work for you? y/n: ')
       
# vehicle = transpgeneration(transport)
# user_input = input(f'We have selected {vehicle} does this work for you? y/n: ')

# fun = generateRandomOption(entertain)
# user_input = input(f'We have selected {fun} does this work for you? y/n: ')


# print(f'Thank you for using the Day Time Trip Generator {name}! We hope you enjoy the day! Please come back and see use again!')
# print('Here is your Itinerary.')
# print(f'Destination: {place}')
# print(f'Restaraunt: {food}')
# print(f'Transportation: {vehicle}')
# print(f'Entertainment: {fun}') 
