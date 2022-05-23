## Problema: Uma string de DNA e uma string de peptídeo
## Resultado: Todas as substrings de DNA que codificam o peptídeo

# Importar a biblioteca
from Bio.Seq import Seq

# Informar o arquivo usado
arquivo = 'rosalind_ba4b.txt'

# Abrir o arquivo
with open(arquivo, 'r') as doc:
    conteudo = doc.read().split('\n')
    dna = conteudo[0]
    peptideo = conteudo[1]

# Definir o tamanho da sequência codificadora
tamanho_codons = len(peptideo) * 3

# Criar uma lista_pedacos para armazenar os pedaços de DNA no tamanho informado por "tamanho_codons"
# já transformados em objetos Seq
lista_dna = [Seq(dna[i:i + tamanho_codons]) for i in range(len(dna))
             if len(Seq(dna[i:i + tamanho_codons])) == tamanho_codons]

# Criar uma lista_pedacos para armazenar as sequências que formam o peptídeo
lista_sequencias = []

# Iterar sobre a "lista_dna"
for seq in lista_dna:
    # Condição para saber se a sequência traduzida é igual ao peptídeo informado
    if seq.translate() == peptideo:
        lista_sequencias.append(str(seq))

# Iterar sobre a "lista_dna"
for seq_rev_comp in lista_dna:
    # Condição para saber se a sequência reversa complementar traduzida é igual
    # ao peptídeo informado
    if seq_rev_comp.reverse_complement().translate() == peptideo:
        # Se a sequência reversa complementar está presente em DNA, adicione-a em "lista_sequencias"
        # O que é adicionado não é o reverso complementar, mas sim a sequência que codifica o peptídeo
        # em seu reverso complementar
        if str(seq_rev_comp) in dna:
            lista_sequencias.append(str(seq_rev_comp))

# Como a resposta gerada é grande, escrevê-la em um arquivo é a melhor solução
for resposta in lista_sequencias:
    with open('resposta.txt', 'a') as txt:
        txt.write(resposta)
        txt.write('\n')
