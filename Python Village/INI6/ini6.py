## Problema: Uma string s de até 10000 letras.
## Resultado: O número de ocorrências de cada palavra na string s, onde as
## palavras são separadas por espaços. As palavras se diferenciam em maiúsculas
## e minúsculas. A saída das palavras pode estar em qualquer ordem.

# Indicar o arquivo usado
arquivo = 'rosalind_ini6.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Separar as palavras onde houver espaço
    frase = doc.read().split()

# Criar um dicionário
dic_palavras = {}

# Loop para iterar sobre a frase
for palavra in frase:
    # Para cada palavra, contar quantas vezes ele aparece na frase
    dic_palavras[palavra] = frase.count(palavra)

# Loop para iterar sobre o dicionário
for chave, valor in dic_palavras.items():
    # Mostrar a cada chave e o seu respectivo valor
    print(chave, valor)
