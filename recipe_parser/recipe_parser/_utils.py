import re
import extruct
import requests
import unicodedata
from w3lib.html import get_base_url

from ._settings import SYNTAXES

UNITS = {
    "(tps.|teaspoons)": "teaspoon",
    "(tbps.|tbps|tablespoons)": "tablespoon",
}


def clean_unicode(string):
    """
    """
    cleaned = string.replace(u"\u2009", " ")
    cleaned = clean_vulgar_fraction(cleaned)
    return cleaned.replace("⁄", "/")


def clean_vulgar_fraction(string):
    cleaned = [
        unicodedata.normalize("NFKC", char)
        if unicodedata.name(char).startswith("VULGAR FRACTION")
        else char
        for char in string
    ]
    return "".join(cleaned)


def cleanhtmltags(raw_html):
    """
    """
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def get_html(url: str, headers: dict = {}) -> bytes:
    """
    """
    response = requests.get(url, headers=headers)
    return response.text


def get_metadata(html: bytes, url: str, uniform: bool = True) -> dict:
    """
    """
    metadata = extruct.extract(
        html,
        base_url=get_base_url(url),
        syntaxes=SYNTAXES,
        uniform=uniform,
        errors="log",
    )

    try:
        metadata = metadata["json-ld"]

    except KeyError:
        return {}

    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]

    return metadata


def scrape(url: str, headers: dict = {}) -> dict:
    """Parse structured data from a target page."""
    html = get_html(url, headers=headers)
    metadata = get_metadata(html, url)
    return metadata
