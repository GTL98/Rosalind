# --- Dado: Uma coleção de até 10 entradas FASTA com sequência de DNA de até mil nucleotídeos --- #
# --- Problema: A sequência consenso e a matriz do consenso --- #

# --- Importar as bibliotecas --- #
from Bio import SeqIO
from statistics import mode

# --- Informar o arquivo --- #
arquivo = ''

# --- Obter as sequências de DNA --- #
len_seqs = 0
sequencias = []
for registro in SeqIO.parse(arquivo, 'fasta'):
    len_seqs = len(registro.seq)
    sequencias.append(registro.seq)

# --- Colocar em um dicionário as posições como chaves e os valores como lista --- #
dic_nt = {}
for i in range(len_seqs):
    dic_nt[i] = list()

# --- Obter os nucleotídeos de cada posição --- #
for sequencia in sequencias:
    for i in range(len_seqs):
        dic_nt[i].append(sequencia[i])

# --- Variáveis para montar a sequência consenso e a matriz --- #
consenso = ''
adenina_str = 'A:'
citosina_str = 'C:'
guanina_str = 'G:'
timina_str = 'T:'

# --- Iterar sobre cada nucleotídeo de cada posição --- #
for nucleotideos in dic_nt.values():
    # --- Contar a frequência --- #
    adenina = nucleotideos.count('A')
    citosina = nucleotideos.count('C')
    guanina = nucleotideos.count('G')
    timina = nucleotideos.count('T')

    # --- Obter o nucleotídeo que mais aparece na posição analisada --- #
    nucleotideo = mode(nucleotideos)
    consenso += nucleotideo

    # --- Montar a matriz --- #
    adenina_str += f' {adenina}'
    citosina_str += f' {citosina}'
    guanina_str += f' {guanina}'
    timina_str += f' {timina}'

print(''.join(consenso))
print(adenina_str)
print(citosina_str)
print(guanina_str)
print(timina_str)
