## Problema: Duas strings de DNA s e t, cada uma com no máximo 1000 nucleotídeos
## Resultado: Todas as posições iniciais de t em s

# Informar o arquivo usado
arquivo = 'rosalind_subs.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    dna = conteudo[0]
    motivo = conteudo[1]

# Declarar o tamanho de "motivo"
k = len(motivo)

# Criar uma lista_pedacos com os pedaços de "dna" com o tamanho de "motivo"
lista_sequencias = [dna[i:i+k] for i in range(len(dna)) if len(dna[i:i+k]) == k]

# Criar uma lista_pedacos para armazenar as posições em que a sequência é igual ao motivo
# Nesse caso, a contagem começa em 1
lista_posicoes = [posicao for posicao, sequencia in enumerate(lista_sequencias, start=1)
                  if sequencia == motivo]

# Mostrar a resposta
for resposta in lista_posicoes:
    print(resposta, end=' ')
