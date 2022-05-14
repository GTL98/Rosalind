## Problema: Arquivo FASTQ, limite de qualidade q.
## Resultado: Número de posições em que a qualidade de base média fica abaixo do limite determinado.

# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_bphr.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.readlines()
    limite = int(conteudo[0])
    fastq = conteudo[1:]

# Indicar o arquivo FASTQ
arquivo_fastq = 'arquivo_fastq.txt'

# Criar o arquivo FASTQ
with open(arquivo_fastq, 'w') as txt:
    for linha in fastq:
        txt.write(linha)

# Analisar o arquivo FASTQ
analisador = SeqIO.parse(arquivo_fastq, 'fastq')

# Especificar a quantidade de posições
posicoes = 0

# Criar uma lista_pedacos com os valores de leitura
phred = [i.letter_annotations['phred_quality'] for i in analisador]

# Iterar sobre a lista_pedacos
for i in range(len(phred[0])):
    # Somar cada leitura da mesma posição (1ª leitura da 1ª lista_pedacos, 1ª leitura da 2ª lista_pedacos, ...)
    # e dividir pela quantidade de conjunto de leituras (a quantidade de listas em "phred")
    if sum(q[i] for q in phred) / len(phred) < limite:
        posicoes += 1

# Mostrar a resposta_peptideo
print(posicoes)
