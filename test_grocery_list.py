#!/usr/bin/env python

import unittest
from grocery_list import GroceryList

class GroceryListTest(unittest.TestCase):

    def setUp(self):
        self.groceries = GroceryList()

    def test_can_view_a_grocery_list(self):
        self.groceries.add('Flank steak')
        self.groceries.add('Potatoes')
        self.groceries.add('Eggs')

        results = self.groceries.view()

        expected_results = ('Flank steak', 'Potatoes', 'Eggs')
        self.assertEqual(expected_results, results)

    def test_can_create_grocery_list(self):
        self.assertIsInstance(self.groceries, GroceryList)

    def test_can_add_to_grocery_list(self):
        self.groceries.add('Flank steak')

        self.assertTrue('Flank steak' in self.groceries.items)

if __name__ == '__main__':
    unittest.main()
