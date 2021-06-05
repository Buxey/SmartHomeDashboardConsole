from Room import Room


class SmartHome:
    Room = []

    def __init__(self, size_of_array):
        self.size_of_array = size_of_array

    def set_size_of_array(self, size_of_array):
        self.size_of_array = size_of_array

    def get_size_of_array(self):
        return self.size_of_array
