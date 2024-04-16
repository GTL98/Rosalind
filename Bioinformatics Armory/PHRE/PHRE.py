# --- Dado: O limite da qualidade e as entradas FASTQ --- #
# --- Problema: O número de leituras que possuem a média da qualidade menor que o limite --- #

# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO
from statistics import mean


# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter o limite da qualidade --- #
    limite = int(conteudo[0])

    # --- Obter as entradas FASTQ --- #
    entradas = conteudo[1:]


# --- Criar um arquivo temporário para armazenar as entradas FASTQ --- #
with open('fastq_temp.txt', 'w') as temp:
    for entrada in entradas:
        temp.write(entrada)

# --- Contador --- #
contador = 0

# --- Ler as entradas FASTQ --- #
for registro in SeqIO.parse('fastq_temp.txt', 'fastq'):
    # --- Obter a qualidade de cada nucleotídeo lido --- #
    qualidade = registro.letter_annotations['phred_quality']

    # --- Calcular a média da leitura --- #
    media = mean(qualidade)
    
    # --- Verificar se a média da leitura é menor que o limite do problema --- #
    if media < limite:
        contador += 1

# --- Excluir o arquivo temporário --- #
os.remove('fastq_temp.txt')

# --- Mostrar a resposta --- #
print(contador)
