"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""
from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        else:
            return None


MAX_EGGS = 2
MAX_FLOUR = 300
MAX_MILk = 0.5
MAX_SUGAR = 100
MAX_OIl = 10
MAX_BUTTER = 120


class Pancake:

    def __init__(self, eggs=2, flour=300, milk=0.5, sugar=100, sunflower_oil=10, butter=120):
        self.eggs = eggs
        self.flour = flour
        self.milk = milk
        self.sugar = sugar
        self.sunflower_oil = sunflower_oil
        self.butter = butter

    def add_eggs(self, eggs):
        self.eggs += eggs

    def add_flour(self, flour):
        self.flour += flour

    def add_milk(self, milk):
        self.milk += milk

    def add_sugar(self, sugar):
        self.sugar += sugar

    def add_oil(self, oil):
        self.sunflower_oil += oil

    def add_butter(self, butter):
        self.butter += butter

    @property
    def eggs(self):
        return self._eggs

    @eggs.setter
    def eggs(self, value):
        if 0 <= value <= 2:
            self._eggs = value
        else:
            raise ValueError('Число яиц должно быть от 0 до 2-х')

    @property
    def flour(self):
        return self._flour

    @flour.setter
    def flour(self, value):
        if 0 <= value <= 300:
            self._flour = value
        else:
            raise ValueError('Количество муки должно быть от 0 до 300 гр.')

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, value):
        if 0 <= value <= 0.5:
            self._milk = value
        else:
            raise ValueError('Количество молока должно быть от 0 до 0.5 л.')

    @property
    def sugar(self):
        return self._sugar

    @sugar.setter
    def sugar(self, value):
        if 0 <= value <= 100:
            self._sugar = value
        else:
            raise ValueError('Количество сахара должно быть от 0 до 100 гр.')

    @property
    def sunflower_oil(self):
        return self._sunflower_oil

    @sunflower_oil.setter
    def sunflower_oil(self, value):
        if 0 <= value <= 10:
            self._sunflower_oil = value
        else:
            raise ValueError('Количество  подсолнечного масла должно быть от 0 до 10 мл.')

    @property
    def butter(self):
        return self._butter

    @butter.setter
    def butter(self, value):
        if 0 <= value <= 120:
            self._butter = value
        else:
            raise ValueError('Количество сливочного масла должно быть от 0 до 120 гр.')


class EggsHandler(AbstractHandler):
    def handle(self, pancake):
        if pancake.eggs < MAX_EGGS:
            deficit = MAX_EGGS - pancake.eggs
            pancake.add_eggs(deficit)
            print(f'Добавлено {deficit} яиц')
        if self._next_handler:
            return self._next_handler.handle(pancake)


class FlourHandler(AbstractHandler):
    def handle(self, pancake):
        if pancake.flour < MAX_FLOUR:
            deficit = MAX_FLOUR - pancake.flour
            pancake.add_flour(deficit)
            print(f'Добавлено {deficit} гр. муки')
        if self._next_handler:
            return self._next_handler.handle(pancake)


class MilkHandler(AbstractHandler):
    def handle(self, pancake):
        if pancake.milk < MAX_MILk:
            deficit = MAX_MILk - pancake.milk
            pancake.add_milk(deficit)
            print(f'Добавлено {round(deficit, 2)} л. молока')
        if self._next_handler:
            return self._next_handler.handle(pancake)


class SugarHandler(AbstractHandler):
    def handle(self, pancake):
        if pancake.sugar < MAX_SUGAR:
            deficit = MAX_SUGAR - pancake.sugar
            pancake.add_sugar(deficit)
            print(f'Добавлено {deficit} гр. сахара')
        if self._next_handler:
            return self._next_handler.handle(pancake)


class OilHandler(AbstractHandler):
    def handle(self, pancake):
        if pancake.sunflower_oil < MAX_OIl:
            deficit = MAX_OIl - pancake.sunflower_oil
            pancake.add_oil(deficit)
            print(f'Добавлено {deficit} мл. подсолнечного масла')
        if self._next_handler:
            return self._next_handler.handle(pancake)


class ButterHandler(AbstractHandler):
    def handle(self, pancake):
        if pancake.butter < MAX_BUTTER:
            deficit = MAX_BUTTER - pancake.butter
            pancake.add_butter(deficit)
            print(f'Добавлено {deficit} гр. сливочного масла')
        if self._next_handler:
            return self._next_handler.handle(pancake)


def add_deficit_items(recipe):
    eggs_handler = EggsHandler()
    flour_handler = FlourHandler()
    milk_handler = MilkHandler()
    sugar_handler = SugarHandler()
    oil_handler = OilHandler()
    butter_handler = ButterHandler()
    eggs_handler.set_next(flour_handler).set_next(milk_handler).\
        set_next(sugar_handler).set_next(oil_handler).set_next(butter_handler)

    eggs_handler.handle(recipe)


if __name__ == '__main__':
    recipe = Pancake(eggs=2, flour=220, milk=0.4, sugar=100, sunflower_oil=5, butter=110)
    add_deficit_items(recipe)