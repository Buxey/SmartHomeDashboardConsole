from Room import Room
from SmartPlug import SmartPlug


class SmartHome:

    def __init__(self):
        self._rooms_list = []
        self._number_of_plugs = 0
        self.plugs_on_or_off = None

    def create_room(self, room_id, name_of_room):
        room = Room(room_id, name_of_room)
        self._rooms_list.append(room)

    def add_smart_plug(self, room_index, device_type):
        # need to understand line below (need someone to explain this to me)
        self._rooms_list[room_index].create_smart_plug_list(device_type, self._number_of_plugs + 1)
        self._number_of_plugs += 1

    def display_room_list(self):
        print("ENTER PLUG INFORMATION BELOW:\nROOMS AVAILABLE:")
        for room in self._rooms_list:
            print(room)

    def set_all_plugs(self, state):
        for room in self._rooms_list:
            # ask connor about this i do not understand how i can access the set_all_plugs method
            room.set_all_plugs2(state)
