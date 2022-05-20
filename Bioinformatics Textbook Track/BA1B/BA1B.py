## Problema: Uma string de DNA e um interiro k.
## Resultado: Todos os k-mers mais frequentes na string de DNA em qualquer ordem.

# Informar o arquivo usado
arquivo = 'rosalind_ba1b.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    sequencia = conteudo[0]
    k = int(conteudo[1])

# Criar uma lista_pedacos para armazenar os pedaços com tamanho k
lista_sequencias = [sequencia[i:k+i] for i in range(len(sequencia)) if len(sequencia[i:k+i]) == k]

# Criar um dicionário com as chaves sendo as sequências de tamanho k
# e os valores, a quantidade de vezes que aparecem na lista_pedacos
dic_sequencias = {i: lista_sequencias.count(i) for i in lista_sequencias}

# Definir uma variável para armazenar o maior número entre os valores do dicionário
maior = 0

# Loop para saber qual é o maior número entre os valores do dicionário
for valor in dic_sequencias.values():
    if valor > maior:
        maior = valor

# Loop para saber qual (ou quais) chave(s) possui(em) o maior número como chave
for chave, valor in dic_sequencias.items():
    if valor == maior:
        print(chave, end=' ')
