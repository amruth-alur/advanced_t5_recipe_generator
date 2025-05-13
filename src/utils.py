import os
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID")
EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY")

def get_nutrition(ingredients: str) -> dict:
    """
    Fetch nutrition data for the given ingredients using the Edamam API.
    """
    if not (EDAMAM_APP_ID and EDAMAM_APP_KEY):
        logging.warning("Edamam API credentials not set.")
        return {}
    params = {"app_id": EDAMAM_APP_ID, "app_key": EDAMAM_APP_KEY, "ingr": ingredients}
    try:
        resp = requests.get("https://api.edamam.com/api/nutrition-data", params=params, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logging.error(f"Nutrition API error: {e}")
        return {}
