## Problema: Uma coleção de até 10 símbolos definidos em ordem alfabética
## e um inteiro positivo n (n <= 10)
## Resultado: Todas as strings de tamanho n que podem ser formadas com os símbolos em ordem alfabética

# Importar a biblioteca
from itertools import product

# Informar o arquivo usado
arquivo = 'rosalind_lexf.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    letras = [l for l in conteudo[0].split()]
    letras_juntas = ''.join(letras)
    n = int(conteudo[1])

# Criar todas as combinações
combinacoes = list(product(letras_juntas, repeat=n))

# Editar os item de 'combinacoes' para que fique igual a resposta
# Como a resposta gerada é grande, salvá-la em um arquivo é a melhor opção
with open('resposta_lexf.txt', 'a') as txt:
    for c in combinacoes:
        c_str = str(c)
        c_novo = c_str.replace('(', '').replace("'", '').replace(',', '').replace(' ', '').replace(')', '')
        txt.write(f'{c_novo}\n')
