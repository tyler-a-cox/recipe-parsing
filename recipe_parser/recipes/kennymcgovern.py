from ._abstract import DefaultSchema
from ._utils import get_minutes, get_yields, normalize_string


class KennyMcGovern(DefaultSchema):
    @classmethod
    def host(cls):
        return "kennymcgovern.com"

    def title(self):
        return self.soup.find("div", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("span", {"class": "wprm-recipe-total_time"}).parent
        )

    def yields(self):
        yields = self.soup.find("span", {"class": "wprm-recipe-servings"}).get_text()

        return get_yields("{} servings".format(yields))

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll(
            "div", {"class": "wprm-recipe-instruction-text"}
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )