import ConsoleHelper
from SmartHome import SmartHome


def main():
    device_list = ["Lamp", "TV", "Computer", "Phone Recharger", "Heater"]
    number_of_rooms = int(input("How many rooms are there in this property?: "))
    number_of_smart_plugs = int(input("How many plugs do you want to place in this property?: "))

    smart_home = SmartHome()

    for room_id in range(number_of_rooms):
        name_of_room = input("please enter the name of your room: ")
        smart_home.create_room(room_id + 1, name_of_room)
    smart_home.display_room_list()
    ConsoleHelper.display_list_options(device_list)
    for smart_plug_id in range(number_of_smart_plugs):
        room_id_selection = int(input("Using the above list, please select the room ID for this plug (integer only): "))
        device_selection = int(input(
            "Using the above list, please select the device to attach to the smart plug (integer only): "))
        smart_home.add_smart_plug(room_id_selection, device_list[device_selection - 1], smart_plug_id + 1)
    smart_home.display_smart_plugs()
    on_or_off_selection = bool(int(input(
        "HOUSE LEVEL OPTIONS:\n 0 - Switch all plugs off \n"
        " 1 - Switch all plugs on\nSelect an option (integer only): ")))
    smart_home.set_plug_status(on_or_off_selection)
    smart_home.display_smart_plugs()
    smart_home.display_available_room_id()
    room_id_selection_2 = int(input("Please select a room ID (integer only): "))
    smart_home.display_selected_room(room_id_selection_2)
    print(
        "ROOM LEVEL OPTIONS: \n "
        "0 - Switch all devices off in room \n "
        "1 - Switch all devices on in room \n "
    )
    room_level_option = bool(int(input(
        "Please select an option: ")))
    smart_home.room_level_status_change(room_id_selection_2, room_level_option)
    smart_home.display_selected_room(room_id_selection_2)
    smart_plug_id_selection = int(input("Please select a smart plug ID (integer only): "))
    print(
        "PLUG LEVEL OPTIONS \n 0 - Switch plug off \n 1 - Switch plug on \n 2 - Change attached device \n 3 - Move "
        "plug to different room")
    smart_plug_id_option = int(input(
        "Please select an option: "))
    if smart_plug_id_option == 0 and smart_plug_id_option == 1:
        smart_home.smart_plug_id_state(smart_plug_id_selection, smart_plug_id_option)
        smart_home.display_selected_smart_plug_id(smart_plug_id_selection)
    if smart_plug_id_option == 2:
    # working on organisation of the options that are available
    if smart_plug_id_option == 3:
        ConsoleHelper.display_list_options(device_list)


main()
