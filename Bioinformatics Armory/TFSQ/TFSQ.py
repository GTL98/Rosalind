# --- Dado: Arquivo FASTQ --- #
# --- Problema: Registro FASTA presente no FASTQ --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO

# --- Informar o arquivo --- #
arquivo = 'rosalind_tfsq.txt'


# --- Ler o arquivo --- #
for registro in SeqIO.parse(arquivo, 'fastq'):
    # --- Obter o id da sequência --- #
    id_seq = registro.id

    # --- Obter a sequência --- #
    seq = registro.seq

    # --- Mostrar a resposta formatada --- #
    print(f'''>{id_seq}
{seq}''')
