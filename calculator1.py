
import math
import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trigonometric Calculator")

        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=10)

        self.result = tk.StringVar()

        self.sin_button = ttk.Button(self, text="sin", command=lambda: self.calculate("sin"))
        self.sin_button.pack(padx=5, pady=5)

        self.cos_button = ttk.Button(self, text="cos", command=lambda: self.calculate("cos"))
        self.cos_button.pack(padx=5, pady=5)

        self.tg_button = ttk.Button(self, text="tg", command=lambda: self.calculate("tg"))
        self.tg_button.pack(padx=5, pady=5)

        self.ctg_button = ttk.Button(self, text="ctg", command=lambda: self.calculate("ctg"))
        self.ctg_button.pack(padx=5, pady=5)

        self.asin_button = ttk.Button(self, text="asin", command=lambda: self.calculate("asin"))
        self.asin_button.pack(padx=5, pady=5)

        self.acos_button = ttk.Button(self, text="acos", command=lambda: self.calculate("acos"))
        self.acos_button.pack(padx=5, pady=5)

        self.atg_button = ttk.Button(self, text="atg", command=lambda: self.calculate("atg"))
        self.atg_button.pack(padx=5, pady=5)

        self.actg_button = ttk.Button(self, text="actg", command=lambda: self.calculate("actg"))
        self.actg_button.pack(padx=5, pady=5)

        self.result_label = tk.Label(self, textvariable=self.result)
        self.result_label.pack(padx=10, pady=10)

    def calculate(self, operation):
        try:
            number = float(self.entry.get())
            result = None

            if operation == "sin":
                result = math.sin(math.radians(number))
            elif operation == "cos":
                result = math.cos(math.radians(number))
            elif operation == "tg":
                result = math.tan(math.radians(number))
            elif operation == "ctg":
                result = 1 / math.tan(math.radians(number))
            elif operation == "asin":
                result = math.degrees(math.asin(number))
            elif operation == "acos":
                result = math.degrees(math.acos(number))
            elif operation == "atg":
                result = math.degrees(math.atan(number))
            elif operation == "actg":
                result = 1 / math.degrees(math.atan(1 / number))

            self.result.set(round(result, 5))
        except ValueError:
            self.result.set("Invalid input")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()