from src.models.ingredient import Ingredient  # noqa: F401, E261, E501

from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient_carne = Ingredient("carne")
    assert ingredient_carne.name == "carne"
    assert ingredient_carne.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient_carne_hash = Ingredient("carne").__hash__()
    assert ingredient_carne_hash == hash("carne")

    ingredient_carne_eq = Ingredient("carne").__eq__(ingredient_carne)
    assert ingredient_carne_eq

    ingredient_carne_repr = Ingredient("carne").__repr__()
    assert ingredient_carne_repr == "Ingredient('carne')"
