from enum import Enum


class Item(Enum):
    APPLE = "apple"
    BANANA = "banana"
    ORANGE = "orange"


class ShoppingBasket:
    PRICES = {Item.APPLE: 0.25, Item.BANANA: 0.35, Item.ORANGE: 0.70}
    PROMOTIONAL_ITEMS = frozenset({Item.APPLE, Item.BANANA, Item.ORANGE})

    def __init__(self, items: list[Item]):
        self.items = items

    def calculate_total(self) -> float:
        promotional_prices = self._extract_promotional_prices()
        promotional_total = self._apply_two_for_one_promotion(promotional_prices)
        regular_total = self._calculate_regular_total()
        return promotional_total + regular_total

    def _extract_promotional_prices(self) -> list[float]:
        promotional_prices = []

        for item in self.items:
            if self._is_promotional_item(item):
                promotional_prices.append(self._get_item_price(item))

        return promotional_prices

    def _calculate_regular_total(self) -> float:
        regular_total = 0.0

        for item in self.items:
            if not self._is_promotional_item(item):
                regular_total += self._get_item_price(item)

        return regular_total

    def _is_promotional_item(self, item: Item) -> bool:
        return item in self.PROMOTIONAL_ITEMS

    def _get_item_price(self, item: Item) -> float:
        return self.PRICES.get(item, 0.0)

    def _apply_two_for_one_promotion(self, promotional_prices: list[float]) -> float:
        sorted_prices_descending = sorted(promotional_prices, reverse=True)
        return sum(price for index, price in enumerate(sorted_prices_descending) if index % 2 == 0)
