## Problema: Um arquivo que contém no máximo 1000 linhas.
## Resultado: Um arquivo que contenha todas as linhas pares do arquivo original.
## Assuma a numeração baseada em 1.

# Indicar o arquivo usado
arquivo = 'rosalind_ini5.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Separar as linha onde há uma nova linha ('\n')
    texto = doc.read().split('\n')

# Loop para iterar sobre o texto
# Usar "start=1" para que a numeração seja baseada em 1
for linha, frase in enumerate(texto, start=1):
    # Se a posição da linha for par, então mostre a frase dessa linha
    if linha % 2 == 0:
        print(frase)
