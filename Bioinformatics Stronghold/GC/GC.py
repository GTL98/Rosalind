## Problema: Até 10 strings de DNA com até 1000 nucleotídeos no formato FASTA
## Resultado: O ID da strings que possui o maior conteúdo GC, seguido pelo valor do conteúdo GC

# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_gc.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    # Criar uma lista_pedacos para armazenar os IDs
    ids = [registro.id for registro in SeqIO.parse(arquivo, 'fasta')]

    # Criar uma lista_pedacos para armazenar as sequências
    sequencias = [registro.seq for registro in SeqIO.parse(arquivo, 'fasta')]

# Criar uma lista_pedacos para armazenar os valores do conteúdo GC
conteudo_gc = []

# Iterar sobre a lista_pedacos "sequencias"
for seq in sequencias:
    tamanho = len(seq)
    g = seq.count('G')
    c = seq.count('C')
    # Cálculo do conteúdo GC
    gc = ((g + c) / tamanho) * 100
    conteudo_gc.append(gc)

# Obter o índice do valor máximo na lista_pedacos "conteudo_gc"
max_gc = max(conteudo_gc)
indice_max_gc = conteudo_gc.index(max_gc)

# Mostrar a resposta
print(ids[indice_max_gc])
print(f'{conteudo_gc[indice_max_gc]:.6f}')
