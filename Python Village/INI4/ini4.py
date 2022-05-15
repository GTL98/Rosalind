## Problema: Dois números inteiros positivos a & b (a < b < 1000).
## Resultado: A soma de todos os inteiros ímpares no intervalo de
## a até b, inclusive.

# Indicar o arquivo usado
arquivo = 'rosalind_ini4.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    numeros = doc.read().split()
    # Criar uma lista_pedacos com os números
    lista_numeros = [int(num) for num in numeros]

# Separar os dois números
num_1 = lista_numeros[0]
num_2 = lista_numeros[1]

# Armazenar a soma dos valores ímpares
soma = 0

# Loop iterar sobre o intervalo
for i in range(num_1, num_2+1):
    # Se o resultado da divisão for 1, então é impar
    if i % 2 == 1:
        soma += i

# Mostrar o resultado da soma
print(soma)
