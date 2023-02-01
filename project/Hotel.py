class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    def find_room(self, rooms, room_number):
        return list(filter(lambda room: room.number == room_number, rooms))[0]

    def from_stars(self, stars_count: int):
        return f"{self.stars_count} stars Hotel"

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = self.find_room(self.rooms, room_number).take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.find_room(self.rooms, room_number)
        guests_to_remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= guests_to_remove

    def print_status(self):
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join([str(i) for i in self.rooms if not i.is_taken])}")
        print(f"Taken rooms: {', '.join([str(i) for i in self.rooms if i.is_taken])}")



