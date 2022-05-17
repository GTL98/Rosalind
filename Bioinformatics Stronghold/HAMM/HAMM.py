## Problema: Duas strings de DNA s & t de tamanho igual (não excedendo 1 kb)
## Resultado: A distância de Hamming dh(s, t)

# Informar o arquivo usado
arquivo = 'rosalind_hamm.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    s = conteudo[0]
    t = conteudo[1]

# Declarar a variável que armazenará a resposta
distancia_hamming = 0

# Calcular a distância de Hamming
for nt_1, nt_2 in zip(s, t):
    # Calcular a distância de Hamming
    if nt_1 != nt_2:
        distancia_hamming += 1

# Mostrar a resposta
print(distancia_hamming)
