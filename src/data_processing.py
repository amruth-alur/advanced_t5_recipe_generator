import json
import logging
from difflib import get_close_matches

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Load common ingredients
try:
    with open("data/ingredients.json") as f:
        COMMON_INGREDIENTS = json.load(f)
except FileNotFoundError:
    logging.error("ingredients.json file not found.")
    COMMON_INGREDIENTS = []

def normalize_ingredients(raw: str) -> str:
    """
    Normalize a comma-separated string of ingredients by correcting misspellings
    and standardizing names based on a predefined list of common ingredients.
    """
    try:
        if not raw or not isinstance(raw, str):
            raise ValueError("Provide a non-empty comma-separated string of ingredients.")
        tokens = [t.strip() for t in raw.split(",") if t.strip()]
        if not tokens:
            raise ValueError("No valid tokens found in input.")
        normalized = []
        for t in tokens:
            match = get_close_matches(t.lower(), COMMON_INGREDIENTS, n=1, cutoff=0.7)
            normalized.append(match[0] if match else t)
        return ", ".join(normalized)
    except Exception as e:
        logging.error(f"Error in normalize_ingredients: {e}")
        return ""
