"""
Factory Method (Фабричный метод)
Также известен как Виртуальный конструктор (Virtual Constructor)

Порождающий шаблон проектирования, предоставляющий подклассам (дочерним классам) интерфейс для создания экземпляров
  некоторого класса. В момент создания наследники могут определить, какой класс создавать.
  Иными словами, данный шаблон делегирует создание объектов наследникам родительского класса.
  Это позволяет использовать в коде программы не специфические классы,
  а манипулировать абстрактными объектами на более высоком уровне.

Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс инстанцировать.
  Фабричный метод позволяет классу делегировать создание подклассов. Используется, когда:
 * Классу заранее неизвестно, объекты каких подклассов ему нужно создавать.
 * Класс спроектирован так, чтобы объекты, которые он создаёт, специфицировались подклассами.
 * Класс делегирует свои обязанности одному из нескольких вспомогательных подклассов, и планируется локализовать
     знание о том, какой класс принимает эти обязанности на себя

Структура
 * Product — продукт. Определяет интерфейс объектов, создаваемых абстрактным методом;
 * ConcreteProduct — конкретный продукт, реализует интерфейс Product;
 * Creator — создатель. Объявляет фабричный метод, который возвращает объект типа Product. Может также содержать
     реализацию этого метода «по умолчанию»; может вызывать фабричный метод для создания объекта типа Product;
 * ConcreteCreator — конкретный создатель. Переопределяет фабричный метод таким образом, чтобы он создавал и
     возвращал объект класса ConcreteProduct.


Достоинства:
 * Позволяет сделать код создания объектов более универсальным, не привязываясь к конкретным классам (ConcreteProduct),
     а оперируя лишь общим интерфейсом (Product)
 * Позволяет установить связь между параллельными иерархиями классов.

Недостатки:
 * Необходимость создавать наследника Creator для каждого нового типа продукта (ConcreteProduct).

Смысл шаблона Фабрика – инкапсулировать логику создания новых объектов.
"""


from abc import ABC, abstractmethod


class Product(ABC):  # абстрактное колесо
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """

    @abstractmethod
    def operation(self):  # надуть абстрактное колесо
        pass


"""
Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""


class ConcreteProduct1(Product):  # колесо автомобиля
    def operation(self):  # надуть колесо
        return "{Результат операции ConcreteProduct1}"


class ConcreteProduct2(Product):  # колесо велосипеда
    def operation(self):  # надуть колесо
        return "{Результат операции ConcreteProduct2}"


class Creator(ABC):  # создатель колес
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
    метода.
    """

    @abstractmethod
    def factory_method(self):  # создадим какое-то колесо
        """
        Обратите внимание, что Создатель может также обеспечить реализацию
        фабричного метода по умолчанию.
        """
        pass

    def some_operation(self):  # сделаем что-то полезное
        """
        Также заметьте, что, несмотря на название, основная обязанность
        Создателя не заключается в создании продуктов. Обычно он содержит
        некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту
        бизнес-логику, переопределяя фабричный метод и возвращая из него другой
        тип продукта.
        """

        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()  # сделаем какое-то колесо

        # Далее, работаем с этим продуктом.
        # надуем какае-то колесо
        result = f"Создатель: Код создателя только что выполнен, и вернул {product.operation()}"

        return result


"""
Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип
результирующего продукта.
"""


class ConcreteCreator1(Creator):  # создатель колес автомобиля
    """
    Обратите внимание, что сигнатура метода по-прежнему использует тип
    абстрактного продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """

    def factory_method(self):
        return ConcreteProduct1()  # конкертное колесо автомобиля


class ConcreteCreator2(Creator):  # создатель колес велосипеда
    def factory_method(self):
        return ConcreteProduct2()  # конкретное колесо велосипеда


def client_code(creator):
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """

    print(f"Клиент: Я не знаю, какой конкретный класс у создателя, но операция все равно работает\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("Приложение: Запущено с ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("Приложение: Запущено с ConcreteCreator2")
    client_code(ConcreteCreator2())
