import os
import logging
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Load T5 model
model_name = "flax-community/t5-recipe-generation"
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).eval()
except Exception as e:
    logging.error(f"Error loading model: {e}")
    tokenizer = None
    model = None

def generate_recipe(
    ingredients: str,
    strategy: str = "sampling",
    style: str = "standard",
    max_length: int = 512,
    temperature: float = 0.9,
    top_k: int = 50,
    top_p: float = 0.95,
    num_beams: int = 5
) -> str:
    """
    Generate a recipe based on the provided ingredients and generation strategy.
    """
    if tokenizer is None or model is None:
        logging.error("Model or tokenizer not loaded.")
        return ""
    try:
        if strategy not in {"greedy", "beam", "sampling"}:
            raise ValueError(f"Invalid strategy '{strategy}'. Choose from greedy, beam, sampling.")
        prompt = f"style: {style} ingredients: {ingredients}"
        ids = tokenizer.encode(prompt, return_tensors="pt", truncation=True)
        gen_kwargs = {"max_length": max_length}
        if strategy == "beam":
            gen_kwargs.update({"num_beams": num_beams, "early_stopping": True})
        elif strategy == "sampling":
            gen_kwargs.update({
                "do_sample": True,
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p
            })
        out = model.generate(ids, **gen_kwargs)
        return tokenizer.decode(out[0], skip_special_tokens=True)
    except Exception as e:
        logging.error(f"Error in generate_recipe: {e}")
        return ""
