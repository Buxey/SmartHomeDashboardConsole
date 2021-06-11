from SmartPlug import SmartPlug


class Room:

    def __init__(self, _room_id, _room_name):
        self._room_id = _room_id
        self._room_name = _room_name
        self._plug_list = []

    def create_smart_plug_list(self, device_type, smart_plug_id):
        smart_plug = SmartPlug(False, device_type, smart_plug_id)
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

    # maybe try and do the calculations in room
    # then call one of the methods inside of smartplug
    # then change the status that way

    # def set_all_plugs(self, state):
    #     for smart_plug in self._plug_list:
    #         smart_plug.smart_plug_status(state)

    def set_all_plugs_rooms(self, value):
        for plug in self._plug_list:
            if value == 1:
                # i believe this issue lies here
                plug.turn_on_smart_plugs()
                # print statement does not work
                plug.get_smart_plug_status()
            if value == 2:
                plug.turn_on_smart_plugs()
