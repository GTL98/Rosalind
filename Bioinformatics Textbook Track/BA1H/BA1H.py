## Problema: Uma string de DNA, um genoma e um inteiro d
## Resultado: Todas as posições iniciais em que a strings de DNA aparece no genoma com no máximo
## d incompatibilidades

# Informar o arquivo usado
arquivo = 'rosalind_ba1h.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    sequencia = conteudo[0]
    genoma = conteudo[1]
    d = int(conteudo[2])

# Definir o tamanho de "sequencia"
tamanho_sequencia = len(sequencia)

# Criar uma lista_pedacos para armazenar os pedaços com o tamanho informado em "tamanho_sequencia"
lista_pedacos = [(genoma[i:tamanho_sequencia + i], sequencia) for i in range(len(genoma))
                 if len(genoma[i:tamanho_sequencia+i]) == tamanho_sequencia]

# Criar uma lista_pedacos para armazenar os valores da distância Hamming
lista_dh = []

# Analisar cada item em "lista_pedacos"
for pedaco in zip(lista_pedacos):
    # Declarar a variável que armazenará o valor da distância Hamming
    # sempre que um novo "pedaco" for analisado
    distancia_hamming = 0
    # Analisar cada nucleotídeo do em "pedaco"
    for nt_1, nt_2 in zip(pedaco[0][0], pedaco[0][1]):
        # Se os nucleotídeos forem diferentes, calcular a distância Hamming
        if nt_1 != nt_2:
            distancia_hamming += 1
    lista_dh.append(distancia_hamming)

# Saber a posição de cada valor da distância Hamming, pois ela indica
# a posição do nucleotídeo inicial que satisfaz a condição do problema
for posicao, valor in enumerate(lista_dh):
    if valor <= d:
        # Mostar a resposta_peptideo
        print(posicao, end=' ')
