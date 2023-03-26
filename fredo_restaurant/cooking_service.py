class Dish:
    def __init__(self, pasta, salsa, topping):
        self.pasta = pasta
        self.salsa = salsa
        self.topping = topping


class CookingService:
    def take_order(self, order):
        pasta = order.content["pasta"]
        salsa = order.content["salsa"]
        topping = order.content["topping"]

        return Dish(pasta=pasta, salsa=salsa, topping=topping)
