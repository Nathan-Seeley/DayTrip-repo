greeting = print ("Welcome to your day trip planner, enjoy!")
   
import random
# day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]

# def user_destinations_choice (): 
#     random_destinations = random.choice (day_trip_destinations)
#     user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")
#     while user_destination_input != "y":
#         if user_destination_input == "n":
#             random_destinations = random.choice (day_trip_destinations)
#             user_destination_input = input (f"Would you like to go to {random_destinations} instead? (y/n) ")
#         else:
#             print ("Error: please use lower case letter y or n in order to continue with your trip planner.")
#             user_destination_input = input (f"Would you like to go to {random_destinations}? (y/n) ")

#     return random_destinations

# user_destination = user_destinations_choice ()

# day_trip_restaurants = ["Ivars", "Balthazar", "Primal Steak House"]

# def user_restaurants_choice ():
#     random_restaurants = random.choice (day_trip_restaurants)
#     user_restaurant_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
#     while user_restaurant_input != "y":
#         if user_restaurant_input == "n":
#             random_restaurants = random.choice (day_trip_restaurants)
#             user_restaurant_input = input (f"Do you want to dine at {random_restaurants} instead? (y/n) ")
#         else:
#             print ("Oops, please eat by using the lower case letters y or n")
#             user_restaurant_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
   
#     return random_restaurants

# user_restaurant = user_restaurants_choice ()

day_trip_mode_of_transportation = ["Plane", "Train", "Flying Saucer"]

def user_transportation_choice ():
    random_transportation = random.choice (day_trip_mode_of_transportation)
    user_transportation_input = input (f"Do you want to travel via {day_trip_mode_of_transportation}? (y/n) ")
    while user_transportation_input != "y":
        if user_transportation_input == "n":
            random_transportation = random.choice (day_trip_mode_of_transportation)
            user_transportation_input = input (f"In that case what about a {random_transportation} instead? (y/n)")
        else:
            print (f'' (y/n) ")    

# day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway",
# "Experience Blue Man Group"]




# random_entertainment = random.choice (day_trip_entertainment)