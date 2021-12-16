class Agent:

    def __init__(self, _id, name, version, os, inventory, modules, status):
        self.id = _id
        self.name = name
        self.version = version
        self.os = os
        self.inventory = inventory
        self.modules = modules
        self.status = status

    def show_all_attributes_agent(self):
        print(self.__dict__)
        return self.__dict__


