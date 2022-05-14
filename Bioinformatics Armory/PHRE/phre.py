## Problema: Um limite de qualidade com as entrdas FASTQ com várias leituras.
## Resultado: O número de leituras cuja a média da qualidade seja menor do
## que o limite.

# Importar as bibliotecas
from Bio import SeqIO
from statistics import mean

# Indicar o arquivo usado
arquivo = 'rosalind_phre.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.readlines()
    limite = int(conteudo[0])
    fastq = conteudo[1:]

# Criar um arquivo para a leitura do FASTQ
arquivo_fastq = 'arquivo_fastq.txt'
with open(arquivo_fastq, 'w') as txt:
    for linha in fastq:
        txt.write(linha)

# Definir um contador para saber o número de leituras
leituras = 0

# Analisar e iterar o arquivo FASTQ
analisador = SeqIO.parse(arquivo_fastq, 'fastq')
for registro in analisador:
    if mean(registro.letter_annotations['phred_quality']) < limite:
        leituras += 1

# Mostrar a resposta_peptideo
print(leituras)
