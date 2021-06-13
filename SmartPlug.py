class SmartPlug:

    def __init__(self, smart_plug_device, smart_plug_room_name, smart_plug_id, smart_plug_status):
        self.smart_plug_device = smart_plug_device
        self.smart_plug_room_name = smart_plug_room_name
        self.smart_plug_id = smart_plug_id
        self.smart_plug_status = smart_plug_status

    def set_smart_plug_device(self, smart_plug_device):
        self.smart_plug_device = smart_plug_device

    def get_smart_plug_device(self):
        return self.smart_plug_device

    def set_smart_plug_room_name(self, smart_plug_room_name):
        self.smart_plug_room_name = smart_plug_room_name

    def get_smart_plug_room_name(self):
        return self.smart_plug_room_name

    def set_smart_plug_id(self, smart_plug_id):
        self.smart_plug_id = smart_plug_id

    def get_smart_plug_id(self):
        return self.smart_plug_id

    def set_smart_plug_status(self, smart_plug_status):
        self.smart_plug_status = smart_plug_status

    def get_smart_plug_status(self):
        return self.smart_plug_status

    def display_smart_plugs(self):
        status = \
            f"SmartPlug | attached to: {self.smart_plug_device}" \
            f" | room: {self.smart_plug_room_name}" \
            f" | ID: {self.smart_plug_id}" \
            f" | Status: {self.smart_plug_status}"
        print(status)
