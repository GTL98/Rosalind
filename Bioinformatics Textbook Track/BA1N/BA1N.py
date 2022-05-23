## Problema: Uma string de DNA e um inteiro d
## Resultado: Todas as combinações de strings que possuem até d compatibilidades

# Importar a biblioteca
from itertools import product

# Informar o arquivo usado
arquivo = 'rosalind_ba1n.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    dna = conteudo[0]
    d = int(conteudo[1])
    tamanho_dna = len(dna)

# Criar uma lista_pedacos para armazenar o valor de "dna" sempre que existir uma combinação feita
lista_dna = []

# Adicionar todas as combinações com o tamanho de "tamanho_dna"
lista_combinacoes = []

# Informar as bases de DNA a serem combinadas
bases = 'ACGT'

# Criar a função de combinação
combinacoes = product(bases, repeat=tamanho_dna)

# Iterar sobre as combinações
# Transformar em lista_pedacos para que seja possível iterar, sem isso é retornado um objeto "itertools"
for c in list(combinacoes):
    # Como os itens são retornados como uma tupla, transformar em string para poder
    # tratar as saídas
    str_c = str(c)
    c_novo = str_c.replace('(', '').replace("'", '').replace(',', '').replace(')', '').replace(' ', '')
    lista_combinacoes.append(c_novo)
    lista_dna.append(dna)

# Fazer um loop para criar uma tupla com os dados pareados de "lista_dna" e "lista_combinacoes"
for tupla in zip(lista_dna, lista_combinacoes):
    # Declarar uma variável para armazenar o valor da distância Hamming
    distancia_hamming = 0
    # Informar a condição para calcular a distância Hamming
    for nt_1, nt_2 in zip(tupla[0], tupla[1]):
        if nt_1 != nt_2:
            distancia_hamming += 1
    # Informar a condição para mostrar a reposta
    if distancia_hamming <= d:
        # Escrever em um arquivo a resposta_peptideo, já que são muitas sequências para
        # mostrar na tela de comando
        with open('resposta_ba1n.txt', 'a') as txt:
            txt.write(tupla[1])
            txt.write('\n')
