import random
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']# 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

print("Generátor hesel")
number_of_small_letters = int(input("Zadejte kolik chcete mít ve Svém heslu malých písmen: \n"))
number_of_big_letters = int(input("Zadejte kolik chcete mít ve Svém heslu velkých písmen: \n"))
number_of_numbers = int(input("Zadejte kolik chcete mít ve Svém heslu čísel: \n"))
number_of_special_char = int(input("Zadejte kolik chcete mít ve Svém heslu speciálních znaků: \n"))

password_list = []

for password in range(number_of_small_letters):
  password_list.append(random.choice(small_letters))

for password in range(number_of_big_letters):
  password_list.append(random.choice(big_letters))

for password in range(number_of_numbers):
  password_list.append(random.choice(numbers))

for password in range(number_of_special_char):
  password_list.append(random.choice(special_char))

random.shuffle(password_list)
print(password_list)