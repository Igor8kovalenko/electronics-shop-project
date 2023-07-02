"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Product", 10000, 20)
    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item = Item("Product", 10000, 20)
    Item.pay_rate = 0.8  # set the discount to 20%
    item.apply_discount()
    assert item.price == 8000