# Simple Judo Training Calculator

import math

# Constants for pricing
BEGINNER_WEEKLY = 25.00
INTERMEDIATE_WEEKLY = 30.00
ELITE_WEEKLY = 35.00
PRIVATE_COACHING = 9.50
COMPETITION_FEE = 22.00
WEEKS_PER_MONTH = 4


def get_training_fee(plan):
    """Calculate monthly training fee based on plan"""
    weekly_prices = {"1": BEGINNER_WEEKLY, "2": INTERMEDIATE_WEEKLY, "3": ELITE_WEEKLY}
    if plan not in weekly_prices:
        raise ValueError("Training plan must be 1, 2 or 3.")
    return weekly_prices[plan] * WEEKS_PER_MONTH



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


def read_number(prompt, *, integer=False, minimum=0, maximum=None, exclusive_min=False):
    """Keep asking until the value is finite and within the allowed range."""
    while True:
        try:
            raw = input(prompt)
            value = int(raw) if integer else float(raw)
            if not math.isfinite(value):
                raise ValueError
            if value < minimum or (exclusive_min and value == minimum):
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except (ValueError, OverflowError):
            lower = "greater than" if exclusive_min else "at least"
            upper = f" and at most {maximum}" if maximum is not None else ""
            kind = "whole number" if integer else "number"
            print(f"Enter a finite {kind} {lower} {minimum}{upper}.")


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
            plan = input("Choose training plan (1-3): ").strip()
            while plan not in ("1", "2", "3"):
                print("Choose 1, 2 or 3.")
                plan = input("Choose training plan (1-3): ").strip()

            # Calculate base training fee
            monthly_fee = get_training_fee(plan)

            # Get weight information
            weight = read_number("Enter current weight in kg: ", exclusive_min=True)
            category = get_weight_category(weight)

            # Get competition entries (only for Intermediate and Elite)
            competitions = 0
            if plan != "1":  # Not beginner
                competitions = read_number("Enter number of competitions this month: ", integer=True)
            else:
                print("Note: Beginner athletes cannot enter competitions")

            # Get private coaching hours
            coaching_hours = read_number("Enter private coaching hours this month (0-20): ", maximum=20)

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


        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
