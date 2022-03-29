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
    while user_input is 'n':
          print(f'We have selected {place} does this work for you? y/n: ')
def  foodgeneration(food):
     food = generateRandomOption(restaraunt)
     user_input = input(f'We have selected {food} does this work for you? y/n: ') 
     return user_input
def  transpgeneration(vehicle):
     vehicle = generateRandomOption(transport)
     user_input = input(f'We have selected {vehicle} does this work for you? y/n: ')
     return user_input
def  entertaingeneration(fun):
     fun = generateRandomOption(entertain)
     user_input = input(f'We have selected {fun} does this work for you? y/n: ')
     return user_input
def get_user_choice(some_list):
    user_choice = "n"
    while user_choice.lower() == "n":
            random_selection = generateRandomOption(some_list)
            user_choice = input(f"We have selected {random_selection}. Do you like this choice? Enter y/n :")
            if user_choice.lower() == 'n':
                print("Sorry I guess that wasn't good enough how about now")
                some_list.remove(random_selection)
            else:
                print(f"Finally you have chosen  {random_selection}.")
    return random_selection

final_destination = get_user_choice (dest)
restaraunt = foodgeneration(final_destination)
final_restaurant = get_user_choice (restaraunt)
modes_of_transportation = transpgeneration(final_destination)
final_mode_of_transportation = get_user_choice (transport)
forms_of_entertainment = entertaingeneration(final_destination)
final_form_of_entertainment = get_user_choice(entertain)
print(f"""Congratulations! {name} Your day trip booking is complete.
You have chosen to travel to {final_destination}.
You have chosen to dine at {final_restaurant}.
You have chosen to use a/an {final_mode_of_transportation} to get around.
You have chosen to {final_form_of_entertainment}.
Have a great time!!""")
