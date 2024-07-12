import random
from test import stages
#GENEROVÁNÍ NÁHODNÉHO SLOVA
words = ["harry", "ron", "hermiona", "draco", "snape", "albus"]
random_word = random.choice(words)

#GENEROVÁNÍ PODTRŽÍTEK
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")

#ŽIVOTY
životy = 6
print(stages[životy])

#VYPSÁNÍ SLOVA S PODTRŽÍTKY V NORMÁLNÍ PODOBĚ
printed_word = ""
for one_letter in hidden_word:
  printed_word += one_letter
print(printed_word)

while "_" in hidden_word:
  guess = input("Zadejte hádané písmeno\n").lower()
  for index in range(0, len(random_word)):
    if guess == random_word[index]:
        hidden_word[index] = guess

  #KONTROLA ŽIVOTŮ
  if guess not in hidden_word:
     životy -= 1
     print(stages[životy])
  print(f"Počet Vašich životů je {životy}")

  if životy == 0:
     print("Prohráli jste!!!")
     break
  
  #VYPSÁNÍ SLOVA S PODTRŽÍTKY V NORMÁLNÍ PODOBĚ
  printed_word = ""
  for one_letter in hidden_word:
    printed_word += one_letter
  print(printed_word)

  #KONTROLA VÍTĚZSTVÍ
  if "_" not in hidden_word:
    print("Vyhráli jste!!!")
