## ESSE AQUI É O ERRADO, MAS VOU SALVAR PORQUE FOI UM BOM APRENIZADO USAR BEM A CABEÇA PARA
## ENTENDER COMO RESOLVER OS PROBLEMAS!!!


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

# Criar uma lista_pedacos para armazenar os pedaços com tamanho k
lista_pedacos = [genoma[i:k+i] for i in range(len(genoma)) if len(genoma[i:k+i]) == k]

# Criar um dicionário com com as chaves sendo as sequências de tamanho k
# e os valores, a quantidade de vezes que aparecem na lista_pedacos
dic_sequencias = {i: lista_pedacos.count(i) for i in lista_pedacos}

# Criar uma lista_pedacos com as sequências que aparecem t vezes
lista_t = [chave for chave, valor in dic_sequencias.items() if valor == t]

# Criar uma lista_pedacos para armazenar as posições das substrings na "lista_pedacos"
lista_posicao = []

# Criar uma lista_pedacos para armazenar as substrings que satisfazem a condição
lista_kmers = []

# Definir um contador para selecionar os itens da "lista_pos"
contador = 0

# Loop para iterar sobre os items de "lista_pedacos"
for posicao, pedaco in enumerate(lista_pedacos):
    # Ver se o "pedaco" é igual a substring na posição do "contador"
    if pedaco == lista_t[contador]:
        # Adicionar todas as posições em que o "pedaco" aparece em "lista_pedacos"
        lista_posicao.append(posicao)
        # Somar mais k para pegar a última base da substring
        if lista_posicao[-1]+k - lista_posicao[0] <= l:
            # Isso evita de colocar a mesma informação duas vezes
            if pedaco in lista_kmers:
                break
            else:
                # Assim coloca somente uma vez a informação
                lista_kmers.append(pedaco)
                # Deleta a "lista_posicao" para colocar as posições da nova substring
                del lista_posicao[:]
                contador += 1
    if contador == len(lista_t):
        break

# Mostrar a resposta_peptideo
resposta = ' '.join(lista_kmers)
print(resposta)
