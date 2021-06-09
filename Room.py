from SmartPlug import SmartPlug


class Room:

    ## i need to initalise something from smartplug to then save it in room
    # list of plugs inside of room
    # then create the plug object from the smartplug class
    def __init__(self, _room_id, _room_name):
        self._room_id = _room_id
        self._room_name = _room_name
        self._plug_list = []

    def create_smart_plug_list(self, device_type, smartplug_id):
        smart_plug = SmartPlug(device_type, smartplug_id)
        self._plug_list.append(smart_plug)
        print(smart_plug.get_smart_plug_name())

    def __str__(self):
        return f"{self._room_id} - {self._room_name} "

    def create_smartplug(self):
        pass

    def set_room_name(self, value):
        self._room_name = value

    def get_room_name(self):
        return self._room_name

    def set_room_id(self, value):
        self._room_id = value

    def get_room_id(self):
        return self._room_id
