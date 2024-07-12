import random
import os

# MOJE ŘEŠENÍ

print("Vítejte v hádací hře, kde musíte porazit počítač.")
print("Uhodněte číslo od 1 do 100.")
lets_continue = "ano"
while lets_continue == "ano":
  difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")

  lives = 1

  if difficulty == "easy":
    lives = 10
    print(f"Váš počet pokusů je {lives}.")
  elif difficulty == "hard":
    lives = 5
    print(f"Váš počet pokusů je {lives}.")

  random_number = random.randint(1, 100)
  print(random_number)

  while lives != 0:
    user_number = int(input("Tipněte si číslo: "))
    if user_number == random_number:
      print("Výborně vyhráli jste!!!")
    elif user_number < random_number:
      print("Příliš nízký tip.")
      lives -= 1
      if lives != 0:
        print(f"Váš počet zbývajících pokusů k uhádnutí je {lives}.")
      else:
        print("Počitač vyhrál. Prohráli jste!")
        lets_continue = input("Napište 'ano' pokud chcete pokračovat. Napište 'ne' pokud chcete hru ukončit. ")
        os.system("cls")
    elif user_number > random_number:
      print("Příliš vysoký tip.")
      lives -= 1
      if lives != 0:
        print(f"Váš počet zbývajících pokusů k uhádnutí je {lives}.")
      else:
        print("Počitač vyhrál. Prohráli jste!")
        lets_continue = input("Napište 'ano' pokud chcete pokračovat. Napište 'ne' pokud chcete hru ukončit. ")
        os.system("cls")

print("Doufám, že jste si hru užily.")


# #ŘEŠENÍ OD DAVIDA ŠETKA

# print("Vítejte v hádací hře, kde musíte porazit počítač.")
# print("Uhodněte číslo od 1 do 100.")

# def difficulty():
#   difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")
#   if difficulty == "easy":
#     return 10
#   elif difficulty == "hard":
#     return 5

# def guessing_game():
#   random_number = random.randint(1, 100)
#   lets_continue = ""
#   lives = difficulty()

#   while lives > 0:
#     print(f"Váš počet zbývajících pokusů je {lives}")
#     user_number = int(input("Tipněte si číslo: "))

#     if user_number > random_number:
#       print("Příliš vysoké")
#       lives -= 1
#     elif user_number < random_number:
#       print("Příliš nízké")
#       lives -= 1
#     else:
#       print("Vyhráli jste. Počítač prohrál!")
#       lets_continue = input("Napište 'ano' pokud chcete pokračovat. Napište 'ne' pokud chcete hru ukončit. ")

#     if lives == 0:
#       print("Prohráli jste!")
#       lets_continue = input("Napište 'ano' pokud chcete pokračovat. Napište 'ne' pokud chcete hru ukončit. ")

#     if lets_continue == "ano":
#       os.system("cls")
#       guessing_game()
#     elif lets_continue == "ne":
#       os.system("cls")
#       break

# guessing_game()