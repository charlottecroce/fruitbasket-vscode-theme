#!/usr/bin/env python3

import math, os, sys  # standard libraries

# Constants
PI = 3.14159
GREETING = "Hello, World!"

class ThemePreview:
    def __init__(self, name: str):
        self.name = name
        self.colors = {"background": "#000000", "text": "#FFFFFF"}

    def display(self):
        print(f"Previewing theme: {self.name}")
        for key, value in self.colors.items():
            print(f"{key.capitalize()}: {value}")

@staticmethod
def helper(x: int) -> bool:
    return x in range(10) and not x % 2

if __name__ == "__main__":
    tp = ThemePreview("Fruitbasket")
    tp.display()
