# --- Dado: Coleção de n (n <= 10) strings de DNA --- #
# --- Problema: O número de strings que são iguais no modo normal e no reverso complementar --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO

# --- Indicar o arquivo --- #
arquivo = ''

# --- Criar o contador --- #
contador = 0

# --- Ler o arquivo com o Biopython --- #
for registro in SeqIO.parse(arquivo, 'fasta'):
    # --- Obter a sequência --- #
    sequencia = registro.seq

    # --- Obter a sequência reversa complementar --- #
    sequencia_reversa_complementar = sequencia.reverse_complement()

    # --- Verificar se a sequência reversa complementar é igual a original --- #
    if sequencia_reversa_complementar == sequencia:
        # --- Se for igual, o contador aumenta 1 --- #
        contador += 1

# --- Mostrar a resposta --- #
print(contador)
