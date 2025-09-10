nome = input("Digite seu nome completo: ")
nome = nome.lower()
vog = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"

if nome[0] in vog:
    print("O nome começa com vogal.")
if nome[-1] in cons:
    print("O nome termina com consoante.")
if (nome[0] in cons) and (nome[-1] in vog):
    print("Nome neutro.")