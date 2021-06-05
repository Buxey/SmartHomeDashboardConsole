class SmartPlug:
    def __init__(self, smartplug_name, smartplug_id):
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
