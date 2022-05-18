## Problema: Uma string de DNA com no máximo 1kb no formato FASTA
## Resultado: A posição e o comprimento de qualquer palíndromo na string com um tamanho de 4 a 12
## nucleotídeos. A resposta pode ser retornada em qualquer ordem

# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_revp.txt'

# Armazenar a string de DNA em uma variável
s = ''
for registro in SeqIO.parse(arquivo, 'fasta'):
    s = str(registro.seq)

# Criar um dicionário para armazenar os nucleotídeos para a leitura
dic_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# Armazenar em uma lista os pedaços com tamanho de 4 a 12 nucleotídeos
lista_tamanho = list(range(4, 13))
for i in lista_tamanho:
    lista_pedacos = list()
    for j in range(len(s)):
        if len(s[j:j+i]) == i:
            lista_pedacos.append(s[j:j+i])

    # Verificar se o reverso complementar do pedaço é igual ao pedaço na ordem normal
    # Se sim, então é uma região palindrômica
    for posicao, pedaco in enumerate(lista_pedacos, start=1):
        rev_comp = ''
        for nt in pedaco:
            rev_comp += dic_bases[nt]
        if rev_comp[::-1] == pedaco:
            # Como a resposta gerada é grande, salvá-la em um arquivo é a melhor opção
            with open('resposta_revp.txt', 'a') as txt:
                txt.write(f'{posicao} {len(pedaco)}\n')
