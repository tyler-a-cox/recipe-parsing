from urllib.parse import urlparse

from ._schema import DefaultSchema
from ._utils import get_metadata, clean_unicode
from .seriouseats import SeriousEats
from .allrecipes import AllRecipes

parsers = {
    "www.seriouseats.com": SeriousEats,
    "www.allrecipes.com": AllRecipes,
}


def scrape_page(url):
    parsed = urlparse(url)
    parser = parsers.get(parsed.netloc, DefaultSchema)
    return parser(url).properties()
