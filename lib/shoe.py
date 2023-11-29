#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        self.brand = brand
        self.size = size
        self.condition = "New"

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"
    