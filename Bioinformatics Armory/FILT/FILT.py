# --- Dado: O limite da qualidade q, porcentagem de bases p e as entradas FASTQ --- #
# --- Problema: O número de entradas que possuem as leituras maior que q e que estejam presentes em mais que p porcento da leitura --- #

# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO

# --- Informar o arquivo --- #
arquivo = 't'

# --- Ler o arquivo --- #
with open(arquivo, 'r') as txt:
    # --- Obter o valor de q e p --- #
    conteudo = txt.readlines()

    # --- Valores de q e p --- #
    valores = conteudo[0].split()
    q = int(valores[0])
    p = int(valores[1])

    # --- Obter as entradas FASTQ --- #
    entradas = conteudo[1:]

# --- Criar o arquivo temporário do FASTQ --- #
with open('fastq_temp.txt', 'w') as txt:
    for entrada in entradas:
        txt.write(entrada)

# --- Contador de entradas --- #
contador = 0

# --- Obter as entradas do arquivo FASTQ --- #
for registro in SeqIO.parse('fastq_temp.txt', 'fastq'):
    # --- Contador da porcentagem --- #
    contador_p = 0

    # --- Obter os valores da leitura --- #
    valores_leitura = registro.letter_annotations['phred_quality']

    # --- Verificar se cada valor é maior igual a q --- #
    for valor in valores_leitura:
        if valor >= q:
            contador_p += 1

    # --- Obter a quantidade de leituras --- #
    leituras = len(valores_leitura)

    # --- Verificar a porcentagem de leituras --- #
    if (contador_p / leituras) * 100 >= p:
        contador += 1
# --- Deletar o arquivo temporário FASTQ --- #
os.remove('fastq_temp.txt')

# --- Mostrar resposta --- #
print(contador)
