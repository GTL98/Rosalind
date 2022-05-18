## Problema: Um inteiro positivo n <= 7
## Resultado: O número total de permutações de n e todas as permutções possíveis (em qualquer ordem)

# Importar as bibliotecas
from math import factorial
from itertools import permutations

# Informar o arquivo usado
arquivo = 'rosalind_perm.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    num = int(doc.read().strip())

# Saber quantas permutações existem
total_permutacoes = factorial(num)

# Criar uma lista_pedacos para armazenar os número de 1 a 'num'
lista_numeros = [i+1 for i in range(num)]

# Saber quais são as permutações
permutacoes = list(permutations(lista_numeros))

# Criar a uma lista_pedacos para armazenar os valores do tratamento dos itens de 'permutacoes'
lista_permutacoes = []

# Tratar os itens de 'permutacoes'
for p in permutacoes:
    p_str = str(p)
    permutacao = p_str.replace('(', '').replace("'", '').replace(',', '').replace(')', '')
    lista_permutacoes.append(permutacao)

# Como a resposta gerada é grande, a melhor opção é salvá-la em um arquivo
with open('resposta_perm.txt', 'a') as txt:
    txt.write(str(total_permutacoes))
    txt.write('\n')
    for resposta in lista_permutacoes:
        txt.write(resposta)
        txt.write('\n')
