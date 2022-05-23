## Problema: Uma sequência de kmers, tal que os últimos k-1 símbolos do kmeri são iguais
## aos k-1 símbolos de kmeri+1, para i de 1 a n-1
## Resultado: Uma string de comprimento k+n-1 com a junção de todos os kmers

# Importar a biblioteca
import pyperclip

# Informar o arquivo usado
arquivo = 'rosalind_ba3b.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    kmers = doc.read().split('\n')

# Informar o valor de k (tamanho de cada kmer)
k = len(kmers[0])

# Declarar a variável de onde será armazenada a resposta_peptideo
# Começar com o primeiro item da lista_pedacos "kmer", uma vez que ele é que começa a sequência
resposta = kmers[0][:k-1]

# Iterar sobre a lista_pedacos "kmers"
for i in range(len(kmers)):
    # Como o pedaço final de k-1 da sequência anterior  é igual ao pedaço k-1 inicial do item atual,
    # basta pegar somente o último caractere da sequência em questão, já que esse
    # é o único caractere que não existe na sequência anterior
    kmer = kmers[i][-1]
    # Isso evita de colocar pedaços repetidos em "resposta_peptideo"
    if kmer != resposta:
        resposta += kmer

# Como a resposta_peptideo é muito grande (k+n-1, onde k é o tamanho dos kmers e n a quantidadade de kmers)
# copiar automaticamente a resposta_peptideo é a melhor saída
pyperclip.copy(resposta)
