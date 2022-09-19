greeting = print ("Welcome to your day trip planner, enjoy!")
   
import random
day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]

def user_destinations_choice (): 
    random_destinations = random.choice (day_trip_destinations)
    user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")
    while user_destination_input != "y":
        if user_destination_input == "n":
            random_destinations = random.choice (day_trip_destinations)
            user_destination_input = input (f"Would you like to go to {random_destinations} instead? (y/n) ")
        else:
            print ("Albiet your answer is an answer. Please use y or n to complete.")
            user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")

    return random_destinations

user_destination = user_destinations_choice ()

day_trip_restaurants = ["Ivars", "", " Balthazar", "Primal Steak House"]

def user_restaurants_choice ():
    random_restaurants = random.choice (day_trip_restaurants)
    user_restaurants_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
    while user_restaurants_input != "y":
        if user_restaurants_input == "n":
            random_restaurants = random.choice (day_trip_restaurants)
            random_restaurants_input = input (f"Do you want to dine at {random_restaurants} instead? (y/n) ")
        else:
            print ("Albiet your answer is an answer. Please use y or n to complete.")
            user_restaurants_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
    return random_restaurants

user_restaurant = user_restaurants_choice ()









# day_trip_mode_of_transportation = ["Plane", "Train", "Automobile"]
# day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway",
# "Experience Blue Man Group"]



# random_transportation = random.choice (day_trip_mode_of_transportation)

# random_entertainment = random.choice (day_trip_entertainment)