import requests
from ._settings import SYNTAXES


def get_html(url: str, headers: dict = {}) -> bytes:
    """
    """
    response = requests.get(url, headers=headers)
    return response.text


def get_metadata(html: bytes, url: str) -> dict:
    """
    """
    metadata = extruct.extract(
        html, base_url=get_base_url(url), syntaxes=SYNTAXES, uniform=True
    )["json-ld"]
    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]
    return metadata


def scrape(url: str) -> dict:
    """Parse structured data from a target page."""
    html = get_html(url)
    metadata = get_metadata(html, url)
    return metadata
