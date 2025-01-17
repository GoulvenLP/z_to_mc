

class ConfigP1():

    def __init___(self):
        self.pc = 0


    def __hash__(self):
        return hash(self.pc)
    
    def __eq__(self, obj):
        if (not isinstance(obj, ConfigP1)):
            return False
        return self.pc == obj.pc