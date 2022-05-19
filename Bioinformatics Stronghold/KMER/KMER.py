## Problema: Uma string de DNA s no formato FASTA, com tamanho máximo de 100 kb
## Resultado: A compsição de 4-mer de s

# Importar as bibliotecas
from Bio import SeqIO
from itertools import product

# Informar o arquivo usado
arquivo = 'rosalind_kmer.txt'

# Armazenar a string 's' em uma variável
s = str(SeqIO.read(arquivo, 'fasta').seq)

# Declarar o tamanho do kmer
k = 4

# Criar uma lista para armazenar os pedaços de 's' com tamanho 'k'
lista_pedacos = [s[i:i+k] for i in range(len(s)) if len(s[i:i+k]) == k]

# Ordenar a lista lexicograficamente
lista_ordenada = sorted(lista_pedacos)

# Criar uma lista com todas as possibilidades de kmers
bases = 'ACGT'
combinacoes = []
possibilidades = list(product(bases, repeat=k))
for p in possibilidades:
    p_str = str(p)
    p_novo = p_str.replace('(', '').replace("'", '').replace(',', '').replace(' ', '').replace(')', '')
    combinacoes.append(p_novo)

# Criar um dicionário para armazenar a quantidade de cada kmer
dic_kmers = {j: lista_ordenada.count(j) for j in combinacoes}

# Como a resposta gerada é grande (4**4 = 256), salvá-la em um arquivo é a melhor opção
with open('resposta_kmer.txt', 'a') as txt:
    for chave in dic_kmers:
        txt.write(f'{str(dic_kmers[chave])} ')
