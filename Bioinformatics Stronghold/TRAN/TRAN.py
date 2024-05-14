# --- Dado: Duas strings de DNA com até mil nucleotídeos --- #
# --- Problema: A razão de transisão e transversão --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO

# --- Informar o arquivo --- #
arquivo = ''

# --- Obter as sequências --- #
sequencias = []
for registro in SeqIO.parse(arquivo, 'fasta'):
    # --- Adicionar a sequência à lista --- #
    sequencias.append(registro.seq)

# --- Comparar as sequências --- #
transicao = 0
transversao = 0
dna_1 = sequencias[0]
dna_2 = sequencias[1]
for nt_1, nt_2 in zip(dna_1, dna_2):
    # --- Calcular a transição --- #
    if nt_1 == 'A' and nt_2 == 'G':
        transicao += 1
    if nt_1 == 'G' and nt_2 == 'A':
        transicao += 1
    if nt_1 == 'C' and nt_2 == 'T':
        transicao += 1
    if nt_1 == 'T' and nt_2 == 'C':
        transicao += 1

    # --- Calcular a transversão --- #
    if nt_1 == 'A' and nt_2 == 'C':
        transversao += 1
    if nt_1 == 'A' and nt_2 == 'T':
        transversao += 1
    if nt_1 == 'G' and nt_2 == 'T':
        transversao += 1
    if nt_1 == 'G' and nt_2 == 'C':
        transversao += 1
    if nt_1 == 'C' and nt_2 == 'A':
        transversao += 1
    if nt_1 == 'C' and nt_2 == 'G':
        transversao += 1
    if nt_1 == 'T' and nt_2 == 'A':
        transversao += 1
    if nt_1 == 'T' and nt_2 == 'G':
        transversao += 1

# --- Calcular a razão --- #
razao = transicao / transversao

# --- Mostrar a resposta --- #
print(round(razao, 11))
