greeting = print ("Welcome to your day trip planner.  Let's explore some options together!")
   
import random
day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]

def choose_destination (): 
    random_destinations = random.choice (day_trip_destinations)
    user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")
    while user_destination_input != "y":
        if user_destination_input == "n":
            random_destinations = random.choice (day_trip_destinations)
            user_destination_input = input (f"Would you like to go to {random_destinations} instead? (y/n) ")
        else:
            print ("Error: please use lower case letter y or n in order to continue with your trip planner.")
            user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")

    return random_destinations

user_destination = choose_destination ()


day_trip_restaurants = ["Ivars", "Balthazar", "Primal Steak House"]

def choose_restaurant ():
    random_restaurants = random.choice (day_trip_restaurants)
    user_restaurant_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
    while user_restaurant_input != "y":
        if user_restaurant_input == "n":
            random_restaurants = random.choice (day_trip_restaurants)
            user_restaurant_input = input (f"Do you want to dine at {random_restaurants} instead? (y/n) ")
        else:
            print ("Oops, please eat by using the lower case letters y or n")
            user_restaurant_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
   
    return random_restaurants

user_restaurant = choose_restaurant ()

day_trip_mode_of_transportation = ["Plane", "Train", "Flying Saucer"]

def choose_transportation ():
    random_transportation = random.choice (day_trip_mode_of_transportation)
    user_transportation_input = input (f"Do you want to travel via {random_transportation}? (y/n) ")
    while user_transportation_input != "y":
        if user_transportation_input == "n":
            random_transportation = random.choice (day_trip_mode_of_transportation)
            user_transportation_input = input (f"In that case what about a {random_transportation}? (y/n) ")
        else:
            print ("Well then, that looks interesting, but please enter the lower case letters n or y! ")   
            user_transportation_input = input (f"Do you want to travel via {random_transportation}? (y/n) ")
    return random_transportation

user_transportation = choose_transportation ()

day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway","Experience Blue Man Group"]

def choose_entertainment ():
    random_entertainment = random.choice (day_trip_entertainment)
    user_entertainment_input = input (f"Would you like to {random_entertainment} for your entertainment? (y/n) ")
    while user_entertainment_input != "y":
        if user_entertainment_input == "n":
            random_entertainment = random.choice (day_trip_entertainment)
            user_entertainment_input = input (f"Would you like to {random_entertainment} instead? (y/n) ")
        else:
            print ("Invalid entry, please use a y or n")
            user_entertainment_input = input (f"Would you like to {random_entertainment} for your entertainment? (y/n) ")

    return random_entertainment        

user_entertainment = choose_entertainment ()

# user_day_trip_dictionary = {
# user_destination :
# c_user_restaurant : u,
# c_user_entertainment : user_entertainment,
# c_user_transportation : user_transportation
# }



def confirm_final_trip ():
    user_trip_confirmation = input (f"Congratulations! Your day trip is: You are going to {user_destination} on a {user_transportation} to eat at {user_restaurant} and {user_entertainment}. Do you like this trip? (y/n) "
    while user_trip_confirmation == "y"
    return confirm_final_trip

user_confirmation = confirm_final_trip ()
    
def print_confirmed_day_trip ():
    confirmed_day_trip_input = input("Would you like to see your confirmed final trip? (y/n) ")
    while confirmed_day_trip_input != "Y":
        


    







