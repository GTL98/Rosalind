## Problema: Duas strings de DNA s1 & s2 com tamanho igual (no máximo 1 kb)
## Resultado: A taxa de transição/transversão R(s1, s2)

# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_tran.txt'

# Armazenar em uma lista as sequências de DNA
lista_sequencias = [str(registro.seq) for registro in SeqIO.parse(arquivo, 'fasta')]

# Declarar as sequências de DNA
s_1 = lista_sequencias[0]
s_2 = lista_sequencias[1]

# Transição é quando o nucleotídeo muda para a mesma classe química
transicao = 0

# Transversão é quando o nucleotídeo muda para a classe química diferente
transversao = 0

# Saber a quantidade de transição e transversão
for nt_1, nt_2 in zip(s_1, s_2):
    # Calcular a transição
    if nt_1 == 'A' and nt_2 == 'G':
        transicao += 1
    if nt_1 == 'G' and nt_2 == 'A':
        transicao += 1
    if nt_1 == 'T' and nt_2 == 'C':
        transicao += 1
    if nt_1 == 'C' and nt_2 == 'T':
        transicao += 1
    # Calcular a transversão
    if nt_1 == 'A' and (nt_2 == 'C' or nt_2 == 'T'):
        transversao += 1
    if nt_1 == 'G' and (nt_2 == 'C' or nt_2 == 'T'):
        transversao += 1
    if nt_1 == 'C' and (nt_2 == 'A' or nt_2 == 'G'):
        transversao += 1
    if nt_1 == 'T' and (nt_2 == 'A' or nt_2 == 'G'):
        transversao += 1

# Taxa de transição/transversão
taxa = transicao/transversao

# Mostrar resposta
print(f'{taxa:.11f}')
