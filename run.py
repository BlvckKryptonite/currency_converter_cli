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
        self.api_base = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1"
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
                print("No currencies data")
                return False

        # To handle network-related and API data decoding errors
        except requests.exceptions.Timeout:
            print("Request timed out.")
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
        
    def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        """
        Gets exchange rate between two currencies.

        Args:
            from currency (str): Source/initial currency code (such as "USD")
            to currency (str): Target/final currency code (e.g., "EUR")

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
            response.raise_for_status()  # Raises an error if the request failed (non-200 status)

            # Parse the JSON response
            data = response.json()

            # Checks if the from_currency key exists in the response
            if data and from_currency.lower() in data:
                # Retrieves the nested dictionary containing exchange rates
                rates = data[from_currency.lower()]

                # Return the specific rate for the final/to_currency
                # IMPORTANT:
                # I WILL NEED TO EDIT THE USER PRINT STATEMENTS LATER 
                return rates.get(to_currency.lower())
            else:
                print(f"Currency {from_currency} invalid")
                return None

        # Handle different error scenarios as well:
        except requests.exceptions.Timeout:
            print("Request timed out.")
            return None
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the API.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None
        except json.JSONDecodeError:
            print("Invalid format from API")
            return None

    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Optional[float]:
        """
        Convert entered amount from one currency to another.

        Args:
            amount (float): Amount to convert
            from_currency (str): Source/initial currency code
            to curency (str): Target/final currency code

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
        # IMPORTANT: 
        # I WILL NEED TO EDIT & STYLIZE THE PRINT STATEMENTS LATER

        print("MUMA's CURRENCY EXCHANGE CLI APPLICATION")
        print("Welcome!")
        print("Convert currencies.")  # Briefly describe what it does
        print("API by..")  # API INFORMATION





