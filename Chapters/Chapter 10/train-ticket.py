# Define the class `train`
class train:
    # Class attribute: same fare for all trains
    

    # Constructor to initialize train name and available seats
    def __init__(self, name, total_seats,fare=850):
        self.name = name              # Instance attribute for train name
        self.seats = total_seats      # Instance attribute for number of available seats
        self.fare = fare

    # Instance method to display train status
    def getStatus(self):
        print(f"Name of the train: {self.name}")     # Print train name
        print(f"Available seats: {self.seats}")      # Print number of available seats

   
    def getFareInfo(self):
        print(f"The fare for the Train is {self.fare}/Seat")  # Access class attribute using cls

    # Method to book multiple seats
    def bookSeat(self, Quantity):
        if self.seats == 0:
            # No seats left
            print("Sorry, no seat available at the moment")
        elif Quantity > self.seats:
            # Trying to book more seats than available
            print(f"Only {self.seats} available, you can't book {Quantity} seats for {self.name}")
        else:
            # Enough seats are available, proceed with booking
            print(f"{Quantity} number of seats booked in {self.name}.")
            for i in range(Quantity):
                print(f"Seat number {self.seats} booked")  # Show which seat is being booked
                self.seats -= 1                            # Decrease available seats

# Create a train object named R with 5 available seats
R = train("Rajdhani", 5,540)

# Display status of the train (name and available seats)
R.getStatus()

# Show the fare info (same for all trains, comes from class attribute)
R.getFareInfo()

# Try to book 3 seats — should succeed
R.bookSeat(3)

# Try to book 4 seats — should fail since only 2 seats remain
R.bookSeat(4)
