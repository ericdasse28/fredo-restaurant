from fredo_restaurant.cooking_service import CookingService
from fredo_restaurant.dish import PastaType, Salsa, Topping
from fredo_restaurant.order import Order


def make_test_order(pasta, salsa, topping=None):
    order_content = {"pasta": pasta, "salsa": salsa, "topping": topping}
    order = Order(
        order_content=order_content,
        location="The place over there!",
        comment="Some blabla",
        customer_name="Veronica",
    )

    return order


def test_cooking_service_can_take_penne_carbonara_order():
    cooking_service = CookingService()
    penne_carbonara_order = make_test_order(
        pasta=PastaType.PENNE,
        salsa=Salsa.CARBONARA,
    )

    dish_to_cook = cooking_service.take_order(penne_carbonara_order)

    assert dish_to_cook.pasta == PastaType.PENNE
    assert dish_to_cook.salsa == Salsa.CARBONARA
    assert dish_to_cook.topping is None


def test_cooking_service_can_take_spaghetti_bolognaise_order():
    cooking_service = CookingService()
    spaghetti_bolognaise_order = make_test_order(
        pasta=PastaType.SPAGHETTI,
        salsa=Salsa.BOLOGNAISE,
    )

    dish_to_cook = cooking_service.take_order(spaghetti_bolognaise_order)

    assert dish_to_cook.pasta == PastaType.SPAGHETTI
    assert dish_to_cook.salsa == Salsa.BOLOGNAISE
    assert dish_to_cook.topping is None


def test_cooking_service_can_take_penne_carbonara_with_mushrooms_order():
    cooking_service = CookingService()
    penne_carbonara_with_mushrooms = make_test_order(
        pasta=PastaType.PENNE,
        salsa=Salsa.CARBONARA,
        topping=Topping.MUSHROOMS,
    )

    dish_to_cook = cooking_service.take_order(penne_carbonara_with_mushrooms)

    assert dish_to_cook.pasta == PastaType.PENNE
    assert dish_to_cook.salsa == Salsa.CARBONARA
    assert dish_to_cook.topping == Topping.MUSHROOMS
