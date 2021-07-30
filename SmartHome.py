from Room import Room


class SmartHome:
    def __init__(self):
        self._rooms_list = []

    def create_room(self, room_id, name_of_room):
        room = Room(room_id, name_of_room)
        self._rooms_list.append(room)

    def add_smart_plug(self, room_id_selection, device_type, smart_plug_id):
        for room in self._rooms_list:
            if room.get_room_id() == room_id_selection:
                room.create_smart_plug_list(device_type, smart_plug_id)

    def display_room_list(self):
        print("ENTER PLUG INFORMATION BELOW:\nROOMS AVAILABLE:")
        for room in self._rooms_list:
            print(room)

    def display_available_room_id(self):
        print("ROOMS AVAILABLE:")
        for room in self._rooms_list:
            print(room)

    def set_plug_status(self, state_of_smart_plugs):
        for room in self._rooms_list:
            room.set_plug_status(state_of_smart_plugs)

    def display_selected_room(self, room_id_selection):
        for room in self._rooms_list:
            if room.get_room_id() == room_id_selection:
                room.display_smart_plugs()

    def room_level_status_change(self, room_id_selection, state_of_smart_plugs):
        for room in self._rooms_list:
            if room.get_room_id() == room_id_selection:
                room.set_plug_status(state_of_smart_plugs)

    def smart_plug_id_state(self, smart_plug_id_selection, smart_plug_id_state):
        for room in self._rooms_list:
            room.get_smart_plug_id(smart_plug_id_selection, smart_plug_id_state)

    def display_selected_smart_plug_id(self, smart_plug_id):
        for room in self._rooms_list:
            room.display_smart_plug_id(smart_plug_id)

    def display_smart_plugs(self):
        for room in self._rooms_list:
            room.display_smart_plugs()

    def get_smart_plug_id(self, smart_plug_id_selection):
        for room in self._rooms_list:
            room.get_smart_plug_id(smart_plug_id_selection)

    def replace_device(self, smart_plug_id_selection, device_replacement):
        for room in self._rooms_list:
            room.replace_smart_plug_device(smart_plug_id_selection, device_replacement)

    def move_smart_plug(self, device_type, room_selection, smart_plug_id_selection):
        for room in self._rooms_list:
            if room.get_room_id() == room_selection:
                # struggling to pass down the device selected once the smartplug has been moved
                room.create_smart_plug_list(device_type, smart_plug_id_selection)
