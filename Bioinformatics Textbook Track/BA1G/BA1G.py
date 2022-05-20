## Problema: Duas strings de DNA
## Resultado: Um valor inteiro que represente a distância Hamming

# Informar o arquivo usado
arquivo = 'rosalind_ba1g.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    sequencia_1 = conteudo[0]
    sequencia_2 = conteudo[1]

# Verificar se o tamanho das duas sequências são iguais
assert len(sequencia_1) == len(sequencia_2)

# Declarar a variável que salvará o valor da distância Hamming
distancia_hamming = 0

# Fazer uma tupla com os nucleotídeos na mesma posição das duas sequências
for nt_1, nt_2 in zip(sequencia_1, sequencia_2):
    if nt_1 != nt_2:
        distancia_hamming += 1

# Mostrar a resposta_peptideo
print(distancia_hamming)
