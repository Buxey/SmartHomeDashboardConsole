class SmartPlug:

    def __init__(self, smart_plug_name, smart_plug_id):
        self.smart_plug_status = False
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
