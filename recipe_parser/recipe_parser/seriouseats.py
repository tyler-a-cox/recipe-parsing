import inspect
from bs4 import BeautifulSoup
from typing import Optional, Union

from ._settings import HEADERS
from ._schema import DefaultSchema
from ._utils import clean_vulgar_fraction, clean_unicode


class SeriousEats(DefaultSchema):
    """
    """

    def __init__(self, url: str, headers: Optional[dict] = HEADERS):
        """
        url : str
            url
        headers : dict, Optional
            dict
        """
        super().__init__(url)
        self.soup = BeautifulSoup(self.page, "html.parser")

    def title(self):
        """
        """
        return self.soup.find("h1", {"class": "heading__title"}).get_text()

    def description(self):
        """
        """
        description = self.soup.find("h2", {"class": "heading__subtitle"})
        if description:
            return description.get_text()

        return ""

    def instructions(self):
        """
        """
        tags = self.soup.find_all("li", {"class": "mntl-sc-block-group--LI"})
        return [tag.get_text().strip() for tag in tags]

    def author(self):
        """
        """
        author = self.soup.find("meta", {"name": "sailthru.author"})
        return author["content"] if author else None

    def rating(self):
        """
        """
        return self.soup.find("p", {"id": "recipe-rating_1-0"}).get_text().strip()

    def yields(self):
        """
        """
        return (
            self.soup.find(
                "div", {"class": "loc recipe-serving project-meta__recipe-serving"}
            )
            .find("span", {"class": "meta-text__data"})
            .get_text()
        )

    def time(self) -> float:
        """
        """
        return (
            self.soup.find("div", {"class": "loc total-time project-meta__total-time"})
            .find("span", {"class": "meta-text__data"})
            .get_text()
        )

    def image(self) -> Union[str, list]:
        """
        """
        tag = self.soup.find("meta", {"property": "og:image"})
        return tag.get("content")

    def category(self) -> list:
        """
        """
        tags = self.soup.find_all("a", {"class": "link-list__link"})
        return [tag.get_text() for tag in tags]

    def ingredients(self) -> list:
        """
        """
        tags = self.soup.findAll("li", {"class": "ingredient"})
        return [clean_unicode(tag.get_text().strip()) for tag in tags]

    def properties(self) -> dict:
        """
        """
        values = {}
        for method, f in inspect.getmembers(self, predicate=inspect.ismethod):
            if method != "properties" and not method.startswith("_"):
                values[method] = f()

        return values
