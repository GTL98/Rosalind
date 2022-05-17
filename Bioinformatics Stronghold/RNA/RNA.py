## Problema: Uma string de DNA t com comprimento de até 1000 nt
## Resultado: A string de RNA transcrita de t

# Importar a biblioteca
import pyperclip

# Informar o arquivo usado
arquivo = 'rosalind_rna.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    dna = doc.read()

# Declarar a variável de onde será armazenado o RNA
rna = ''

# Realizar a troca de T para U
for nt in dna:
    if nt == 'T':
        rna += 'U'
    else:
        rna += nt

# Como a resposta é grande, copiá-la é a melhor opção
pyperclip.copy(rna)
