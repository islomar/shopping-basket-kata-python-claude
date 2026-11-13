<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

- Empty shopping cart returns 0 total price.
- Total price for one apple --> 25 cents
- Total price for one banana --> 35 cents
- Total price for one orange --> 70 cents
- Total price for list of ["apple", "apple"] → 50 cents (discount 2x1 in apples)
- Total price for list of ["apple", "orange", "apple"] → 1.20 euros (discount 2x1 applies to any combination of apples and oranges)

Part 5 - Implement a new promotion: Bananas take part in the same promotion as apples,
 and the cheapest one should be given first.
[banana, banana, apple, apple, apple] = pay 2 bananas (discount 2 apples) + 1 extra apple
[banana, banana, banana, apple apple] = pay 2 bananas (discount 2 apples) + 1 extra banana
[banana, apple, apple, apple, apple] = pay 1 banana + [apply promo to remaining] (pay 2 apples, discount 2 apples)
[banana, banana, banana, banana, apple] = pay 3 bananas + discount 1 banana and 1 apple
