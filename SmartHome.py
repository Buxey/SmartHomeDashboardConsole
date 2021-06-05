from Room import Room


class SmartHome:
    rooms_list = []


def __init__(self, room_status, room_id):
    self.room_status = room_status
    self.room_id = room_id


def create_rooms(room_id, room_name, rooms_list):
    room = Room(room_id, room_name)
    rooms_list.append(room)
