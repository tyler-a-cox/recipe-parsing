import os
import spacy
import pkg_resources
from typing import Optional
from .ingredient import Ingredient
from ._utils import stardardize_input
from pkg_resources import resource_string


class IngredientParser:
    def __init__(self, model: Optional[str] = "ner"):
        """
        """
        # Try-except load this
        dirname = os.path.dirname(__file__)
        stream = os.path.join(dirname, "models/ner")
        # stream = resource_string("recipe_parser.ingredient_parser", "ner")
        # print(stream)
        self.nlp = spacy.load(stream)

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
