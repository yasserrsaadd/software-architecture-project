import random

class Ticket:
    def __init__(self):
        self.team = None
        self.seat = None

    def set_team(self, team):
        self.team = team

    def set_seat(self, seat):
        self.seat = seat

    def show_details(self):
        print(f"Ticket Details: Team - {self.team}, Seat - {self.seat}")

    def clone(self):
        return self.__class__()

class TicketFactory:
    def create_ticket(self):
        return Ticket()

class FootballTicketFactory(TicketFactory):
    def create_ticket(self):
        return Ticket()

class PaymentMethod:
    def pay(self, amount):
        pass

class Fawry(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} EGP via Fawry.")

class VodafoneCash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} EGP via Vodafone Cash.")

class PaymentMethodFactory:
    def create_payment_method(self):
        pass

class FawryFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return Fawry()

class VodafoneCashFactory(PaymentMethodFactory):
    def create_payment_method(self):
        return VodafoneCash()

class TicketBookingSystem:
    def __init__(self):
        self.available_seats = set(range(1, 50001))
        self.booked_seats = []
        self.ticket_pool = []
        self.payment_method_pool = []

    def book_ticket(self):
        # List of available teams
        teams = ["Team A", "Team B", "Team C", "Team D"]
        # User selects team
        print("Available teams:")
        for i, team in enumerate(teams):
            print(f"{i + 1}. {team}")
        try:
            team_choice = int(input("Enter the number corresponding to your favorite team: "))
            if team_choice < 1 or team_choice > len(teams):
                print("Invalid team selection. Exiting...")
                return
            selected_team = teams[team_choice - 1]
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # Select number of seats
        try:
            seats = int(input("Enter the number of seats you want to book: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # Check seat availability
        if seats > len(self.available_seats):
            print("Not enough seats available.")
            return

        # Book seats
        booked = []
        for _ in range(seats):
            try:
                seat = int(input("Enter the seat number you want to book: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            if seat in self.available_seats:
                booked.append(seat)
                self.available_seats.remove(seat)
            else:
                print(f"Seat {seat} is not available.")
        print("Seats booked successfully.")

# Example usage
system = TicketBookingSystem()
system.book_ticket()
