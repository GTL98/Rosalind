# --- Dado: Limite da qualidade q e entradas FASTQ --- #
# --- Problema: Número de posições onde a média da qualidade é menor que o limite q --- #

# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter o limite da qualidade --- #
    q = int(conteudo[0])

    # --- Obter as entradas FASTQ --- #
    entradas = conteudo[1:]

# --- Criar o arquivo com as entradas FASTQ --- #
arquivo_fastq = 'temp_fastq.txt'
with open(arquivo_fastq, 'w') as txt:
    for entrada in entradas:
        txt.write(entrada)

# --- Ler as entradas FASTQ --- #
fastq = SeqIO.parse(arquivo_fastq, 'fastq')

# --- Especificar a quantidade de posições --- #
posicoes = 0

# --- Criar uma lista com os valores da leitura --- #
phred = [leitura.letter_annotations['phred_quality'] for leitura in fastq]

# --- Verificar se a soma de cada posição é menor do que o limite q --- #
for i in range(len(phred[0])):
    if sum(leitura[i] for leitura in phred) / len(phred) < q:
        posicoes += 1

# --- Deletar o arquivo temporário --- #
os.remove(arquivo_fastq)

# --- Mostrar a resposta --- #
print(posicoes)
