import logging
from src.data_processing import normalize_ingredients
from src.model import generate_recipe
from src.utils import get_nutrition
from src.visualization import plot_nutrition
from dotenv import load_dotenv

# load environment Variables 
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def main():
    raw = "chiken, garlick, lemmon"
    norm = normalize_ingredients(raw)
    logging.info(f"Normalized: {norm}")

    nutri = get_nutrition(norm)
    logging.info(f"Nutrition: {nutri}")
    plot_nutrition(nutri)

    logging.info("\n— Generating Recipe —")
    recipe = generate_recipe(norm, strategy="beam", style="gourmet", max_length=200)
    logging.info(f"\n{recipe}")

    md = (
        f"# Recipe\n\n"
        f"**Ingredients:**\n- " + "\n- ".join(norm.split(", ")) +
        f"\n\n**Directions:**\n{recipe}\n"
    )
    with open("recipe.md", "w") as f:
        f.write(md)
    logging.info("\nMarkdown saved to recipe.md")

if __name__ == "__main__":
    main()
