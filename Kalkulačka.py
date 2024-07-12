print("Kalkulačka připravena")
pokračovat = "ano"
while (pokračovat == "ano"):
  Hodnota_1 = float(input("Zadejte první hodonotu: "))
  Hodnota_2 = float(input("Zadejte druhou hodnotu: "))
  Hodnota_3 = input("Zvolte aritmetickou operaci: +, -, *, /, **, %, // ")
# Sčítání
  if Hodnota_3 == "+":
    print(Hodnota_1 + Hodnota_2)
# Odčítání
  elif Hodnota_3 == "-":
    print(Hodnota_1 - Hodnota_2)
# Násobení
  elif Hodnota_3 == "*":
    print(Hodnota_1 * Hodnota_2)
# Dělení
  elif Hodnota_3 == "/":
    print((Hodnota_1) / (Hodnota_2))
# Mocnina
  elif Hodnota_3 == "**":
    print(Hodnota_1 ** Hodnota_2)
# Zbytek po dělení
  elif Hodnota_3 == "%":
    print((Hodnota_1) % (Hodnota_2))
# Celočíselné dělení
  elif Hodnota_3 == "//":
    print(Hodnota_1 // Hodnota_2)
# Špatně zvolená aritmetická operace
  else:
    print("Špatně zvolená aritmetická operace")
  print("Chcete zadat nový příklad? ano/ne")
  pokračovat = input()
else:
  print("Děkujeme za využití kalkulačky")
