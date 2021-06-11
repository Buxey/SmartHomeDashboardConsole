class SmartPlug:

    def __init__(self, smart_plug_status, smart_plug_name, smart_plug_id):
        self.smart_plug_status = smart_plug_status
        self.smart_plug_name = smart_plug_name
        self.smart_plug_id = smart_plug_id

    def set_smart_plug_name(self, smart_plug_name):
        self.smart_plug_name = smart_plug_name

    def get_smart_plug_name(self):
        return self.smart_plug_name

    def set_smart_plug_id(self, smart_plug_id):
        self.smart_plug_id = smart_plug_id

    def get_smart_plug_id(self):
        return self.smart_plug_id

    def set_smart_plug_status(self, smart_plug_status):
        self.smart_plug_status = smart_plug_status

    def turn_on_smart_plugs(self):
        self.smart_plug_status = True

    def turn_off_smart_plugs(self):
        self.smart_plug_status = False

    def get_smart_plug_status(self):
        return self.smart_plug_status

    # def smart_plug_status(self, value):
    #     if value == 1:
    #         self.smart_plug_status = True
    #     if value == 2:
    #         self.smart_plug_status = False
