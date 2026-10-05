"""Interactive Calculator & Unit Converter
A beginner-friendly CLI program: arithmetic, currency conversion and unit conversion.
"""

# Fixed sample exchange rates (1 unit of currency = X Indian Rupees).
# Update these values to match current rates.
RATES_TO_INR = {"INR": 1.0, "USD": 83.0, "EUR": 90.0, "GBP": 105.0}


# ---------- Input helpers (validation with while loops) ----------
def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("  Invalid input. Please enter a number, e.g. 12 or 3.5.")


def get_choice(prompt, valid_choices):
    """Keep asking until the user enters one of the valid choices."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"  Invalid choice. Please pick one of: {', '.join(valid_choices)}")


# ---------- Arithmetic ----------
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # division by zero is handled by the caller
    return a / b


def calculator():
    print("\n--- Calculator ---")
    a = get_number("Enter first number: ")
    op = get_choice("Choose operation (+, -, *, /): ", ["+", "-", "*", "/"])
    b = get_number("Enter second number: ")

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    else:
        result = divide(a, b)
        while result is None:
            print("  Cannot divide by zero.")
            b = get_number("Enter a non-zero second number: ")
            result = divide(a, b)

    print(f"Result: {a:g} {op} {b:g} = {result:g}")


# ---------- Currency ----------
def convert_currency(amount, from_cur, to_cur):
    in_inr = amount * RATES_TO_INR[from_cur]
    return in_inr / RATES_TO_INR[to_cur]


def currency_converter():
    print("\n--- Currency Converter ---")
    codes = [c.lower() for c in RATES_TO_INR]
    print("Available currencies:", ", ".join(RATES_TO_INR))
    amount = get_number("Enter amount: ")
    while amount < 0:
        print("  Amount cannot be negative.")
        amount = get_number("Enter amount: ")
    from_cur = get_choice("From currency: ", codes).upper()
    to_cur = get_choice("To currency: ", codes).upper()
    result = convert_currency(amount, from_cur, to_cur)
    print(f"{amount:,.2f} {from_cur} = {result:,.2f} {to_cur}")
    print("(Uses fixed sample rates, not live data.)")


# ---------- Units ----------
def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometres to miles")
    print("2. Miles to kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    choice = get_choice("Choose (1-4): ", ["1", "2", "3", "4"])
    value = get_number("Enter value: ")

    if choice == "1":
        print(f"{value:g} km = {km_to_miles(value):.2f} miles")
    elif choice == "2":
        print(f"{value:g} miles = {miles_to_km(value):.2f} km")
    elif choice == "3":
        print(f"{value:g} °C = {celsius_to_fahrenheit(value):.2f} °F")
    else:
        print(f"{value:g} °F = {fahrenheit_to_celsius(value):.2f} °C")


# ---------- Main menu ----------
def main():
    print("=== Interactive Calculator & Unit Converter ===")
    while True:
        print("\nMain Menu")
        print("1. Calculator")
        print("2. Currency converter")
        print("3. Unit converter")
        print("4. Exit")
        choice = get_choice("Choose an option (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            calculator()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            unit_converter()
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
