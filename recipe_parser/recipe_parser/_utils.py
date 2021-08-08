import re
import extruct
import requests
from w3lib.html import get_base_url

from ._settings import SYNTAXES


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
        html, base_url=get_base_url(url), syntaxes=SYNTAXES, uniform=uniform
    )["json-ld"]

    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]

    return metadata


def scrape(url: str, headers: dict = {}) -> dict:
    """Parse structured data from a target page."""
    html = get_html(url, headers=headers)
    metadata = get_metadata(html, url)
    return metadata
