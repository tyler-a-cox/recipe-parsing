import extruct
import requests
from typing import Optional
from ._utils import *
from ._settings import *


class Schema:
    def __init__(self, url: str, headers: Optional[dict] = HEADERS):
        """
        """
        self.url = url
        self.metadata = scrape(url=url, headers=headers)

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
