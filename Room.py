from SmartPlug import SmartPlug


class Room:
    def __init__(self, _room_id, _room_name):
        self._room_id = _room_id
        self._room_name = _room_name
        self._plug_list = []

    def create_smart_plug_list(self, device_type, smart_plug_id):
        smart_plug = SmartPlug(device_type, self._room_name, smart_plug_id, False)
        self._plug_list.append(smart_plug)

    def __str__(self):
        return f"{self._room_id} - {self._room_name} "

    def set_room_name(self, value):
        self._room_name = value

    def get_room_name(self):
        return self._room_name

    def set_room_id(self, value):
        self._room_id = value

    def get_room_id(self):
        return self._room_id

    def set_plug_status(self, state_of_smart_plugs):
        for plug in self._plug_list:
            plug.set_smart_plug_status(state_of_smart_plugs)

    def display_smart_plugs(self):
        for plug in self._plug_list:
            plug.display_smart_plugs()

    def smart_plug_id_state(self, smart_plug_id_selection, smart_plug_id_state):
        for plug in self._plug_list:
            if plug.get_smart_plug_id() == smart_plug_id_selection:
                if smart_plug_id_state == 1:
                    smart_plug_id_state = False
                else:
                    smart_plug_id_state = True
                self.set_plug_status(smart_plug_id_state)

    def display_smart_plug_id(self, smart_plug_id):
        for plug in self._plug_list:
            if plug.get_smart_plug_id() == smart_plug_id:
                plug.display_smart_plugs()

    def replace_smart_plug_device(self, smart_plug_id_selection, device_replacement):
        for plug in self._plug_list:
            if plug.get_smart_plug_id() == smart_plug_id_selection:
                plug.set_smart_plug_device(device_replacement)
                return

    def move_smart_plug(self, plug_selection):
        for plug in self._plug_list:
            # i need to create some kind of method to add this room to the selected room
            plug.add_plug_to_room(plug_selection)

