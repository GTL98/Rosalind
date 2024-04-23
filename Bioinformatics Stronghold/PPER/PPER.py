# --- Dado: Dois números inteiros positivos (n, k) --- #
# --- Problema: O módulo de um milhão do número total de permutações de P(n ,k) --- #

# --- Importar a biblioteca --- #
from math import factorial

# --- Informar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo --- #
    conteudo = txt.read()

    # --- Obter os números --- #
    n = int(conteudo.split()[0])
    k = int(conteudo.split()[1])

# --- Calcular a quantidade de permutações possíveis --- #
p = factorial(n) / (factorial(n - k))

# --- Mostrar a resposta --- #
print(int(p % 1_000_000))
