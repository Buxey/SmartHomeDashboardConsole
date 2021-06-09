import ConsoleHelper
from SmartHome import SmartHome


# start building your classes this might help you build your project

# 1) get number of rooms (done)
# 2) get number of plugs (done)
# 3) do a for loop for each room on its own, sorting out any variables that need to be sorted out (done)
# 4) add that room object to the end of the array of rooms at the end of each iteration (done)
# 5) do a for loop sorting out the plugs
# 6) add each plug object to the room (this will be another for loop and then appending this to the list)

def main():
    number_of_rooms = int(input("How many rooms are there in this property?: "))
    number_of_smartplugs = int(input("How many plugs do you want to place in this property?: "))

    # we create our smart_home object
    # this allows us to access the methods inside of the smarthome class
    smart_home = SmartHome()

    for room_id in range(number_of_rooms):
        name_of_room = input("please enter the name of your room: ")
        # double check the room + 1
        # pass these values inside of add_room
        smart_home.add_room(room_id + 1, name_of_room)
    smart_home.display_room_list()
    ConsoleHelper.display_list_options()


main()
