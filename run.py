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
