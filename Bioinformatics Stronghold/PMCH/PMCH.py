# --- Dado: Uma string de s de RNA de até 80 nucleotídeos com as mesmas quantidades de A com U e G com C --- #
# --- Problema: O número total de pareamentos perfeitosde s --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO
from math import factorial

# --- Informar o arquivo --- #
arquivo = ''

# --- Obter a quantidade dos pares de nucleotídeos --- #
A_U = 0
G_C = 0
for registro in SeqIO.parse(arquivo, 'fasta'):
    # --- Obter a sequência --- #
    sequencia = registro.seq

    # --- Contagem de A e U --- #
    A = sequencia.count('A')
    A_U = A

    # --- Contagem de G e C --- #
    G = sequencia.count('G')
    G_C = G

# --- Pareamentos --- #
pareamentos = factorial(A_U) * factorial(G_C)

# --- Mostrar a resposta --- #
print(factorial(A_U) * factorial(G_C))
