## Problema: Um inteiro k seguido por uma lista_pedacos de kmers
## Resultado: A composição dos kmers na string de DNA original

# Importar a biblioteca
import pyperclip

# Informar o arquivo usado
arquivo = 'rosalind_ba3h.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    k = int(conteudo[0])
    kmers = conteudo[1:]

# Criar uma lista_pedacos para armazenar a ordem inical dos kmers
lista_pos_inicio = []

# Criar uma lista_pedacos para armazenar a ordem final dos kmers
lista_pos_final = []

# Criar uma lista_pedacos de tuplas com os grafos
lista_pos_inicio_final = []

# Iterar sobre a lista_pedacos "kmers"
for b, i in enumerate(kmers):
    for n, j in enumerate(kmers):
        kmer_inicio = i[:k-1]
        kmer_final = j[-(k-1):]
        if kmer_final == kmer_inicio:
            # Adicionar à lista_pedacos a posição da sequência em que o kmer termina
            lista_pos_final.append(n)
            # Adicionar à lista_pedacos a posição da sequência em que o kmer começa
            lista_pos_inicio.append(b)
            # Adicionar à lista_pedacos as tuplas com os grafos (kmer que começa e o kmer que termina)
            lista_pos_inicio_final.append((n, b))

# Criar uma lista_pedacos com a ordem dos kmers
lista_ordem = []

# Iterar sobre a lista_pedacos "lista_pos_final"
for pos_final in lista_pos_final:
    # Essa condição é necessária para colocar na primeira posição da "lista_ordem"
    # a posição do kmer que inicia a sequência de DNA final
    if pos_final not in lista_pos_inicio:
        lista_ordem.insert(0, pos_final)

# Iterar sobre a lista_pedacos "lista_ordem"
for pos_ordem in lista_ordem:
    for h in lista_pos_inicio_final:
        # Essa condição serve para ver se o primeiro item do grafo é igual ao item "pos_ordem"
        # Se for igual, adicionar ao final da lista_pedacos o segundo item do grafo
        if h[0] == pos_ordem:
            lista_ordem.append(h[1])

# Criar uma lista_pedacos para armazenar os kmers em ordem
lista_ordem_kmers = [kmers[i] for i in lista_ordem]

# Declarar a variável para armazenar a resposta_peptideo
resposta = lista_ordem_kmers[0][:k-1]

# Iterar sobre a lista_pedacos "lista_ordem_kmers"
for i in range(len(lista_ordem_kmers)):
    # Como o pedaço final de k-1 da sequência anterior  é igual ao pedaço k-1 inicial do item atual,
    # basta pegar somente o último caractere da sequência em questão, já que esse
    # é o único caractere que não existe na sequência anterior
    kmer = lista_ordem_kmers[i][-1]
    # Isso evita de colocar pedaços repetidos em "resposta_peptideo"
    if kmer != resposta:
        resposta += kmer

# Como a resposta_peptideo é muito grande (k+n-1, onde k é o tamanho dos kmers e n a quantidadade de kmers)
# copiar automaticamente a resposta_peptideo é a melhor saída
pyperclip.copy(resposta)
