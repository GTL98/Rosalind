# --- Dado: Até 15 IDs de acesso do UniProt --- #
# --- Problema: A identificação e as posições do motivo de N-gligosilação --- #

# --- Importar as bibliotecas --- #
import os
import re
from Bio import SeqIO
from urllib.request import urlopen

# --- Informar o arquivo --- #
arquivo = ''

# --- Abrir o arquivo --- #
ids = []
with open(arquivo, 'r') as txt:
    # --- Obter os IDs --- #
    linhas = txt.readlines()
    for linha in linhas:
        if '\n' in linha:
            linha = linha[:-1].strip()
        ids.append(linha)

# --- Acessar a informação na internet de cada arquivo FASTA --- #
for id_fasta in ids:
    # --- Tratar o ID --- #
    if '_' in id_fasta:
        id_fasta = id_fasta.split('_')[0].strip()

    # --- Montar a URL --- #
    url = f'http://www.uniprot.org/uniprot/{id_fasta}.fasta'

    # --- Abrir a URL --- #
    dados = urlopen(url)

    # --- Armazenar a informação FASTA --- #
    fasta = dados.read().decode('utf-8', 'ignore')

    # --- Armazenar em um arquivo as informações FASTA --- #
    with open('fasta_temp.fasta', 'a') as txt:
        txt.write(fasta)

# --- Criar a string do motivo --- #
motivos = re.compile(r'(?=(N[^P][ST][^P]))')

# -- Contador --- #
contador = 0

# --- Trabalhar sobre as sequências --- #
for registro in SeqIO.parse('fasta_temp.fasta', 'fasta'):
    # --- Obter as sequências --- #
    sequencia = str(registro.seq)

    # --- Lista com as posições do motivo --- #
    posicoes = []

    # --- Encontrar onde estão os motivos --- #
    for motivo in re.finditer(motivos, sequencia):
        posicoes.append(motivo.start() + 1)
    if len(posicoes) > 0:
        print(ids[contador])
        print(' '.join(map(str, posicoes)))
    contador += 1

# --- Deletar o arquivo temporário --- #
os.remove('fasta_temp.fasta')
