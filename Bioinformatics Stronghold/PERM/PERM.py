# --- Dado: Um número positivo inteiro (n <= 7) --- #
# --- Problema: O número total de permutações, seguido de todas as permutações (em qualquer ordem) --- #

# --- Importar a biblioteca --- #
from itertools import permutations

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o número --- #
    n = int(txt.read())

# --- Criar uma lista para armazenar os números de 1 a n --- #
numeros = [i for i in range(1, n+1)]

# --- Criar as permutações --- #
p = list(permutations(numeros, n))

# --- Quantidade de permutações --- #
qtde_p = len(p)

# --- Mostrar a resposta --- #
print(qtde_p)
for item in p:
    # --- Retirar os parênteses e as vírgulas --- #
    resposta = str(item).replace('(', '').replace(')', '').replace(',', ' ')

    # --- Mostrar a resposta --- #
    print(resposta)
