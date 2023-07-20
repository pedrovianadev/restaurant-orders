from src.models.dish import Dish # noqa: F401, E261, E501
from models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    ingredient = Ingredient("salmão")
    dish_salmon = Dish("Salmão ao Forno", 40.0)
    assert dish_salmon.name == "Salmão ao Forno"
    assert dish_salmon.recipe == {}

    dish_salmon.add_ingredient_dependency(ingredient, 1)
    assert dish_salmon.recipe == {ingredient: 1}
    assert dish_salmon.get_ingredients() == {ingredient}

    assert dish_salmon.__eq__(dish_salmon)

    assert dish_salmon.__hash__() == hash("Dish('Salmão ao Forno', R$40.00)")

    assert dish_salmon.get_restrictions() == ingredient.restrictions

    with pytest.raises(TypeError):
        Dish("Salmão ao Forno", "40.0")

    with pytest.raises(ValueError):
        Dish("Salmão ao Forno", -40.0)
