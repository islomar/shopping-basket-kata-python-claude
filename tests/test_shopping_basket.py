import pytest
from expects import equal, expect

from src.shopping_basket import ShoppingBasket, Item


class TestShoppingBasket:
    @pytest.mark.parametrize("items,expected", [
        ([], 0.00),
        ([Item.APPLE], 0.25),
        ([Item.BANANA], 0.35),
        ([Item.ORANGE], 0.70),
    ])
    def test_single_item_without_promotion(self, items: list[Item], expected: float) -> None:
        basket = ShoppingBasket(items)

        result = basket.calculate_total()

        expect(result).to(equal(pytest.approx(expected)))

    @pytest.mark.parametrize("items,expected", [
        ([Item.APPLE, Item.APPLE], 0.25),  # 2-for-1: pay for 1 apple
        ([Item.APPLE, Item.ORANGE, Item.APPLE], 0.95),  # 2-for-1: pay for 2 most expensive (orange + apple)
        ([Item.APPLE, Item.APPLE, Item.APPLE], 0.50),  # 2-for-1: pay for 2 out of 3 apples
        ([Item.APPLE, Item.APPLE, Item.APPLE, Item.APPLE], 0.50),  # 2-for-1: pay for 2 out of 4 apples
        ([Item.APPLE, Item.BANANA, Item.APPLE], 0.60),  # 2-for-1 on apples + full price banana
        ([Item.ORANGE, Item.ORANGE], 0.70),  # 2-for-1: pay for 1 orange
        ([Item.BANANA, Item.BANANA, Item.APPLE, Item.APPLE, Item.APPLE], 0.85),  # 2-for-1 with bananas: pay 2 bananas + 1 apple (discount 2 apples)
        ([Item.BANANA, Item.BANANA, Item.BANANA, Item.APPLE, Item.APPLE], 0.95),  # 2-for-1 with 3 bananas + 2 apples: pay for 3 most expensive
        ([Item.BANANA, Item.APPLE, Item.APPLE, Item.APPLE, Item.APPLE], 0.85),  # 1 banana + 4 apples: pay for banana + 2 apples
        ([Item.BANANA, Item.BANANA, Item.BANANA, Item.BANANA, Item.APPLE], 1.40),  # 4 bananas + 1 apple: pay 3 bananas + 1 apple (discount 1 banana)
    ])
    def test_items_with_promotion(self, items: list[Item], expected: float) -> None:
        basket = ShoppingBasket(items)

        result = basket.calculate_total()

        expect(result).to(equal(pytest.approx(expected)))
