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
            # once again i believe that some kind of condition is not being made because
            # when i run this thing through the debugger, it stops at the for loop and does not continue?
            # so this must mean that this get smartplug_id method i have is not doing what it should be doing??
            # i am almost certain that the issue is that we are NOT GETTING THE SMARTPLUG ID
            if room.get_smart_plug_id() == smart_plug_id:
                room.display_smart_plug_id()

    def room_level_status_change(self, room_id_selection, state_of_smart_plugs):
        for room in self._rooms_list:
            if room.get_room_id() == room_id_selection:
                room.set_plug_status(state_of_smart_plugs)

    def room_level_smart_plug_id(self, smart_plug_selection, state_of_smart_plugs):
        for room in self._rooms_list:
            # from having a look it seems like this piece of code below is not being met therefore is it not calling
            # the room.set_plug_status(state_of_smart_plugs) ????
            if room.get_smart_plug_id() == smart_plug_selection:
                room.set_plug_status(state_of_smart_plugs)

    def display_smart_plugs(self):
        for room in self._rooms_list:
            room.display_smart_plugs()

    def get_smart_plug_id(self, smart_plug_id_selection):
        for room in self._rooms_list:
            room.get_smart_plug_id(smart_plug_id_selection)
