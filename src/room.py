# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def __str__(self):
        room_string = f"{self.name}\n\n{self.description}"
        room_string += ("\n\nExits: " + " ".join(list(self.exits.keys())))
        return room_string