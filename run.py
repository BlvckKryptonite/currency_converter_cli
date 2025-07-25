import requests
import json
import time
import sys
import re
from typing import Dict, List, Optional, Tuple

# TODO: Clean up unused imports later
# (Currently imported for planned functionality)


class CurrencyExchangeApp:
    """Main application class for currency exchange operations."""
    def __init__(self):
        """Initialize the application with API base URL."""
        self.api_base = ("https://cdn.jsdelivr.net/npm/"
                         "@fawazahmed0/currency-api@latest/v1")
        self.supported_currencies = {}

    # Simulates a real-time loading effect using dots
    def show_loading(self, message: str = "Loading", duration: float = 1.5):
        """
        Display a loading animation with dots.
        Args:
            message (str): Message to display while loading.
            duration (float): Duration of loading animation in seconds.
        """
        print(f"\n{message}", end="")
        # Loop runs 'duration * 2' times to print a dot every 0.5 seconds
        for _ in range(int(duration * 2)):
            print(".", end="", flush=True)
            time.sleep(0.5)

    def validate_currency_code(self, currency: str) -> bool:
        """
        Validate currency code format (3 uppercase letters) eg: USD, EUR, GBP.

        Args:
            currency (str): Currency code to validate

        Returns:
            bool: True if valid format, False otherwise
        """
        # Return False if the input is empty or not exactly 3 characters
        if not currency or len(currency) != 3:
            return False

        # Regular expression checks that currency matches 3 uppercase letters
        return bool(re.match(r'^[A-Z]{3}$', currency.upper()))

    def validate_amount(self, amount_str: str) -> Tuple[bool, float]:
        """
        Validates and converts amount string to float.

        Args:
            amount_str (str): String representation of amount

        Returns:
            Tuple[bool, float]: (is_valid, amount_value)
        """
        try:
            # Attempts to convert the string to a float
            amount = float(amount_str)

            # Checks if the amount is positive to avoid invalid inputs
            # Negative or zero amounts are considered invalid
            if amount <= 0:
                return False, 0.0

            return True, amount

        except ValueError:
            # If conversion fails/non-numeric input return invalid.
            return False, 0.0

    def fetch_supported_currencies(self) -> bool:
        """
        Fetch our supported currencies from the external API.

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # To display a simple loading animation for user experience
            self.show_loading("Fetching supported currencies")

            # Make GET request to the API's /currencies.json
            response = requests.get(
                f"{self.api_base}/currencies.json", timeout=10
            )
            # Raise error for any input not among 200 supported currencies
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Cache the supported currencies if the response has content
            # *** I WILL NEED TO EDIT/STYLIZE PRINT STATEMENTS LATER ***
            if data:
                # Caches the currency list in memory for later use
                self.supported_currencies = data
                return True
            else:
                print(" ❌ No currency data available ❌")
                return False

        # To handle network-related and API data decoding errors
        except requests.exceptions.Timeout:
            print("Request timed out ⏱️")
            return False
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the API.")
            return False
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return False
        except json.JSONDecodeError:
            print("Invalid format from API")
            return False

    def get_exchange_rate(self, from_currency: str,
                          to_currency: str) -> Optional[float]:
        """
        Gets exchange rate between two currencies.

        Args:
            from_currency (str): Source/initial currency code (such as "USD")
            to_currency (str): Target/final currency code (e.g., "EUR")

        Returns:
            Exchange rate as a float or None if something fails
        """
        try:
            # Display loading animation again for UX polish
            self.show_loading("Fetching exchange rate")

            # Build the API endpoint URL using the from_currency
            url = f"{self.api_base}/currencies/{from_currency.lower()}.json"

            # Make the GET request to fetch the currency data
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Checks if the from_currency key exists in the response
            if data and from_currency.lower() in data:
                # Retrieves the nested dictionary containing exchange rates
                rates = data[from_currency.lower()]

                # Return the specific rate for the final/to_currency
                return rates.get(to_currency.lower())
            else:
                print(f"❌ Currency {from_currency} invalid")
                return None

        # Handle different error scenarios as well:
        except requests.exceptions.Timeout:
            print("⏱️ Request timed out.")
            return None
        except requests.exceptions.ConnectionError:
            print(" ❌ Cannot connect to the API.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"⚠️ API request failed: {e}")
            return None
        except json.JSONDecodeError:
            print("⛔️ Invalid format from API")
            return None

    def convert_currency(self, amount: float, from_currency: str,
                         to_currency: str) -> Optional[float]:
        """
        Convert entered amount from one currency to another.

        Args:
            amount (float): Amount to convert
            from_currency (str): Source/initial currency code
            to_currency (str): Target/final currency code

        Returns:
            Converted amount or None if failed
        """
        # Use the pre existing get_exchange_rate method for conversion
        rate = self.get_exchange_rate(from_currency, to_currency)
        # If the rate is valid, multiply it with the input amount,
        # and get the converted value
        if rate is not None:
            return amount * rate
        return None

    def display_welcome(self):
        """Display welcome message and application information for engaging
        user experience."""

        print("=" * 60)
        print(" WELCOME TO MUMA'S CURRENCY EXCHANGE CLI 👋".center(60))
        print("This app helps you check exchange rates and convert "
              "currencies ")
        print("in real time 🙂".center(60))
        print("\n")
        print("Data provided by Fawaz Ahmed Currency API".center(60))
        print("=" * 60)

    def display_menu(self):
        """This will display the main menu options."""

        print("\n")
        print("MAIN MENU".center(30))
        print("-" * 30)
        # Displays the menu options for the user to choose from
        print("1. View Exchange Rate")
        print("2. Convert Currency")
        print("3. Check Supported Currencies")
        print("4. Exit")
        print("-" * 30)

    def get_user_choice(self) -> str:
        """
        Get and validate user menu choice.

        Returns:
            str: User's validated choice
        """
        valid_choices = ['1', '2', '3', '4']
        while True:
            # An infinite loop to keep asking until a valid input is given.
            choice = input("Enter your choice (1-4): ").strip()
            if choice in valid_choices:
                return choice
            else:
                print("❌ Invalid choice. Please enter a number "
                      "between 1 and 4.")

    def get_currency_input(self, prompt: str) -> str:
        """
        Get and validate currency code input from user.

        Args:
            prompt (str): Prompt message for user

        Returns:
            str: Validated currency code in uppercase
        """

        while True:
            # Trims whitespace, ensures input is uppercase
            currency = input(prompt).strip().upper()

            if not self.validate_currency_code(currency):
                print("❌ Invalid currency code. Please enter a 3-letter "
                      "code (e.g: USD, EUR).")
                continue
            # Check if we have currency list and validate against it
            if (self.supported_currencies and
               currency.lower() not in self.supported_currencies):
                print(f"'{currency}' is not a supported currency.")
                print("💡 Tip: Use option 3 to view supported currencies.")
                continue

            return currency

    def get_amount_input(self) -> float:
        """
        Get and validate amount input from user.
        Returns:
            float: Validated amount
        """
        while True:
            amount_str = input("Enter amount to convert: ").strip()
            is_valid, amount = self.validate_amount(amount_str)
            if not is_valid:
                print("❌ Invalid amount. Please enter a positive number.")
                continue
            return amount

    def handle_exchange_rate(self):
        """Handle the exchange rate viewing functionality."""

        print("\n")
        print("📊 VIEW EXCHANGE RATE".center(30))
        print("-" * 30)

        from_currency = self.get_currency_input(
            "Enter source currency (e.g. USD): ")
        target_prompt = "Enter target currency (e.g. EUR): "
        to_currency = self.get_currency_input(target_prompt)

        # If the user selects the same currency, we can skip the API call
        if from_currency == to_currency:
            print("Same currency selected. Exchange rate is 1.0000")
            return

        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate is not None:
            print(f"\n ✅ SUCCESS!")
            print(f" 📊 Exchange Rate: 1 {from_currency} = "
                  f"{rate:.4f} {to_currency}")

            # Shows a timestamp for when the data was fetched
            print(f"Data fetched on: "
                  f"{time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("\n ❌ Failed to fetch exchange rate. Please try again.")

    def handle_currency_conversion(self):
        """
        Handles the currency conversion functionality.
        Asks the user for source/target currencies and an amount,
        then performs the conversion and displays the result afterwards.
        """
        # Section Header
        print("\n")
        print("🔄 CONVERT CURRENCY".center(30))
        print("-" * 30)

        # Ask the user for the source and target currencies using validation
        from_currency = self.get_currency_input(
            "Enter source currency (e.g. USD): ")
        to_currency = self.get_currency_input(
            "Enter target currency (e.g. EUR): ")

        # Asks for the amount to convert and validate it
        amount = self.get_amount_input()

        # If same currency for both, no conversion needed
        if from_currency == to_currency:
            print(f"\n 💡 Same currency selected.")
            print(f" ✅ {amount:.2f} {from_currency} = "
                  f"{amount:.2f} {to_currency}")
            return

        converted_amount = self.convert_currency(
            amount, from_currency, to_currency)

        # Displays the result if the conversion is successful:
        if converted_amount is not None:
            print(f"\n ✅ CONVERSION SUCCESSFUL!")
            print(f"💰 {amount:.2f} {from_currency} = "
                  f"{converted_amount:.2f} {to_currency}")
            print(f" Rate: 1 {from_currency} = "
                  f"{converted_amount / amount:.4f} {to_currency}")
            # Date & Time:
            print(f"Converted on: "
                  f"{time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            # If API or rate fetching fails, notify the user
            print("\n ⚠️ Failed to convert currency. Please try again.")

    def handle_supported_currencies(self):
        """
        Will display the list of supported currencies.
        Fetches them from the API if not already cached.
        """
        # Section heading
        print("\n")
        print(" 📜 SUPPORTED CURRENCIES: ".center(35))
        print("-" * 35)

        # If currencies haven't been fetched yet, fetch and cache them
        if not self.supported_currencies:
            if not self.fetch_supported_currencies():
                print("❌ Failed to fetch supported currencies.")
                print("Please try again.")
                return

        # If the currency is available, display them:
        if self.supported_currencies:
            print(f" ✅ Found {len(self.supported_currencies)} "
                  "supported currencies:")
            print()
            currencies = list(self.supported_currencies.keys())
            currencies.sort()

            # Shows total count and prints helpful instructions
            print(f"\n Total: {len(currencies)} currencies available")
            print("\n")

            # Display currencies in rows of 4 to fit terminals
            for i in range(0, len(currencies), 4):
                row = currencies[i:i+4]
                formatted_row = [f"{curr:>3}" for curr in row]
                print("  ".join(formatted_row))
            print("\n")
            print("💡 Use any of the codes above for conversions and rates 💡")
        else:
            print(" ❌ No currency data available.")

    def ask_continue(self) -> bool:
        """
        Ask the user if they want to perform another operation.

        Returns:
            bool: True if user wants to continue, False if not.
        """
        # Loop until a valid input is received
        while True:
            # Will print a separator for better UX
            print("\n" + "─" * 50)
            continue_choice = input(
                "Would you like to perform another operation? (y/n): "
            ).strip().lower()

            if continue_choice in ['y', 'yes']:
                return True
            elif continue_choice in ['n', 'no']:
                return False
            else:
                print("❌ Please enter 'y' for yes or 'n' for no.")

    def display_goodbye(self):
        """
        Display goodbye message when the user exits the application.
        Provides a friendly and professional sign-off.
        """
        # Border line for visual separation
        print("\n" + "=" * 60)

        print(" Thank you for using Muma's Currency Exchange CLI!".center(60))
        print(" 👋 ".center(60))
        print("\n")
        print(" I truly hope you enjoyed using it! 🙂".center(60))
        print("\n")
        print("Have an absolutely wonderful day! 🌟".center(60))

        print("=" * 60)

    def run(self):
        """
        Runs the main loop of the application.
        """
        try:
            # Calls welcome message with app info
            self.display_welcome()

            print(" Initializing application...")
            self.fetch_supported_currencies()

            # Main loop
            while True:
                # Show menu options
                self.display_menu()

                # Validate user input (1-4)
                choice = self.get_user_choice()

                if choice == '1':
                    self.handle_exchange_rate()
                elif choice == '2':
                    self.handle_currency_conversion()
                elif choice == '3':
                    self.handle_supported_currencies()
                elif choice == '4':
                    break

                # Ask if the user wants to continue
                if not self.ask_continue():
                    break

            # Display final goodbye message
            self.display_goodbye()

        except KeyboardInterrupt:
            # Just in case the user interrupts the app
            print("\n\n Application interrupted by user.")
            print("Goodbye!")
            sys.exit(0)

        except Exception as e:
            # For any any unexpected exceptions
            print(f"\n Unexpected error occurred: {e}")
            print(" Please restart the application.")
            sys.exit(1)


def main():
    """
    Entry point for the CLI application.
    Initializes and runs the CurrencyExchangeApp.
    """
    app = CurrencyExchangeApp()
    app.run()


if __name__ == "__main__":
    main()
