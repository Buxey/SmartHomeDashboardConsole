from Room import Room


class SmartHome:

    def __init__(self):
        # write this into a flash card
        self._rooms_list = []

    def add_room(self, room_id, name_of_room):
        # the parameters then get passed into the room Object
        # from the class Rooms
        # which then initalise them
        room = Room(room_id, name_of_room)
        # finally we save our ids and rooms inside of this rooms_list array
        self._rooms_list.append(room)

    # need to come back to this

    def display_room_list(self):
        print("ENTER PLUG INFORMATION BELOW: ")
        for room in self._rooms_list:
            print(room)

    ## need to write down some flash cards and make sure i understand what happened
