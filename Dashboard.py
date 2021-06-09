import ConsoleHelper
from SmartHome import SmartHome


def main():
    device_list = ["Lamp", "TV", "Computer", "Phone Recharger", "Heater"]
    number_of_rooms = int(input("How many rooms are there in this property?: "))
    number_of_smartplugs = int(input("How many plugs do you want to place in this property?: "))

    smart_home = SmartHome()

    for room_id in range(number_of_rooms):
        name_of_room = input("please enter the name of your room: ")
        smart_home.create_room(room_id + 1, name_of_room)
    smart_home.display_room_list()
    room_id_selection = input("Using the above list, please select the room for this plug (integer only): ")
    ConsoleHelper.display_list_options(device_list)
    for smart_plug_index in range(number_of_smartplugs):
        device_selection = int(input(
            "Using the above list, please select the device to attach to the smart plug (integer only): "))
        smart_home.add_smart_plug(smart_plug_index, device_list[device_selection - 1])


main()
