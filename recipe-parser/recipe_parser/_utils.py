import re
import ingredient_parser

UNITS = [
    "CUP",
    "PINCH",
    "OUNCE",
    "POUND",
    "TEASPOON",
    "TABLESPOON",
    "OZ",
    "TBSP",
    "TSP",
    "LB",
]


ABBREVIATION = {
    "OZ": "OUNCE",
    "TBSP": "TABLESPOON",
    "TSP": "TEASPOON",
    "LB": "POUND",
}
