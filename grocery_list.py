#!/usr/bin/env python

class GroceryList:

    def __init__(self, file=None):
        self.items = []
        if file:
            with open(file, 'r') as f:
                _ = [self.add(line.rstrip()) for line in f.readlines()]

    def add(self, item):
        self.items.append(item)

    def view(self):
        _ = [print(item) for item in self.items]
