class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age >= 60:
            return 100

if __name__ == "__main__":
    zoo = Zoo()
    print("This is a simple Zoo class!")
    print("Example: C1b1:", zoo.get_ticket_price(-1))
    print("Example: C1b2:", zoo.get_ticket_price(0))
    print("Example: C1b3:", zoo.get_ticket_price(20))
    print("Example: C1b4:", zoo.get_ticket_price(21))
    print("Example: C1b5:", zoo.get_ticket_price(99))