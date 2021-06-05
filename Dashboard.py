from SmartHome import SmartHome


# start building your classes this might help you build your project

# 1) get number of rooms (done)
# 2) get number of plugs (done)
# 3) do a for loop for each room on its own, sorting out any variables that need to be sorted out
# 4) add that room object to the end of the array of rooms at the end of each iteration
# 5) do a for loop sorting out the plugs
# 6) add each plug object to the room (however you've done this)

def main():
    number_of_rooms = int(input("How many rooms are there in this property?: "))
    number_of_smartplugs = int(input("How many plugs do you want to place in this property?: "))

    for i in range(number_of_rooms):
        name_of_room = str(input("please enter the name of your room: "))
        SmartHome(i, name_of_room)


main()
