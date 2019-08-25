#!/usr/bin/env python

class GroceryList:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def view(self):
        return tuple(self.items)
