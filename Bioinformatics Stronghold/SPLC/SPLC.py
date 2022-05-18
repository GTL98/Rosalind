## Problema: Uma string de DNA s (de no máximo 1kb) e uma coleção de substrings atuando como introns.
## Todas as strings estão no formato FASTA
## Resultado: A string da proteína resultante da tradução dos exons

# Importar as bibliotecas
import pyperclip
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_splc.txt'

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

# Criar uma lista_pedacos para armazenar as sequências
lista_sequencias = [str(registro.seq) for registro in SeqIO.parse(arquivo, 'fasta')]

# Indicar a string 's'
s = lista_sequencias[0]

# Indicar os introns
introns = lista_sequencias[1:]

# Criar um dicionário para saber as posições de onde começa e termina os intros
dic_introns = {s.find(introns[i]): s.find(introns[i]) + len(introns[i]) for i in range(len(introns))}

# Deixar em minúsculo os intros em 's'
for comeco, final in dic_introns.items():
    intron = s[comeco: final]
    s = s.replace(intron, intron.lower())

# Se a letra for maíscula, é exon; caso contrário, intron
exons = ''
for nt in s:
    if nt.isupper():
        exons += nt

# Criar uma lista_pedacos com os códons de 'exons'
lista_codons = [exons[i*3:i*3+3] for i in range(len(exons)) if len(exons[i*3:i*3+3]) == 3]

# Declarar a variável que armazenará a resposta
proteina = ''

# Iterar sobre 'lista_codons'
for codon in lista_codons:
    if codons[codon] != '*':
        proteina += codons[codon]

# Como a reposta é grande, copiá-la é a melhor opção
pyperclip.copy(proteina)
