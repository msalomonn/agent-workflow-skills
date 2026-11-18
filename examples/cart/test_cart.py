import unittest

from cart import total_cents


class CartTests(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(total_cents([]), 0)

    def test_single_item(self):
        self.assertEqual(total_cents([(200, 1)]), 200)

    def test_quantities_change_total(self):
        self.assertEqual(total_cents([(200, 2), (125, 1)]), 525)

    def test_zero_quantity_contributes_nothing(self):
        self.assertEqual(total_cents([(200, 0)]), 0)


if __name__ == '__main__':
    unittest.main()
