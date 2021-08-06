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

    @property
    def title(self) -> str:
        """
        """
        pass

    @property
    def author(self) -> str:
        """
        """
        pass

    @property
    def time(self) -> float:
        """
        """
        pass

    @property
    def yields(self) -> float:
        """
        """
        pass

    @property
    def instructions(self) -> float:
        """
        """
        pass

    @property
    def ratings(self) -> float:
        """
        """
        pass

    @property
    def reviews(self) -> list:
        """
        """
        pass

    @property
    def cuisine(self) -> str:
        """
        """
        pass

    @property
    def nutrition(self) -> dict:
        """
        """
        pass

    @property
    def ingredients(self) -> list:
        """
        """
        pass

    @property
    def image(self) -> str:
        """
        """
        pass

    @property
    def description(self) -> str:
        """
        """
        pass

    @property
    def url(self) -> str:
        """
        """
        pass
