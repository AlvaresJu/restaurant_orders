from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    massa_lasanha = Ingredient("massa de lasanha")
    queijo = Ingredient("queijo mussarela")
    molho_tomate = Ingredient("molho de tomate")

    lasanha_queijo = Dish("lasanha de queijo", 28.45)
    frango_assado = Dish("frango assado", 33.80)

    assert lasanha_queijo.name == "lasanha de queijo"
    assert lasanha_queijo.price == 28.45
    assert lasanha_queijo.recipe == {}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pizza", "25%")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("salada", 0)
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("arroz", -25)

    assert repr(lasanha_queijo) == "Dish('lasanha de queijo', R$28.45)"

    assert hash(lasanha_queijo) == hash("Dish('lasanha de queijo', R$28.45)")
    assert hash(lasanha_queijo) != hash(frango_assado)
    assert hash(lasanha_queijo) == hash(Dish("lasanha de queijo", 28.45))

    assert (lasanha_queijo == lasanha_queijo) is True
    assert (lasanha_queijo == frango_assado) is False
    assert (lasanha_queijo != frango_assado) is True

    lasanha_queijo.add_ingredient_dependency(massa_lasanha, 5)
    lasanha_queijo.add_ingredient_dependency(queijo, 15)
    lasanha_queijo.add_ingredient_dependency(molho_tomate, 7)

    assert massa_lasanha in lasanha_queijo.recipe
    assert queijo in lasanha_queijo.recipe
    assert molho_tomate in lasanha_queijo.recipe

    assert lasanha_queijo.recipe[massa_lasanha] == 5
    assert lasanha_queijo.recipe[queijo] == 15
    assert lasanha_queijo.recipe[molho_tomate] == 7

    assert lasanha_queijo.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }

    assert lasanha_queijo.get_ingredients() == {
        massa_lasanha,
        queijo,
        molho_tomate,
    }
