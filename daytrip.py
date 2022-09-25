greeting = print ("Welcome to your experience. Let's explore your trip for a day!")

       
   
    
    
import random

day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]

def choosing_destination (): 
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

user_destination = choosing_destination ()

day_trip_restaurants = ["Ivars", "Balthazar", "Primal Steak House"]

def choosing_restaurant ():
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

user_restaurant = choosing_restaurant ()

day_trip_mode_of_transportation = ["Plane", "Train", "Flying Saucer"]

def choosing_transportation ():
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

user_transportation = choosing_transportation ()

day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway","Experience Blue Man Group"]

def choosing_entertainment ():
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

user_entertainment = choosing_entertainment ()

user_trip_choice = (f"Your trip choices: You are going to {user_destination} on a {user_transportation} to eat at {user_restaurant} and {user_entertainment}.")

def confirming_trip ():
    confirmation_response = ("Your trip is confirmed.")
    user_confirmation_input = input (f"{user_trip_choice} Please confirm your trip by pressing (y). Otherwise, please press (n) to choose again. ")
    while user_confirmation_input != "y":
        if user_confirmation_input == "n":
            
            import random
            day_trip_destinations = ["Seattle", "New York City", "Las Vegas"]

            def choosing_destination (): 
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

            new_user_destination = choosing_destination ()

            day_trip_restaurants = ["Ivars", "Balthazar", "Primal Steak House"]

            def choosing_restaurant ():
                random_restaurants = random.choice (day_trip_restaurants)
                user_restaurant_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
                while user_restaurant_input != "y":
                    if user_restaurant_input == "n":
                        random_restaurants = random.choice (day_trip_restaurants)
                        user_restaurant_input = input (f"Do you want to dine at {random_restaurants} instead? (y/n) ")
                    else:
                        print ("Invalid entry please use y or n")
                        user_restaurant_input = input (f"Do you want to dine at {random_restaurants}? (y/n) ")
                                        
                return random_restaurants

            new_user_restaurant = choosing_restaurant ()

            day_trip_mode_of_transportation = ["Plane", "Train", "Flying Saucer"]

            def choosing_transportation ():
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

            new_user_transportation = choosing_transportation ()

            day_trip_entertainment = ["Shop at Pike Place Market", "See a musical on Broadway","Experience Blue Man Group"]

            def choosing_entertainment ():
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

            new_user_entertainment = choosing_entertainment ()
            user_new_trip_choice = (f"Your new trip choices: You are going to {new_user_destination} on a {new_user_transportation} to eat at {new_user_restaurant} and {new_user_entertainment}.")
            user_confirmation_input = input (f"{user_new_trip_choice} Please confirm your new trip by pressing (y). Otherwise, please press (n) to choose again. ")
            
            def printing_user_trip_selections ():
                user_input_print_confirmation = input ("Would you like to display your trip on the console (y/n)? ")
                user_trip = ("Have a great time!") 
                while user_input_print_confirmation != "n":
                    if user_input_print_confirmation == "y":
                        print (f"You are going to {new_user_destination} on a {new_user_transportation} to eat at {new_user_restaurant} and {new_user_entertainment}.")
                        break
                    else:
                        print ("Invalid entry, please use a y or n")
                        user_input_print_confirmation = input ("Would you like to see your trip on the console (y/n)? ")  
                               
            user_printable_trip = printing_user_trip_selections ()

        else:
            print ("Invalid entry, please use a y or n")
            user_confirmation_input = input (f" {user_new_trip_choice} Please confirm your trip by pressing (y). Otherwise, please press (n) to choose again. ")

    return (confirmation_response)
def printing_user_trip_selections ():
    user_input_print_confirmation = input ("Would you like to display your trip on the console (y/n)? ")
    user_trip = ("Have a great time!") 
    while user_input_print_confirmation != "n":
        if user_input_print_confirmation == "y":
            print (f"You are going to {user_destination} on a {user_transportation} to eat at {user_restaurant} and {user_entertainment}.")
            break
        else:
            print ("Invalid entry, please use a y or n")
        user_input_print_confirmation = input ("Would you like to see your trip on the console (y/n)? ")  
        print (user_trip)                
                        
user_printable_trip = printing_user_trip_selections ()     
user_confirmation = confirming_trip ()
print (user_confirmation)

def printing_user_trip_selections ():
            user_input_print_confirmation = input ("Would you like to display your trip on the console (y/n)? ")
            user_trip = ("Have a great time!") 
            while user_input_print_confirmation != "n":
                if user_input_print_confirmation == "y":
                    print (f"You are going to {user_destination} on a {user_transportation} to eat at {user_restaurant} and {user_entertainment}.")
                    break
                else:
                    print ("Invalid entry, please use a y or n")
                    user_input_print_confirmation = input ("Would you like to see your trip on the console (y/n)? ")  
            print (user_trip)                
                        
user_printable_trip = printing_user_trip_selections ()



                

