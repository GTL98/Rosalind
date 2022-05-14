## Problema: Arquivo FASTQ, valor de corte de qualidade q, pontuação de qualidade Phred33 assumida.
## Resultado: Arquivo FASTQ cortado de ambas as extremidades
## (bases iniciais e finais removidas com qualidade inferior a q).

# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_bfil.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.readlines()
    limite = int(conteudo[0])
    fastq = conteudo[1:]

# Informar o arquivo FASTQ
arquivo_fastq = 'arquivo_fastq.txt'

# Criar o arquivo FASTQ
with open(arquivo_fastq, 'w') as txt:
    for linha in fastq:
        txt.write(linha)

# Analisar e iterar o arquivo FASTQ
for registro in SeqIO.parse(arquivo_fastq, 'fastq'):
    # Criar uma lista_pedacos com os valores da leitura
    phred = registro.letter_annotations['phred_quality']
    # Informaras posições do começo e final da sequência
    comeco, final = 0, len(phred)
    # Passar um loop através da lista_pedacos e ver se o valor de leitura é menor do que o limite.
    # Se não for, aumentar o valor da variável "comeco".
    # Se for, parar o loop e salvar o novo valor da variável "comeco".
    while phred[comeco] < limite:
        comeco += 1
    # Passar um loop através da lista_pedacos e ver se o valor de leitura é menor do que o limite.
    # Se não for, aumentar o valor da variável "final".
    # Se for, parar o loop e salvar o novo valor da variável "final".
    while phred[final-1] < limite:
        final -= 1

    # Escrever a resposta_peptideo em um documento
    with open('resposta.txt', 'a') as x:
        x.write(registro[comeco:final].format('fastq'))
