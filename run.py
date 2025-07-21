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

