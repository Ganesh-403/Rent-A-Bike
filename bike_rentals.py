class BikeRental:
    def __init__(self, stock=100):
        """Initialize the bike rental shop with a given stock of bikes."""
        self.stock = stock
        print("Welcome to Bike Rentals!")

    def display_stock(self):
        """Display the current stock of bikes."""
        print(f"\nWe currently have {self.stock} bikes available to rent.")

class Customer:
    def __init__(self, number_of_bikes, rental_basis, number_of_days_or_weeks):
        """Initialize the customer with rental details."""
        self.number_of_bikes = number_of_bikes
        self.rental_basis = rental_basis.lower()  # Ensure basis is case-insensitive
        self.number_of_days_or_weeks = number_of_days_or_weeks

    def rent_bike(self, shop):
        """Handle the bike rental process and update the stock."""
        if self.number_of_bikes <= 0:
            print("Invalid input! The number of bikes must be greater than zero.")
        elif self.number_of_bikes > shop.stock:
            print(f"Sorry, we only have {shop.stock} bikes available.")
        else:
            shop.stock -= self.number_of_bikes
            print(f"You have successfully rented {self.number_of_bikes} bikes.")

    def return_bike(self, shop):
        """Calculate the bill and update the stock when bikes are returned."""
        total_bill = self.calculate_bill()
        shop.stock += self.number_of_bikes
        print(f"Total bill: ₹{total_bill}")
        print(f"{self.number_of_bikes} bikes have been returned. Current stock: {shop.stock}")

    def calculate_bill(self):
        """Calculate the rental cost based on the rental basis."""
        rate = {"daily": 500, "weekly": 1500}  # Define rates
        if self.rental_basis not in rate:
            print("Invalid rental basis! Use 'daily' or 'weekly'.")
            return 0

        bill = self.number_of_bikes * rate[self.rental_basis] * self.number_of_days_or_weeks

        # Apply a 30% discount for family rental (3-5 bikes)
        if 3 <= self.number_of_bikes <= 5:
            print("Family rental discount applied: 30%")
            bill *= 0.7

        return bill


def main():
    shop = BikeRental()

    while True:
        shop.display_stock()

        try:
            action = input("\nWould you like to rent or return bikes? (rent/return/exit): ").strip().lower()

            if action == "exit":
                print("Thank you for visiting Bike Rentals! Have a great day!")
                break
            elif action == "rent":
                number_of_bikes = int(input("Enter the number of bikes to rent: "))
                rental_basis = input("Enter the rental basis (daily/weekly): ").strip().lower()
                duration = int(input(f"Enter the number of {rental_basis}s for the rental: "))

                # Create a Customer instance for rental
                customer = Customer(number_of_bikes, rental_basis, duration)
                customer.rent_bike(shop)  # Rent bikes after gathering input
            elif action == "return":
                number_of_bikes = int(input("Enter the number of bikes to return: "))
                rental_basis = input("Enter the rental basis (daily/weekly): ").strip().lower()
                duration = int(input(f"Enter the number of {rental_basis}s the bikes were rented: "))

                # Create a Customer instance for return
                customer = Customer(number_of_bikes, rental_basis, duration)
                customer.return_bike(shop)  # Return bikes after gathering input
            else:
                print("Invalid action! Please enter 'rent', 'return', or 'exit'.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for bikes and duration.")

if __name__ == "__main__":
    main()
