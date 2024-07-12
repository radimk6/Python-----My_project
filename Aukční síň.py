
import os

nabizejici = {}

print("Vítejte v programu na tichou aukci.")
pokracovat = "ano"

while pokracovat == "ano":
  jmeno = input("Jaké je Vaše jméno? ")
  castka = int(input("Jaká je Vaše nabídka? "))
  nabizejici[jmeno] = castka
  pokracovat = input("Jsou další nabízející? Napište 'ano' nebo 'ne'. ")
  if pokracovat == "ne":
    os.system("cls") #Vyčistí konzoly

#print(nabizejici)
def nejvyssi_prihoz(seznam_nabizejicich):
  nejvetsi_prihoz = 0
  vitez = ""
  for key in seznam_nabizejicich:
    if seznam_nabizejicich[key] > nejvetsi_prihoz:
      nejvetsi_prihoz = seznam_nabizejicich[key]
      vitez = key
  print(f"Vítězem tiché aukce je: {vitez} s nabídkou {nejvetsi_prihoz}.")

nejvyssi_prihoz(nabizejici)