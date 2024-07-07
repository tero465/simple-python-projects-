# Room class definition
class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        print(f"Your room number is {self.room_number}, your room type is {self.room_type}, and the price is {self.price}")

    myDir= {
    102: ("Double", 1500),
    103: ("Suite", 2500),
    104: ("Single", 1200),
    105: ("Double", 1800),
    106: ("Suite", 2800),
    107: ("Single", 1100),
    108: ("Double", 1600),
    109: ("Suite", 2700),
    110: ("Single", 1050)
           } 
    print(myDir)
