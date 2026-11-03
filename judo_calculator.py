# Simple Judo Training Calculator

# Constants for pricing
BEGINNER_WEEKLY = 25.00
INTERMEDIATE_WEEKLY = 30.00
ELITE_WEEKLY = 35.00
PRIVATE_COACHING = 9.50
COMPETITION_FEE = 22.00
WEEKS_PER_MONTH = 4


def get_training_fee(plan):
    """Calculate monthly training fee based on plan"""
    if plan == "1":
        return BEGINNER_WEEKLY * WEEKS_PER_MONTH
    elif plan == "2":
        return INTERMEDIATE_WEEKLY * WEEKS_PER_MONTH
    else:
        return ELITE_WEEKLY * WEEKS_PER_MONTH


def get_weight_category(weight):
    """Determine athlete's weight category"""
    if weight <= 66:
        return "Flyweight"
    elif weight <= 73:
        return "Lightweight"
    elif weight <= 81:
        return "Light-Middleweight"
    elif weight <= 90:
        return "Middleweight"
    elif weight <= 100:
        return "Light-Heavyweight"
    else:
        return "Heavyweight"


def main():
    while True:
        print("\nNorth Sussex Judo Training Calculator")
        print("1. Calculate fees for an athlete")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "2":
            print("Thank you for using the calculator!")
            break

        if choice == "1":
            # Get athlete details
            name = input("Enter athlete name: ")

            print("\nTraining Plans:")
            print("1. Beginner (2 sessions/week)")
            print("2. Intermediate (3 sessions/week)")
            print("3. Elite (5 sessions/week)")
            plan = input("Choose training plan (1-3): ")

            # Calculate base training fee
            monthly_fee = get_training_fee(plan)

            # Get weight information
            weight = float(input("Enter current weight in kg: "))
            category = get_weight_category(weight)

            # Get competition entries (only for Intermediate and Elite)
            competitions = 0
            if plan != "1":  # Not beginner
                competitions = int(input("Enter number of competitions this month: "))
            else:
                print("Note: Beginner athletes cannot enter competitions")

            # Get private coaching hours
            coaching_hours = int(input("Enter private coaching hours this month: "))
            if coaching_hours > 20:  # 5 hours per week * 4 weeks
                print("Maximum 20 hours per month. Setting to 20.")
                coaching_hours = 20

            # Calculate total fees
            coaching_fee = coaching_hours * PRIVATE_COACHING
            competition_fee = competitions * COMPETITION_FEE
            total_fee = monthly_fee + coaching_fee + competition_fee

            # Display results
            print("\n" + "=" * 30)
            print(f"Report for {name}")
            print("=" * 30)
            print(f"Training Fee: £{monthly_fee:.2f}")
            print(f"Private Coaching: £{coaching_fee:.2f}")
            print(f"Competition Fees: £{competition_fee:.2f}")
            print(f"Total Monthly Fee: £{total_fee:.2f}")
            print(f"\nWeight Category: {category}")

            # Compare weight with category
            category_limits = {
                "Flyweight": 66,
                "Lightweight": 73,
                "Light-Middleweight": 81,
                "Middleweight": 90,
                "Light-Heavyweight": 100,
                "Heavyweight": float('inf')
            }

            if weight > category_limits[category]:
                print(f"Warning: Current weight ({weight}kg) exceeds category limit!")
            else:
                print(f"Weight within category limit")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
