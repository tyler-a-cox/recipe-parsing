import spacy
from .ingredient import Ingredient
from .utils import stardardize_input


class IngredientParser:
    def __init__(self, model: str):
        """
        """
        # Try-except load this
        nlp = spacy.load(model)

    def parse(self, line: str) -> Ingredient:
        """
        """
        line = stardardize_input(line)
        doc = nlp(line)
