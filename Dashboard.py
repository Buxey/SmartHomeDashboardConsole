import ConsoleHelper
from SmartHome import SmartHome


# start building your classes this might help you build your project

# 5) do a for loop sorting out the plugs
# 6) add each plug object to the room (this will be another for loop and then appending this to the list)

def main():
    number_of_rooms = int(input("How many rooms are there in this property?: "))
    number_of_smartplugs = int(input("How many plugs do you want to place in this property?: "))

    smart_home = SmartHome()

    for room_id in range(number_of_rooms):
        name_of_room = input("please enter the name of your room: ")
        smart_home.add_room(room_id + 1, name_of_room)
    smart_home.display_room_list()
    ConsoleHelper.display_list_options()


main()
