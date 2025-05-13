import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def plot_nutrition(nutrition_data: dict):
    """
    Plot a bar chart of nutrition information.
    """
    try:
        if not nutrition_data:
            logging.warning("No nutrition data provided.")
            return
        labels = list(nutrition_data.keys())
        values = list(nutrition_data.values())
        plt.figure(figsize=(10, 5))
        plt.bar(labels, values, color='skyblue')
        plt.xlabel('Nutrients')
        plt.ylabel('Amount')
        plt.title('Nutrition Information')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.error(f"Error in plot_nutrition: {e}")
