## Problema: Duas strings s & t de DNA no formato FASTA que compartilham
## ma região repetida e inexata r de 32-40 pb. Por "inexata" quer dizer
## que a região r aparece com pequenas modificações (cada região difere em
## =< 3 indels).
## Resultado: O número total de ocorrências de r como uma substring de s,
## seguido pelo número total de ocorrências de r como substring de t.


# Importar a biblioteca
from Bio import SeqIO

# Informar o arquivo usado
arquivo = 'rosalind_subo.txt'

# Analisar o arquivo no formato FASTA
analisador = SeqIO.parse(arquivo, 'fasta')

# Criar uma lista_pedacos para armazenar as sequências
sequencias = [seq.seq for seq in analisador]

# Separar as sequências
seq_1 = sequencias[0]
seq_2 = sequencias[1]

# Criar a função para saber a distância HAMMING
def distancia_hamming(s1, s2, limite_erros=5):
    erros = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            erros += 1
            if erros > limite_erros:
                return erros
    return erros

# Criar a função que encontra o alinhamento local subotimo
def alinhamento(s1, s2):
    contagem_final = 0
    # Tamanho da substring informado no problema
    for tamanho in range(32, 41):
        # O tamanho da substring vai ficando menor, para pegar no intervalo solicitado
        for i in range(len(s1) - tamanho):
            contagem = 0
            for j in range(len(s2) - tamanho):
                if distancia_hamming(s1[i:i+tamanho], s2[j:j+tamanho]) <= 3:
                    contagem += 1
                    if contagem > contagem_final:
                        contagem_final = contagem
    return contagem_final
        

# Mostrar a resposta_peptideo
print(alinhamento(seq_2, seq_1), alinhamento(seq_1, seq_2))
