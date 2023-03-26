import pytest

from fredo_restaurant.cooking_service import CookingService
from fredo_restaurant.dish import PastaType, Salsa, Topping
from fredo_restaurant.order import Order


@pytest.fixture
def penne_carbonara_order():
    penne_order_content = {
        "pasta": PastaType.PENNE,
        "salsa": Salsa.CARBONARA,
        "topping": None,
    }

    order = Order(
        order_content=penne_order_content,
        location="The place over there!",
        comment="Some blabla",
        customer_name="Aline",
    )

    return order


@pytest.fixture
def penne_carbonara_with_mushrooms():
    penne_carbonara_with_mushrooms = {
        "pasta": PastaType.PENNE,
        "salsa": Salsa.CARBONARA,
        "topping": Topping.MUSHROOMS,
    }

    order = Order(
        order_content=penne_carbonara_with_mushrooms,
        location="The place over there!",
        comment="Some blabla",
        customer_name="Aline",
    )

    return order


@pytest.fixture
def spaghetti_bolognaise_order():
    spaghetti_bolognaise_content = {
        "pasta": PastaType.SPAGHETTI,
        "salsa": Salsa.BOLOGNAISE,
        "topping": None,
    }

    order = Order(
        order_content=spaghetti_bolognaise_content,
        location="The place over there!",
        comment="Some blabla",
        customer_name="Axel",
    )

    return order


def test_cooking_service_can_take_penne_carbonara_order(penne_carbonara_order):
    cooking_service = CookingService()

    dish_to_cook = cooking_service.take_order(penne_carbonara_order)

    assert dish_to_cook.pasta == PastaType.PENNE
    assert dish_to_cook.salsa == Salsa.CARBONARA
    assert dish_to_cook.topping is None


def test_cooking_service_can_take_spaghetti_bolognaise_order(
    spaghetti_bolognaise_order,
):
    cooking_service = CookingService()

    dish_to_cook = cooking_service.take_order(spaghetti_bolognaise_order)

    assert dish_to_cook.pasta == PastaType.SPAGHETTI
    assert dish_to_cook.salsa == Salsa.BOLOGNAISE
    assert dish_to_cook.topping is None


def test_cooking_service_can_take_penne_carbonara_with_mushrooms_order(
    penne_carbonara_with_mushrooms,
):
    cooking_service = CookingService()

    dish_to_cook = cooking_service.take_order(penne_carbonara_with_mushrooms)

    assert dish_to_cook.pasta == PastaType.PENNE
    assert dish_to_cook.salsa == Salsa.CARBONARA
    assert dish_to_cook.topping == Topping.MUSHROOMS
