## Problema: Uma string s de no máximo 200 caracteres e quatro números inteiros
## a, b, c & d
## Resultado: O fatiamento da string s dos índices a-->b & c-->d, incluindo os
## espaços. Em outras palavras, deve ser incluso os elementos s[b] e s[d] no
## fatiamento.

# Indicar o arquivo usado
arquivo = 'rosalind_ini3.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Separar a frase
    frase = doc.readline()
    # Separar as posicoes
    numeros = doc.readline().split()
    # Criar uma lista_pedacos com as posições
    posicoes = [int(num) for num in numeros]

# Separar as quatro posições
a = posicoes[0]
b = posicoes[1]
c = posicoes[2]
d = posicoes[3]

# Mostrar o fatiamento da frase
print(f'{frase[a:b+1]} {frase[c:d+1]}')
