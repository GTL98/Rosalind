## Problema: Uma string de DNA s com o comprimento máximo de 1000 nucleotídeos
## Resultado: Quatro inteiros (separados por espaços) que contam os respectivos nucleotídeos
## A, C, G e T

# Informar o arquivo usado
arquivo = 'rosalind_dna.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    dna = doc.read()

# Contar quantos A existem no DNA
a = dna.count('A')

# Contar quantos C existem no DNA
c = dna.count('C')

# Contar quantos G existem no DNA
g = dna.count('G')

# Contar quantos T existem no DNA
t = dna.count('T')

# Mostrar a resposta
print(f'{a} {c} {g} {t}')
