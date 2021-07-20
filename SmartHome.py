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

    def display_selected_smart_plug_id(self, smart_plug_id):
        for room in self._rooms_list:
            # for whatever reason the get_smart_plug_id is not working????
            # this was working fine literally 30 seconds ago something has changed????
            # the room.display_smart_plugs is never touched/ triggered????
            if room.get_smart_plug_id() == smart_plug_id:
                room.display_smart_plug_id()

    def room_level_status_change(self, room_id_selection, state_of_smart_plugs):
        for room in self._rooms_list:
            if room.get_room_id() == room_id_selection:
                room.set_plug_status(state_of_smart_plugs)

    # the below is working fine
    def room_level_smart_plug_id(self, smart_plug_selection, state_of_smart_plugs):
        for room in self._rooms_list:
            # the below is not working
            if room.get_smart_plug_id() == smart_plug_selection:
                room.set_plug_status(state_of_smart_plugs)

    def display_smart_plugs(self):
        for room in self._rooms_list:
            room.display_smart_plugs()

    def get_smart_plug_id(self, smart_plug_id_selection):
        for room in self._rooms_list:
            room.get_smart_plug_id(smart_plug_id_selection)
