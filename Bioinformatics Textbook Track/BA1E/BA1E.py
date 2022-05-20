## Problema: Uma string de um genoma e os inteiros k, l e t
## Resultado: Todas as substrings de tamanho k presentes no pedaço do genoma de tamanho l que se
## repetem t vezes.

# Informar o arquivo usado
arquivo = 'rosalind_ba1e.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    genoma = conteudo[0]
    inteiros = [int(num) for num in conteudo[1].split(' ')]
    k = inteiros[0]
    l = inteiros[1]
    t = inteiros[2]

# Criar uma lista_pedacos para armazenar as substrings
lista_pedacos = []

for i in range(len(genoma)-l+1):
    for j in range(i, i+l-k):
        # Verificar se o pedaço [l:j+k] está presente em [i:i+l]
        # e se estiver, verificar se esse pedaço repete-se t vezes em [i:i+l]
        if genoma[i:i+l].count(genoma[j:j+k]) == t:
            lista_pedacos.append(genoma[j:j+k])

# Criar uma lista_pedacos para colocar os pedaços, mas somente um de cada se tiver mais do mesmo
lista = []

# Adicionar somente uma entrada de cada item em "lista_pedacos"
for r in lista_pedacos:
    if r not in lista:
        lista.append(r)

# Mostrar a resposta_peptideo
print(' '.join(lista))
