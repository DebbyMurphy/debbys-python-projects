# Q1) Kate’s cat, Roary, loves catching moths. Write a program that determines whether or not it is time for Roary catch moths.

                            # print()

                            # moths_in_house = True

                            # if moths_in_house is True:
                            #     print("Get the moths!")

                            # if not moths_in_house is True:
                            #     print("No threat detected.")

                            # print()

# Q2) Kate’s cat, Roary, loves catching moths. Write a program that determines whether or not it is time for Roary catch moths.

print()

moths_in_house = False
mitch_is_home = True

if moths_in_house == True and mitch_is_home == True:
    print("Hoooman! Help me get the moths!")

if moths_in_house == False and mitch_is_home == False:
    print("No threat detected.")

if moths_in_house == True and mitch_is_home == False:
    print("Meooooooooooooow! Hissssss!")

if moths_in_house == False and mitch_is_home == True:
    print("Climb on Mitch.")

print()

# Q3) Write a program that implements the algorithm for Red Light Cameras.

print()

light_colour = "Red"
car_detected = True

if light_colour == "Red" and car_detected == False:
    print("Do nothing.")

if light_colour == "Red" and car_detected == True:
    print("Flash!")

if light_colour == "Green" and car_detected == False:
    print("Do nothing.")

if light_colour == "Green" and car_detected == True:
    print("Do nothing.")

if light_colour == "Amber" and car_detected == False:
    print("Do nothing.")

if light_colour == "Amber" and car_detected == True:
    print("Do nothing.")


# Q4) Write a program that asks the user for their height, and determine whether or not they are tall enough to ride the rollercoaster, which has a height requirement of 120cms.

height = 119

if height >=120:
    print("Hop on!")
else:
    print("Sorry, not today :(")