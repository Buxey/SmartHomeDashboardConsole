class Room:
    def __init__(self, room_name, room_id):
        # _ means they are protected variables
        # these probally need to be turned into an array
        self._room_name = room_name
        self._room_id = room_id

    def set_room_name(self, value):
        # need to double check this
        self._room_name = value

    def get_room_name(self):
        return self._room_name

    def set_room_id(self, value):
        # need to double check this
        self._room_id = value

    def get_room_id(self):
        return self._room_id
