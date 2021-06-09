from Room import Room


class SmartHome:

    def __init__(self):
        self._rooms_list = []
        self._number_of_plugs = 0

    def create_room(self, room_id, name_of_room):
        room = Room(room_id, name_of_room)
        self._rooms_list.append(room)

    def add_smart_plug(self, room_index, device_type):
        self._rooms_list[room_index].create_smart_plug_list(device_type, self._number_of_plugs + 1)
        self._number_of_plugs += 1

    def display_room_list(self):
        print("ENTER PLUG INFORMATION BELOW:\nROOMS AVAILABLE:")
        for room in self._rooms_list:
            print(room)
