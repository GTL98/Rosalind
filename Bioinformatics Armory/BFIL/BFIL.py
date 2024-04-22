# --- Dado: Valor de corte limite q e entradas FASTQ --- #
# --- Problema: Saída em FASTQ com as extremidades removidas, caso tenham o valor de leitura menor do que q --- #

# --- Importar as bibliteca --- #
import os
from Bio import SeqIO

# --- Indicar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o conteúdo do arquivo --- #
    conteudo = txt.readlines()

    # --- Obter o valor limite --- #
    q = int(conteudo[0])

    # --- Obter as entradas FASTQ --- #
    entradas = conteudo[1:]

# --- Criar o arquivo temporário FASTQ --- #
arquivo_fastq = 'temp_fastq.txt'
with open(arquivo_fastq, 'w') as txt:
    for entrada in entradas:
        txt.write(entrada)

# --- Ler o arquivo FASTQ --- #
for registro in SeqIO.parse(arquivo_fastq, 'fastq'):
    # --- Obter o valor de cada leitura --- #
    phred = registro.letter_annotations['phred_quality']

    # --- Informar a posição inicial e final na sequência --- #
    comeco = 0
    final = len(phred)

    # --- Verificar se a posição inicial analizada tem o valor de leitura menor do que q --- #
    while phred[comeco] < q:
        comeco += 1

    # --- Verificar se a posição final analizada tem o valor de leitura menor do que q --- #
    while phred[final-1] < q:
        final -= 1

    # --- Mostrar a resposta de cada iteração --- #
    print(registro[comeco:final].format('fastq'))

# --- Deletar o arquivo temporário FASTQ --- #
os.remove(arquivo_fastq)
