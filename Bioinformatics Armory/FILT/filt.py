## Problema: Um limite de qualidade q, a porcentagem de bases p e um conjunto
## de entradas FASTQ.
## Resultado: Número de leituras em entradas FASTQ filtradas.

# Importar a biblioteca
from Bio import SeqIO

# Indicar o arquivo usado
arquivo = 'rosalind_filt.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.readlines()
    numeros = [int(num) for num in conteudo[0].split() if num != '\n']
    fastq = conteudo[1:]

# Criar o arquivo FASTQ
arquivo_fastq = 'arquivo_fastq.txt'
with open(arquivo_fastq, 'w') as txt:
    for linha in fastq:
        txt.write(linha)

# Declarar as variáveis para o limite e porcentagem
limite = numeros[0]
porcentagem = numeros[1]

contador = 0

# Iterar sobre os registros
analisador = SeqIO.parse(arquivo_fastq, 'fastq')
for registro in analisador:
    # Saber a quantidade de leituras estão acima do limite
    lista_leitura_limite = []
    leituras = registro.letter_annotations['phred_quality']
    quantidade_leitura = len(registro.letter_annotations['phred_quality'])
    # Iterar sobre as leituras do arquivo FASTQ
    for leitura in leituras:
        if leitura >= limite:
            lista_leitura_limite.append(leitura)
    # Saber o tamanho de cada lista_pedacos gerada pela iteração
    tamanho_lista_limite = len(lista_leitura_limite)
    # Saber a porcentagem dos valores acima do limite
    porcentagem_limite = int((tamanho_lista_limite / quantidade_leitura) * 100)
    if porcentagem_limite >= porcentagem:
        contador += 1

# Mostrar a resposta_peptideo
print(contador)
