"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item
import pytest
import os
path = os.path.join('..', 'tests', 'test_items.csv')

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    item1 = Item("Product", 10000, 20)
    assert item1.calculate_total_price() == 200000

def test_apply_discount():
    item1 = Item("Product", 10000, 20)
    Item.pay_rate = 0.8  # set the discount to 20%
    item1.apply_discount()
    assert item1.price == 8000

def test_name_setter():
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


@pytest.mark.parametrize("a, result", [('5', 5),
                                       ('5.0', 5),
                                       ('5.5', 5)])
def test_string_to_number(a, result):
    assert Item.string_to_number(a) == result

def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000.0

