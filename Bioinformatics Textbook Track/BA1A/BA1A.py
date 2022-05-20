## Problema: Strings de DNA (sequência completa e sequência alvo)
## Resultado: Quantas vezes a sequência alvo aparece na sequência completa

# Informar o arquivo usado
arquivo = 'rosalind_ba1a.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    sequencia_completa = conteudo[0]
    sequencia_alvo = conteudo[1]

# Declarar o tamanho a ser encontrado
tamanho_alvo = len(sequencia_alvo)

# Declarar um contador
contador = 0

# Loop para saber quantas vezes aparece a sequência alvo na sequência completa
for i in range(len(sequencia_completa)):
    if sequencia_completa[i:tamanho_alvo+i] == sequencia_alvo:
        contador += 1

# Mostrar a resposta_peptideo
print(contador)
