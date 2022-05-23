## Problema: Uma coleção de kmers
## Resultado: Um gráfico de sobreposição dos kmer como uma lista_pedacos de adjacência

# Informar o arquivo usado
arquivo = 'rosalind_ba3c.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    kmers = doc.read().split('\n')

# Informar o valor de k
k = len(kmers[0])

# Criar uma lista_pedacos para armazenar os grafos criados
lista_grafos = []

# Iterar sobre a lista_pedacos "kmers"
for i in kmers:
    for j in kmers:
        kmer_inicio = i[:k-1]
        kmer_final = j[-(k-1):]
        # Essa condição evita de que sejam analisados o começo e final do mesmo kmer
        if i != j:
            # Se os caracteres k-1 finais da sequência anterior forem iguais aos caracteres k-1
            # da sequência atual, então coloque a resposta_peptideo em "lista_grafos"
            if kmer_final == kmer_inicio:
                lista_grafos.append(f'{j} -> {i}')

# Ordenar os grafos de modo lexicográfico
for grafo in sorted(lista_grafos):
    # Como a resposta_peptideo é muito grande, salvá-la em um arquivo é a melhor opção
    with open('resposta_ba3c.txt', 'a') as txt:
        txt.write(grafo)
        txt.write('\n')
