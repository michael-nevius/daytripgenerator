import random

dest = ['Texas', 'South Africa', 'New Jersey', 'Mexico', 'Florida']
restaraunt = ['Chix on the Beach', 'China One', 'Chilis', 'Texas Roadhouse', 'Dinos']
transport = ['Plane', 'Trex', 'Bicycle', 'Car', 'Ship']
entertain = ['Dancing', 'Horseback', 'Feed Gators', 'Scuba Diving', 'Karaoke']
name = input('Please type your first name.: ')

def generateRandomOption(someArray):
    random_option = random.choice(someArray)
    return random_option

def get_user_choice(some_list):
    user_choice = 'n'
    while user_choice.lower() == 'n':
            random_selection = generateRandomOption(some_list)
            user_choice = input(f'We have selected {random_selection} does this work for you? y/n: ')
            if user_choice.lower() == 'n':
                print('Sorry I guess that wasnt good enough how about now')
               
            else:
                print(f'Finally you have chosen {random_selection}.')
    return random_selection

final_destination = get_user_choice (dest)
final_restaurant = get_user_choice (restaraunt)
final_mode_of_transportation = get_user_choice (transport)
final_form_of_entertainment = get_user_choice (entertain)
print(f"""Wait, your finished! It's about time {name} your day trip booking is complete.
You have chosen to travel to {final_destination}.
You have chosen to dine at {final_restaurant}.
You have chosen to use a/an {final_mode_of_transportation} to get around.
You have chosen to {final_form_of_entertainment}.
You can finally leave my website!!""")
