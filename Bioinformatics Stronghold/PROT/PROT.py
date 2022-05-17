## Problema: Uma string de RNA s correspondente a uma fita de mRNA, com no máximo 10 kb
## Resultado: A proteína codificada pela string s

# Importar a biblioteca
import pyperclip

# Informar o arquivo usado
arquivo = 'rosalind_prot.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    rna = doc.read().strip()

# Criar um dicionário dos códons
# O caractere "*" indica os códons de parada
codons = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S',
    'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'UAA': '*', 'UAC': 'Y', 'UAG': '*', 'UAU': 'Y',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
    'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
}

# Criar uma lista_pedacos com os códons em "rna"
# Deve-se multiplicar por 3 para que seja feita a leitura da string do RNA de 3 em 3
lista_codons = [rna[i*3:i*3+3] for i in range(len(rna)) if len(rna[i*3:i*3+3]) == 3]

# Declarar a variável que armazenará a resposta
proteina = ''

# Iterar sobre a lista_pedacos "lista_codons"
for codon in lista_codons:
    if codons[codon] != '*':
        proteina += codons[codon]

# Como a resposta é muito grande, copiá-la é a melhor opção
pyperclip.copy(proteina)
