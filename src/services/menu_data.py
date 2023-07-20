import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, src_path: str) -> None:
        self.dishes = self.dishes(src_path)

    def dishes(self, path):
        dishes = {}
        with open(path, "r") as file:
            rdr = csv.reader(file)
            next(rdr)

            for line in rdr:
                dish_name, price, ingredient_name, recipe_amount = line

                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, float(price))

                ingredient = Ingredient(ingredient_name)
                dishes[dish_name].add_ingredient_dependency(
                    ingredient, int(recipe_amount)
                )

        return set(dishes.values())
