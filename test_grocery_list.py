#!/usr/bin/env python

import unittest
from unittest.mock import patch, call

from grocery_list import GroceryList

class GroceryListTest(unittest.TestCase):

    def setUp(self):
        self.groceries = GroceryList()

    def test_can_view_a_grocery_list(self):
        self.groceries.add('Flank steak')
        self.groceries.add('Potatoes')
        self.groceries.add('Eggs')

        with patch('builtins.print') as mock_print:
            self.groceries.view()
            calls = [call('Flank steak'), call('Potatoes'), call('Eggs')]
            mock_print.assert_has_calls(calls)

    def test_can_create_grocery_list(self):
        self.assertIsInstance(self.groceries, GroceryList)

    def test_can_add_to_grocery_list(self):
        self.groceries.add('Flank steak')

        self.assertTrue('Flank steak' in self.groceries.items)

class GroceryListFromFileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('test_data.txt', 'w') as f:
            f.write('Flank steak\n')
            f.write('Potatoes\n')
            f.write('Eggs\n')

    @classmethod
    def tearDownClass(cls):
        import os
        os.remove('test_data.txt')

    def test_can_view_a_grocery_list(self):
        groceries = GroceryList(file='test_data.txt')

        with patch('builtins.print') as mock_print:
            groceries.view()
            calls = [call('Flank steak'), call('Potatoes'), call('Eggs')]
            mock_print.assert_has_calls(calls)

    def test_can_add_to_existing_grocery_list(self):
        groceries = GroceryList(file='test_data.txt')

        calls = [call('Flank steak'), call('Potatoes'), call('Eggs')]
        with patch('builtins.print') as mock_print:
            groceries.view()
            mock_print.assert_has_calls(calls)

        groceries.add('Scallions')
        calls.append(call('Scallions'))

        with patch('builtins.print') as mock_print:
            groceries.view()
            mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
