"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""
from abc import ABC, abstractmethod
import yaml


class AbstractFirst(ABC):
    @abstractmethod
    def make_first(self):
        pass


class VeganFirst(AbstractFirst):
    def make_first(self, menu):
        return f'Готовим {menu["vegan"]}'


class ChildFirst(AbstractFirst):
    def make_first(self, menu):
        return f'Готовим {menu["child"]}'


class ChineseFirst(AbstractFirst):
    def make_first(self, menu):
        return f'Готовим {menu["chinese"]}'


class AbstractSecond(ABC):
    @abstractmethod
    def make_second(self, menu):
        pass


class VeganSecond(AbstractSecond):
    def make_second(self, menu):
        return f'Готовим {menu["vegan"]}'


class ChildSecond(AbstractSecond):
    def make_second(self, menu):
        return f'Готовим {menu["child"]}'


class ChineseSecond(AbstractSecond):
    def make_second(self, menu):
        return f'Готовим {menu["chinese"]}'


class AbstractThird(ABC):
    @abstractmethod
    def make_third(self, menu):
        pass


class VeganThird(AbstractThird):
    def make_third(self, menu):
        return f'Готовим {menu["vegan"]}'


class ChildThird(AbstractThird):
    def make_third(self, menu):
        return f'Готовим {menu["child"]}'


class ChineseThird(AbstractThird):
    def make_third(self, menu):
        return f'Готовим {menu["chinese"]}'


class AbstractFactory(ABC):
    @abstractmethod
    def get_first(self):
        pass

    @abstractmethod
    def get_second(self):
        pass

    @abstractmethod
    def get_third(self):
        pass


class ChineseFactory(AbstractFactory):
    def get_first(self):
        return ChineseFirst()

    def get_second(self):
        return ChineseSecond()

    def get_third(self):
        return ChineseThird()


class ChildFactory(AbstractFactory):
    def get_first(self):
        return ChildFirst()

    def get_second(self):
        return ChildSecond()

    def get_third(self):
        return ChildThird()


class VeganFactory(AbstractFactory):
    def get_first(self):
        return VeganFirst()

    def get_second(self):
        return VeganSecond()

    def get_third(self):
        return VeganThird()


def client_code(factory, day):
    with open('./menu.yml') as file:
        menu = yaml.load(file)
    for key, value in menu.items():
        if key == day.capitalize():
            menu = menu[key]
    first = factory.get_first()
    second = factory.get_second()
    third = factory.get_third()
    print(first.make_first(menu['first_courses']))
    print(second.make_second(menu['second_courses']))
    print(third.make_third(menu['drinks']))


if __name__ == '__main__':
    weekday = input('Enter a day of week:')
    client_code(VeganFactory(), weekday)
    print('-'*50)
    client_code(ChildFactory(), weekday)
    print('-' * 50)
    client_code(ChineseFactory(), weekday)


