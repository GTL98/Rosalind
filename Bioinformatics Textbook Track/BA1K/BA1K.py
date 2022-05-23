## Problema: Uma string de DNA e um inteiro k
## Resultado: A matriz de frequência de k-mers na string de DNA

# Importar as bibliotecas
import pyperclip
from itertools import product

# Informar o arquivo usado
arquivo = 'rosalind_ba1k.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    genoma = conteudo[0]
    k = int(conteudo[1])

# Criar uma lista_pedacos com os pedaços do "genoma" com tamanho k
lista_kmers = [genoma[i:i+k] for i in range(len(genoma)) if len(genoma[i:i+k]) == k]

# Criar uma lista_pedacos com as combinações de tamanho k das quatro pares de base do DNA
bases = 'ACGT'

# Declarar a função responsável pela criação das combinações com tamanho k
combinacoes = product(bases, repeat=k)

# Criar um dicionário para armazenar a matriz de frequência
dic_matriz = {}

# Iterar sobre a variável "combinacoes"
# Transformar em lista_pedacos para que seja possível iterar, sem isso é retornado um objeto "itertools"
for combinacao_lista in list(combinacoes):
    contador = 0
    # Como os itens são retornados como uma tupla, transformar em string para poder
    # tratar as saídas
    str_combinacao = str(combinacao_lista)
    combinacao = str_combinacao.replace("'", '').replace('(', '')\
        .replace(')', '').replace(',', '').replace(' ', '')
    # Iterar sobre "lista_kmers"
    for kmer in lista_kmers:
        # Se o valor de "combinacao" for igual ao "kmer" então some 1
        if combinacao == kmer:
            contador += 1
    # Colocar no dicionário a "combinacao" (chave) e "contador" (valor)
    dic_matriz[combinacao] = contador

# Declarar a variável de onde será armazenada a resposta_peptideo
resposta = ''

# Obter cada valor do dicionário
for valor in dic_matriz.values():
    # Salvar a resposta_peptideo
    resposta += f'{valor} '

# Copiar a resposta_peptideo, uma vez que a matriz é muito grande e consome memória mostrar toda ela
pyperclip.copy(resposta)
