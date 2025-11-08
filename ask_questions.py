def ask_user_for_daily() -> dict:
    print("What are you daily habits?")
    # How long did you touch grass?
    # touch grass- Lucas D
    while True:
        touch_grass_input= input("How many minutes did you touch grass for? ")
        if touch_grass_input.isdigit():
            time = int(touch_grass_input)
            break
        else:
            print("Please enter a in how many minutes like 15, 20, 30 ...")
    
    # Water Running -Harry
    while True:
        water_running_input = input("Do you leave the water running when you brush your teeth? Type yes or no.")
        if water_running_input not in ["yes", "no"]:
            continue
        break

    # |Fastest Route| - Eason
    fastest_or_shortest_q = "Do you take the fastest route or on with the route with the least amount of miles?"
    while True:
        fastest_or_shortest = input(fastest_or_shortest_q)
        if fastest_or_shortest not in ["fastest", "shortest"]:
            print("Type 'fastest' or 'shortest'")
            continue
        break
    #|How do you travel?| -Eddy 
    while True:
            bike_or_Car = input("Do you take the bike or on a petrol/eletric car? Bike/Car")
            if bike_or_Car not in ["Bike", "Car"]:
                print("Please enter Bike or Car")#\
                continue
            break
        
    answers = {"Method  Travel" : bike_or_Car, "Water running": water_running_input, "Touch_Grass_Minutes": touch_grass_input, "Routes": fastest_or_shortest}

    return answers

ask_user_for_daily()