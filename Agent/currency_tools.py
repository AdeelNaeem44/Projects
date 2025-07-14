import requests
from langchain.tools import tool

API_KEY = "2d0c0520c3284b88ab912828"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@tool
def convert_currency(from_currency: str, to_currency: str, amount: float) -> str:
    """Convert a given amount from one currency to another."""
    try:
        url = BASE_URL + from_currency.upper()
        res = requests.get(url)
        if res.status_code != 200:
            return f"❌ Error fetching exchange rate: {res.status_code}"
        data = res.json()
        rate = data["conversion_rates"].get(to_currency.upper())
        if not rate:
            return f"❌ Invalid target currency: {to_currency}"
        result = round(amount * rate, 2)
        return f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}"
    except Exception as e:
        return f"❌ Exception: {str(e)}"

@tool
def list_supported_currencies() -> str:
    """List all supported currency codes."""
    try:
        res = requests.get(BASE_URL + "USD")
        if res.status_code != 200:
            return "❌ Error fetching currency list."
        data = res.json()
        return ", ".join(data["conversion_rates"].keys())
    except Exception as e:
        return f"❌ Exception: {str(e)}"
