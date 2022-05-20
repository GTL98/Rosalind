## Problema: Uma string de DNA (genoma)
## Resultado: Todos o(s) inteiros(s) i minimizando o Skew sobre todos os valores de i (de 0 até len(genoma))

# Informar o arquivo usado
arquivo = 'rosalind_ba1f.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    genoma = doc.read()

# Criar uma lista_pedacos para armazenar os valores de Skew
lista_skew = []

# Iterar sobre o "genoma"
for i in range(len(genoma)):
    # Contar quantos "G" possuem no intervalo da posição 0 até a posição i
    g = genoma[0:i].count('G')
    # Contar quantos "G" possuem no intervalo da posição 0 até a posição i
    c = genoma[0:i].count('C')
    # Calcular o Skew (diferença entre "G" e "C", nessa ordem!!!)
    skew = g - c
    lista_skew.append(skew)

# Saber qual é o menor valor de Skew na lista_pedacos
menor_skew = min(lista_skew)

# Sabendo o menor valor de Skew, saber qual é a posição na lista_pedacos desse valor
for posicao, valor_skew in enumerate(lista_skew):
    if valor_skew == menor_skew:
        # Mostrar a resposta_peptideo
        print(posicao, end=' ')
