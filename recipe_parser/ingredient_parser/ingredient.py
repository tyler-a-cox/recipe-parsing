from dataclasses import dataclass


@dataclass
class Ingredient:
    product: str
    quantity: float
    unit: str
    line: str