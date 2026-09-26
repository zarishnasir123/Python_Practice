# 5. Write a class Train which has methods to book a ticket, get status (no of seats)
#    and get fare information of train running under Indian Railways.

class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("No seats available!")

    def get_status(self):
        print(f"Available seats: {self.seats}")

    def get_fare(self):
        print(f"Fare per ticket: {self.fare}")
# Example usage
train = Train("Express", 50, 200)
train.book_ticket()
train.get_status()
train.get_fare()