day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]
day_trip_restaurants = ["Ivars", "", " Balthazar", "Primal Steak House"]
day_trip_mode_of_transportation = ["Plane", "Train", "Automobile"]
day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway",
"Experience Blue Man Group"]

import random

random_restaurants = random.choice (day_trip_restaurants)

random_transportation = random.choice (day_trip_mode_of_transportation)

random_entertainment = random.choice (day_trip_entertainment)
    
def user_destination_generator ():
    import random
    random_destinations = random.choice (day_trip_destinations)
    user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")
    while user_destination_input != "y":
        print (f"How about {random_destinations} instead? (y/m) ")
        
    return user_destination_generator

users_destination_choice = user_destination_generator ()

