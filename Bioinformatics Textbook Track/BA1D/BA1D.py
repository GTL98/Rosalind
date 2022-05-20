## Problema: Strings de DNA, uma query e outra do genoma
## Resultado: Todas as posições no genoma onde a sequência query aparece como substring.
## Use a contagem a partir do 0.

# Informar o arquivo usado
arquivo = 'rosalind_ba1d.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    query = conteudo[0]
    genoma = conteudo[1]

# Definir o tamanho da sequência query
tamanho_query = len(query)

# Criar uma lista_pedacos para adicionar os pedaços do genoma com o tamanho da query
lista_pedacos = [(genoma[i:tamanho_query+i], posicao) for posicao, i in enumerate(range(len(genoma)))
                 if len(genoma[i:tamanho_query+i]) == tamanho_query]

# Loop para iterar sobre as tuplas da "lista_pedacos"
for tupla in lista_pedacos:
    # O item 0 da tupla é a sequência de tamanho igual ao "tamanho_query"
    if tupla[0] == query:
        # O item 1 da tupla é a posição da primeira base no genoma
        print(tupla[1], end=' ')
