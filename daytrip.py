
import random

    
day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]

def user_destination_choice ():
    random_destinations = random.choice (day_trip_destinations)
    user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")
    while user_destination_input != "y":
        if user_destination_input == "n":
            random_destination = random.choice (day_trip_destinations)
    return user_destination_generator


user_destination_choice = user_destination_query ()    

            
        


day_trip_restaurants = ["Ivars", "", " Balthazar", "Primal Steak House"]
day_trip_mode_of_transportation = ["Plane", "Train", "Automobile"]
day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway",
"Experience Blue Man Group"]


random_restaurants = random.choice (day_trip_restaurants)

random_transportation = random.choice (day_trip_mode_of_transportation)

random_entertainment = random.choice (day_trip_entertainment)