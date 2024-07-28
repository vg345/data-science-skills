## Planning a holiday

# I'm going to keep this simple and not drive myself crazy by overthinking everything. 
# Starting location is assumed London. We're not looking at different airline options or different hotel options or different car options. 
# I'm also not looking at the number of people going on vacation. 

# function to print city options 
def options():
    for item in option_list:
        print(str(item) + ": " + option_list[item])

# function for returning flight cost. Double because return flights. Also, I don't need if-elif-else blocks in this function if I just get the value from a dictionary of flight prices.
def plane_cost(city):
    return flight_price[city] * 2

# function for calculating cost of rental car 
def car_rental(rental_days):
    return rental_days * 70

# function for calculating cost of a hotel room.  
def hotel_cost(num_nights):
    return num_nights * 200

# calculate total cost. I know the task description asks to use other functions as arguments but I found this way easier and more intuitive to use. 
def holiday_cost(city_flight, rental_days, num_nights):
    return plane_cost(city_flight) + car_rental(rental_days) + hotel_cost(num_nights)

# dictionary of city options. Using a dictionary because dealing with integer inputs is easier than dealing with case-sensitive text input. 
option_list = {1 : "Paris", 
               2 : "Moscow",
               3 : "New York",
               4 : "Sydney",
               5 : "Singapore"
               }

# prices approximated from Google flight search. Initial location assumed London because that's where I live and I looked at trying to figure this out from ANY start location. Too complicated. Might try to figure that out later. Used city names instead of number keys because you can always add or remove items from the list without keeping track of the key values in the other dictionary. So the order of items in both dictionaries doesn't have to match so long as they both have the same cities.
flight_price = {"Paris" : 50,
                "Moscow" : 375,
                "New York" : 345,
                "Sydney" : 635,
                "Singapore" : 500
                }

# boolean to control while loop
enter_city = True
# while loop until user inputs a valild number. 
while enter_city:
    # print city options
    options()
    # get user input for city option. Will throw a runtime error if the user tries to input letters or special characters. Same problem with num_nights and rental_days variables.
    option_number = int(input("Enter a number from 1-5 to choose travel destination.\n"))
    # exit loop if input is valid
    if 0 < option_number < 6:
        enter_city = False
    # loop again if input is wrong
    else:
        print("Invalid input.")

# variable to store city
city_flight = option_list[option_number]
# user input for number of nights in the hotel
num_nights = int(input("How many nights would you like to book a hotel for?\n"))
# user input for number of days to rent a car
rental_days = int(input("How many days would you need a rental car for?\n"))
# Not sure if I should throw an error if someone wants to book a hotel for 2 days but rent a car for 20. Cross-country drives are a thing. 

# newline for clarity
print()
# print final output. Used separate commands instead of \n because it's easier to read.
print(f"Your chosen holiday destination is {city_flight}.")
print(f"Your flights to and from the city will cost {plane_cost(city_flight)} pounds total.")
print(f"For {num_nights} nights, one hotel room will cost {hotel_cost(num_nights)} pounds.")
print(f"For {rental_days} days, the rental car will cost {car_rental(rental_days)} pounds.")
print(f"In total, the vacation will cost {holiday_cost(city_flight, rental_days, num_nights)}")