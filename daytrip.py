day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]
day_trip_restaurants = ["Ivars", "", " Balthazar", "Primal Steak House"]
day_trip_mode_of_transportation = ["Plane", "Train", "Automobile"]
day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway",
"Experience Blue Man Group"]

day_trip_dictionary = { 
    "west_coast_Location" : "Seattle", 
    "east_coast_location" : "New York City", 
    "no_coast_location" : "Las Vegas",
    "west_coast_restaurant" : "Ivars",
    "east_coast_restaurant" : "Balthazar",
    "no_coast_restaurant" : "Primal Steak House",
    "air_travel" : "Plane",
    "track_travel" : "Train",
    "road_travel" : "Automobile",
    "shop" : "Pike Place Market",
    "see_a_show" : "See a musical on Broadway",
    "see_an_act" : "Experience Blue Man Group"
    }
    
import random
from tkinter import N

def user_destination_generator ():
    random_trip_destinations = random.choice (day_trip_destinations)
    user_destination_input = input ("Would you like to go to {random_trip_destinations}? (y/n) ")
    while user_destination_input != "y":
        if user_destination_input == "n":
            



       
random_trip_restaurants = random.choice (day_trip_restaurants)

random_transportation = random.choice (day_trip_mode_of_transportation)

random_entertainment = random.choice (day_trip_entertainment)




    





