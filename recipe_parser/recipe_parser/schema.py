import extruct
import requests
from typing import Optional, Union
from ._utils import *
from ._settings import *
from ._exceptions import *


class Schema:
    def __init__(self, url: str, headers: Optional[dict] = HEADERS):
        """
        """
        self.url = url
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
            raise NoSchemaFound(url)

    def title(self) -> str:
        """
        """
        pass

    def author(self) -> str:
        """
        """
        pass

    def time(self) -> float:
        """
        """
        pass

    def yields(self) -> Union[str, list]:
        """
        """
        self.data.get("recipeYield", [])

    def instructions(self) -> list:
        """
        """
        instructions = self.data.get("recipeInstructions", "")

        if isinstance(instructions, dict):
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
        pass

    def reviews(self) -> list:
        """
        """
        pass

    def cuisine(self) -> str:
        """
        """
        pass

    def nutrition(self) -> dict:
        """
        """
        pass

    def ingredients(self) -> list:
        """
        """
        return self.data.get("recipeIngredient", "")

    def image(self) -> str:
        """
        """
        pass

    def description(self) -> str:
        """
        """
        pass
