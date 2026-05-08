# Michael Sam C. Apale
# BSCPE 1-4

# Import Tkinter for GUI(para maangas)
import tkinter as Tkinter
from tkinter import messagebox as MessageBox

class Calculator:
    def __init__(self, naruto, luffy):
        self.naruto = naruto
        self.luffy = luffy

    def calculate(self):
        pass

class Addition(Calculator):
    def calculate(self):
        return self.naruto + self.luffy

class Subtraction(Calculator):
    def calculate(self):
        return self.naruto - self.luffy

class Multiplication(Calculator):
    def calculate(self):
        return self.naruto * self.luffy

class Division(Calculator):
    def calculate(self):
        if self.luffy == 0:
            raise ZeroDivisionError
        return self.naruto / self.luffy

# Title, Size and Color ng interface
class CalculatorApp:
    def __init__(self, ichigo):
        self.ichigo = ichigo
        self.ichigo.title("CASIO")
        self.ichigo.geometry("300x400")
        self.ichigo.config(bg="#1e1e2f")

        self.kakashi = Tkinter.StringVar()

        self.tsunade = Tkinter.Label(
            ichigo, text="CASIO", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="#22D3EE")
        self.tsunade.pack(pady=10)
# Creating the option menu :)
        self.zoro = Tkinter.OptionMenu(
            ichigo, self.kakashi,
            "Addition", "Subtraction", "Multiplication", "Division")
        self.zoro.pack(pady=10)

        self.sasuke = Tkinter.Entry(ichigo)
        self.sasuke.pack(pady=10)

        self.sanji = Tkinter.Entry(ichigo)
        self.sanji.pack(pady=10)

        self.ace = Tkinter.Button(
            ichigo, text="Calculate", command=self.calculate_result)
        self.ace.pack(pady=10)

        self.urahara = Tkinter.Label(ichigo, text="Result:")
        self.urahara.pack(pady=10)
# Calculations
    def calculate_result(self):
        try:
            sakura = float(self.sasuke.get())
            nami = float(self.sanji.get())
            shunsui = self.kakashi.get()

            if shunsui == "Addition":
                aizen = Addition(sakura, nami)
            elif shunsui == "Subtraction":
                aizen = Subtraction(sakura, nami)
            elif shunsui == "Multiplication":
                aizen = Multiplication(sakura, nami)
            elif shunsui == "Division":
                aizen = Division(sakura, nami)
            else:
                MessageBox.showerror("Error", "Choose operation")
                return
# Resuuultsss
            whitebeard = aizen.calculate()
            self.urahara.config(text=f"Result: {whitebeard}")
# For syntax error(para sa makukulit na naglalagay ng letters at nagdidivide sa 0)
        except ValueError:
            MessageBox.showerror("Error", "Invalid input")
        except ZeroDivisionError:
            MessageBox.showerror("Error", "Cannot divide by zero")

itachi = Tkinter.Tk()
brook = CalculatorApp(itachi)
itachi.mainloop()