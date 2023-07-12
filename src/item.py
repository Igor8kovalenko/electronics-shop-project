
import os
import csv

# path = os.path.join('..', 'src', 'items.csv')
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self._name}'
    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            with open(path, encoding='windows-1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]

        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')

    @classmethod
    def item_name(cls, name):
        if len(name) <= 10 :
            name = [x for x in name.split() if x]
            return name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        elif len(name) > 10:
            self.__name = name[:10]


    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_item_price = self.price * self.quantity
        return total_item_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))



