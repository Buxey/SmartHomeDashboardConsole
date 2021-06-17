from Room import Room


class SmartHome:
    def __init__(self):
        self._rooms_list = []

    def create_room(self, room_id, name_of_room):
        room = Room(room_id, name_of_room)
        self._rooms_list.append(room)

    def add_smart_plug(self, room_id_selection, device_type, smart_plug_id):
        # i believe because we are interating through the _rooms_list
        # as this has an object attached to it we can therefore access the methods
        # inside of Room
        for room in self._rooms_list:
            if room.get_room_id() == room_id_selection:
                room.create_smart_plug_list(device_type, smart_plug_id)

    def display_room_list(self):
        print("ENTER PLUG INFORMATION BELOW:\nROOMS AVAILABLE:")
        for room in self._rooms_list:
            print(room)

    def set_plug_status(self, state_of_smart_plugs):
        for room in self._rooms_list:
            room.set_plug_status(state_of_smart_plugs)

    def display_smart_plugs(self):
        for room in self._rooms_list:
            room.display_smart_plugs()
