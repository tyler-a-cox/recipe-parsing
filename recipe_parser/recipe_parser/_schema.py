import inspect
import extruct
import requests
from typing import Optional, Union

from ._utils import *
from ._settings import *
from ._exceptions import *

# Nutrition API


class DefaultSchema:
    def __init__(self, url: str, headers: Optional[dict] = HEADERS):
        """
        url : str
            url
        headers : dict, Optional
            dict
        """
        self.url = url
        self.page = get_html(url)
        self.metadata = scrape(url=url, headers=headers)

        metatype = self.metadata.get("@type", "")
        graphtype = self.metadata.get("@graph", None)

        if metatype.lower() == "recipe":
            self.data = self.metadata

        elif isinstance(graphtype, list):
            for graph_item in graphtype:
                if graph_item.get("@type", "").lower() == "recipe":
                    self.data = graph_item
                    return

        else:
            self.data = {}

    def title(self) -> str:
        """
        """
        return self.data.get("name", "")

    def author(self) -> str:
        """
        """
        author = self.data.get("author", "")
        if isinstance(author, dict):
            return author.get("name", "")

        if isinstance(author, list) and isinstance(author[0], dict):
            return author[0].get("name", "")

        return author

    def time(self) -> float:
        """
        """
        a = self.data.get("totalTime", "")
        # normalize text
        return a

    def yields(self) -> Union[str, list]:
        """
        """
        return self.data.get("recipeYield", [])

    def instructions(self) -> list:
        """
        """
        instructions = self.data.get("recipeInstructions", "")

        if isinstance(instructions, list):
            text = []
            for instruct in instructions:
                if instruct.get("@type", "").lower() == "howtostep":
                    text.append(instruct.get("text"))

            return text

        else:
            return instructions

    def ratings(self) -> float:
        """
        """
        return self.data.get("aggregateRating", {}).get("ratingValue", "")

    def reviews(self) -> list:
        """
        """
        return self.data.get("ratings", None)

    def category(self) -> list:
        """
        """
        return self.data.get("recipeCategory", "")

    def cuisine(self) -> str:
        """
        """
        return self.data.get("recipeCuisine", "")

    def nutrition(self, query: bool = False) -> dict:
        """
        """
        nutrition = self.data.get("nutrition", {})
        if len(nutrition) == 0 and query:
            return {}

        return nutrition

    def ingredients(self) -> list:
        """
        """
        ingredients = self.data.get("recipeIngredient", "")
        return [clean_vulgar_fraction(ingredient) for ingredient in ingredients]

    def image(self) -> Union[str, list]:
        """
        """
        image = self.data.get("image", [])
        if isinstance(image, dict):
            return image.get("url", "")

        return image

    def description(self) -> str:
        """
        """
        return self.data.get("description", "")

    def keywords(self) -> dict:
        """
        """
        return self.data.get("keywords", "")

    def properties(self) -> dict:
        """
        """
        values = {}
        for method, f in inspect.getmembers(self, predicate=inspect.ismethod):
            if method != "properties" and not method.startswith("_"):
                values[method] = f()

        return values
