
import os

def sum(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("Zadejte první číslo: "))

    lets_continue = "ano"

    while lets_continue == "ano":
        for symbol in operations:
            print(symbol)

        user_symbol = input("Zvolte jednu z operací výše: ")

        num2 = float(input("Jaké je další číslo: "))

        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)

        print(f"{num1} {user_symbol} {num2} = {result}")
        lets_continue = input("Napište ano, pokud chcete pokračovat. Napište ne, pokud chcete kalkulátor zpustit znovu. ")
        if lets_continue == "ano":
            num1 = result
        elif lets_continue == "ne":
            os.system("cls")
            calculator()
                
calculator()