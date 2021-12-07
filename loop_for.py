"""
Loop -> Estrutura de repetição
For -> Uma estrutura

C ou Java
for (int i = 0; i < limitador; i++){
    // execução do loop
}

Python
for item in iteravel
    // execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteraveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- range
    numeros = range(1, 10)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

"""
# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)


# Enumerate:
# (0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')
# Uma tupla é uma lista com um índice e um valor
for i, v, in enumerate(nome): # Pega cada letra e cria uma tupla
    print(nome[i])


for indice, letra in enumerate(nome):
    print(letra)

# O underline serve quando temos 2 valores e não precisamos de um deles, descartamos utilizando _
# No exemplo abaixo, foi descartado o índice e retornando a letra
for _, letra in enumerate(nome):
    print(letra)


for valor in enumerate(nome):
    print(valor)


qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for incremento in range(1, qtd+1):
    num = int(input(f"Informe o valor {incremento}/{qtd}:"))
    soma = soma + num
print(f"A soma é {soma}")


for letra in nome:
    print(letra, end='')
"""
# Original: U+1F60D
# Modificado: U0001F60D

for x in range(3):
    for num in range(1, 11):
        print("\U0001F60D" * num)
