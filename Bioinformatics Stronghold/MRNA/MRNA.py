## Problema: Uma cadeia de proteína com até 1000 aminoácidos
## Resultado: O número total de sequências de RNA diferentes das quais a proteína pode ter sido
## traduzida, o número total deve ser o módulo de 1.000.000. Não esqueça de considerar os códons
## de parada

# Informar o arquivo usado
arquivo = 'rosalind_mrna.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().strip()
    # Adicionar o códon de parada na sequência proteica
    proteina = conteudo + '*'

# Criar um dicionário com a quantidade de códons que codificam os 20 aminoácidos
aminoacidos = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2,
    'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2,
    'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2, '*': 3
}

# Declarar a variável que armazenará a resposta
combinacoes = 1

# Iterar sobre a "proteina"
for aa in proteina:
    # Multiplicar os valores (quantidade de códons que codificam esse aminoácido)
    # para cada aminoacido presente em "proteina"
    combinacoes *= aminoacidos[aa]

# Mostrar a resposta
print(combinacoes % 10**6)
