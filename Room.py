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

    def set_plug_status_room(self, state_of_smart_plugs):
        for plug in self._plug_list:
            if state_of_smart_plugs == 1:
                # i believe this issue lies here
                # i do not believe that the method inside of smartPlug is being called
                plug.turn_on_smart_plugs()
                # print statement does not work
                print(plug.get_smart_plug_status())
            if state_of_smart_plugs == 2:
                plug.turn_off_smart_plugs()
                print(plug.get_smart_plug_status())
