## Problema: Uma string de DNA s com até 1 kb no formato FASTA
## Resultado: Toda proteína candidata que pode ser traduzida como ORF de s. As respostas podem ser
## retornadas em qualquer ordem

# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_orf.txt'

# Criar um dicionário dos códons
# O caractere "*" indica os códons de parada
codons = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S',
    'ATA': 'I', 'ATC': 'I', 'ATG': 'M', 'ATT': 'I',
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'TAA': '*', 'TAC': 'Y', 'TAG': '*', 'TAT': 'Y',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TGA': '*', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C',
    'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'
}

# Armazenar a sequência de DNA
s = ''

# Iterar sobre o arquivo
for registro in SeqIO.parse(arquivo, 'fasta'):
    s += str(registro.seq)

# Criar a lista_pedacos pra armazenar as sequências que começam com 'ATG'
lista_atg = []

# Iterar sobre a string 's'
for n, i in enumerate(range(len(s))):
    # Verificar se o tamanho do códon é igual a 3
    if len(s[i:i+3]) == 3:
        #  Verificar se o pedaço de s analisado é igual a 'ATG'
        if s[i:i+3] == 'ATG':
            lista_atg.append(s[n:])

# Criar uma lista_pedacos para armazenar as ORF
lista_orfs = []

# Iterar sobre a 'lista_atg'
for sequencia in lista_atg:
    # Armazenar os códons de cada item da 'lista_atg'
    lista_codons = list()
    for i in range(len(sequencia)):
        # Verificar se os códons possuem o tamanho de 3 nucleotídeos
        if len(sequencia[i*3:i*3+3]) == 3:
            lista_codons.append(sequencia[i*3:i*3+3])
    # Armazenar a ORF de cada sequência
    proteina = ''
    for codon in lista_codons:
        proteina += codons[codon]
        # Se o códon analisado for de parada, então parar o loop
        if proteina[-1] == '*':
            break
    # Adicionar somente as ORFs que possuem códon de parada
    if proteina[-1] == '*':
        if proteina[:-1] not in lista_orfs:
            lista_orfs.append(proteina[:-1])

# Agora, fazer a mesma coisa só que com a sequência reversa complementar
dic_reverso = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Armazenar a sequência reversa do DNA
s_rev = ''

# Iterar sobre 's'
for nt in s:
    s_rev += dic_reverso[nt]

# Armazenar a sequência reversa complementar de 's'
s_rev_com = s_rev[::-1]

# Criar a lista_pedacos pra armazenar as sequências que começam com 'ATG' do reverso complementar
lista_atg_rev_com = []

# Iterar sobre a string 's_rev_com'
for n, i in enumerate(range(len(s_rev_com))):
    # Verificar se o tamanho do códon é igual a 3
    if len(s_rev_com[i:i+3]) == 3:
        #  Verificar se o pedaço de s analisado é igual a 'ATG'
        if s_rev_com[i:i+3] == 'ATG':
            lista_atg_rev_com.append(s_rev_com[n:])

# Iterar sobre a 'lista_atg_rev_com'
for sequencia in lista_atg_rev_com:
    # Armazenar os códons de cada item da 'lista_atg_rev_com'
    lista_codons = list()
    for i in range(len(sequencia)):
        # Verificar se os códons possuem o tamanho de 3 nucleotídeos
        if len(sequencia[i*3:i*3+3]) == 3:
            lista_codons.append(sequencia[i*3:i*3+3])
    # Armazenar a ORF de cada sequência
    proteina = ''
    for codon in lista_codons:
        proteina += codons[codon]
        # Se o códon analisado for de parada, então parar o loop
        if proteina[-1] == '*':
            break
    # Adicionar somente as ORFs que possuem códon de parada
    if proteina[-1] == '*':
        if proteina[:-1] not in lista_orfs:
            lista_orfs.append(proteina[:-1])

# Como a resposta pode ser grande, a melhor maneira é salvá-la em um arquivo
with open('resposta_orf.txt', 'a') as txt:
    for orf in lista_orfs:
        txt.write(orf)
        txt.write('\n')
