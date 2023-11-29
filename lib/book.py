#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, page_count):
        if not isinstance(page_count, int):
            raise TypeError("page_count must be an integer")

        self.title = title
        self.author = author
        self.page_count = page_count
        self.current_page = 1

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self.current_page += 1





    
        