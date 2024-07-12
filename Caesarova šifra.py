alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
"""
def encode(message, shift_number):
    shifted_text = ""
    for one_letter in message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index + shift_number
            shifted_text += alphabet[new_index]
        else:
            shifted_text += alphabet[new_index]
    print(f"Vaše zakódovaná zpráva je: {shifted_text}")

def decode(encrypted_message, shift_number):
    normal_text = ""
    for one_letter in encrypted_message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index - shift_number
            normal_text += alphabet[new_index]
        else:
            normal_text += one_letter
    print(f"Vaše dekódovaná zpráva je: {normal_text}")
"""

def sifra(text, posun, funkce):
    vysledny_text = ""
    for one_letter in text:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            if funkce == "encode":
                new_index = index + posun
                vysledny_text += alphabet[new_index]
            elif funkce == "decode":
                new_index = index - posun
                vysledny_text += alphabet[new_index]
        else:
            vysledny_text += one_letter
    print(f"Zadali jste {funkce}, a výsledek je {vysledny_text}")
        
pokračovat = "ano"

while pokračovat == "ano":
    funkce = input("Napište 'encode', pokud chcete zakódovat, Napište 'decode', pokud chcete odkódovat.\n")
    text = input("Napište svou zprávu:\n").lower()
    posun = int(input("Napište o kolik chcete zprávu posunout:\n"))
    sifra(text, posun, funkce)
    pokračovat = input("Napište 'ano' pokud chcete pokračovat, napište 'ne' pokud chcete šifrovací program ukončit.\n")
"""
    if vstup == "encode":
        encode(text, posun)
        pokračovat = input("Napište 'ano' pokud chcete pokračovat, napište 'ne' pokud chcete šifrovací program ukončit.\n")
    elif vstup == "decode":
        decode(text, posun)
        pokračovat = input("Napište 'ano' pokud chcete pokračovat, napište 'ne' pokud chcete šifrovací program ukončit.\n")
    else:
        print("Zadali jste neznámou funkci")
        pokračovat = input("Napište 'ano' pokud chcete pokračovat, napište 'ne' pokud chcete šifrovací program ukončit.\n")
"""
print("Šifrovací program ukončen. Děkujeme za jeho použití.")
