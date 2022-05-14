## Problema: Um arquivo FASTQ
## Resultado: Os registros correspondentes em formato FASTA


# Importar a biblioteca
from Bio import SeqIO

# Indicar o arquivo usado
arquivo = 'rosalind_tfsq.txt'

# Abrir o arquivo para analise
analisador = SeqIO.parse(arquivo, 'fastq')

# Mostrar a resposta_peptideo
for item in analisador:
    print(f'>{item.id}')
    print(item.seq)
