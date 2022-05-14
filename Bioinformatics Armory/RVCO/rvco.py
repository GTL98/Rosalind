## Problema: Uma coleção de n strings de DNA (n =< 10).
## Resultado: O número de strings que são iguais no sentido original e no
## reverso complementar.

# Importar a biblioteca
from Bio import SeqIO

# Indicar o arquivo usado
arquivo = 'rosalind_rvco.txt'

# Analisar o arquivo
analisador = SeqIO.parse(arquivo, 'fasta')

# Definir um contador para saber o número de strings iguais
contador = 0

# Iterar sobre cada sequência
for sequencia in analisador:
    sequencia_rvco = sequencia.reverse_complement()
    if sequencia_rvco.seq == sequencia.seq:
        contador += 1

# Mostrar a resposta_peptideo
print(contador)
