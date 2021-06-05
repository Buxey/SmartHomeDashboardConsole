class SmartPlug:
    # do i even needs these?
    _status = None
    _room_id = None
    _device_id = None
    _smartplug_id = None

    def __init__(self, smartplug_status, smartplug_room_id, smartplug_name, smartplug_id):
        self.smartplug_status = smartplug_status
        self.smartplug_room_id = smartplug_room_id
        self.smartplug_name = smartplug_name
        self.smartplug_id = smartplug_id

    def set_smartplug_name(self, smartplug_name):
        self.smartplug_name = smartplug_name

    def get_smartplug_name(self):
        return self.smartplug_name

    def set_smartplug_id(self, smartplug_id):
        self.smartplug_id = smartplug_id

    def get_smartplug_id(self):
        return self.smartplug_id
