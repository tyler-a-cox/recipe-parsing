import extruct
import requests

SCHEMA_HOST = "schema.org"
SCHEMA_NAMES = ["Recipe", "WebPage"]
SYNTAXES = ["json-ld"]


class Schema:
    def __init__(self, url: str):
        """
        """
        pass

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

    def yields(self) -> float:
        """
        """
        pass

    def instructions(self) -> float:
        """
        """
        pass

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
        pass

    def image(self) -> str:
        """
        """
        pass

    def description(self) -> str:
        """
        """
        pass

    def url(self) -> str:
        """
        """
        pass
