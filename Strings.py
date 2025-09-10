#Uma string nada mais é que uma lista/array de caracteres.
curso="Curso de Python"

#Se quiser imprimir uma posição determinada desse array por exemplo:
print(curso[0]) #Imprime o primeiro caractere.
print(curso[0:5]) #Imprime um intervalo de caracteres
print(curso[9:15])
print("Tamanho: " + str(len(curso))) #len retorna a quantidade de caracteres em uma string (no tipo int)

curso="Curso de Python "

print(curso)
print(curso.strip()) #strip remove os espaços no inicio e no final da string.
print("Tamanho: " + str(len(curso)))
print("Tamanho: " + str(len(curso.strip())))
print(curso.lower().strip()) #Coloca a string toda em caixa baixa
print(curso.upper().strip()) #Coloca a string toda em caixa alta
print(curso.replace("Python","P").strip()) #Replace("a","b") troca "a" por "b" na string.

a=curso.split(" ") #Split("a") dará um corte sempre que encontrar um "a" na string

print(a[0]) #Irá printar a string até o split numerado no argumento.
print()

#Printando as letras maiúsculas

LetrasGrandes=""
for i in curso:
    if i.isupper():
        LetrasGrandes+=i
print(LetrasGrandes)

#Printando as letras minúsculas

LetrasPequenas=""
for i in curso:
    if i.islower():
        LetrasPequenas+=i
print(LetrasPequenas)