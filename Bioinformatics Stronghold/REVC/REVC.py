## Problema: Uma string de DNA s com um comprimento de até 1000 nucleotídeos
## Resultado: O reverso complementar da string s

# Importar a biblioteca
import pyperclip

# Informar o arquivo usado
arquivo = 'rosalind_revc.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    dna = doc.read()

# Criar um dicionário com o complemento das bases
dic_complemento = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'
}

# Armazenar a sequência complementar
complementar = ''

for nt in dna:
    complementar += dic_complemento[nt]

# Criar a sequência reversa do "complementar"
reverso_complementar = complementar[::-1]

# Como a resposta gerada é grande, copiá-la é a melhor opção
pyperclip.copy(reverso_complementar)
