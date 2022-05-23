## Problema: Um inteiro k e uma string de DNA
## Resultado: Composição de todos os kmers (em qualquer ordem)

# Informar o arquivo usado
arquivo = 'rosalind_ba3a.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    k = int(conteudo[0])
    dna = conteudo[1]

# Criar uma lista_pedacos para armazenar os kmers
lista_kmers = [dna[i:i+k] for i in range(len(dna)) if len(dna[i:i+k]) == k]

# Armazenar a resposta_peptideo em ordem lexicográfica em um arquivo
for kmer in sorted(lista_kmers):
    with open('resposta_ba3a.txt', 'a') as txt:
        txt.write(kmer)
        txt.write('\n')
