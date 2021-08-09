import spacy
from typing import Optional
from .ingredient import Ingredient
from ._utils import stardardize_input


class IngredientParser:
    def __init__(self, model: Optional[str] = "recipe_parser/ingredient_parser/ner"):
        """
        """
        # Try-except load this
        self.nlp = spacy.load(model)

    def parse(self, line: str) -> Ingredient:
        """
        """
        # line = stardardize_input(line)
        doc = self.nlp(line)
        return doc

        product = ...
        quantity = ...
        unit = ...

        return Ingredient(product=product, quantity=quantity, unit=unit, line=line)
