import requests
import json
import time
import sys
import re
from typing import Dict, List, Optional, Tuple

class CurrencyExchangeApp:
    """Main application class for currency exchange operations."""
    
    def __init__(self):
        """Initialize the application with API base URL."""
        self.api_base = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1"
        self.supported_currencies = {}