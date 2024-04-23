# --- Dado: Uma string de DNA com no máximo mil nucleotídeos --- #
# --- Problema: A posição e tamanho da sequência palindrômica. O tamanho deve ser de 4 a 12 nucleotídeos --- #

# --- Importar as bibliotecas --- #
from Bio import SeqIO
from Bio.Seq import Seq

# --- Indicar o arquivo --- #
arquivo = ''

# --- Obter a sequência --- #
sequencia = ''
for registro in SeqIO.parse(arquivo, 'fasta'):
    sequencia = registro.seq

# --- Separar as substrings da sequência --- #
for k in range(4, 13):
    # --- Lista com as substrings --- #
    substrings = [Seq(sequencia[i:i+k]) for i in range(len(sequencia)) if len(sequencia[i:i+k]) == k]

    # --- Obter a substring e qual a sua posição --- #
    for posicao, sub in enumerate(substrings, start=1):
        # --- Obter a sequçência reversa complementar da substring --- #
        rev_comp = sub.reverse_complement()

        # --- Verificar se o reverso complementar da substring é igual a mesma. Se for, é uma região palindrômica --- #
        if sub == rev_comp:
            # --- Mostrar a resposta --- #
            print(posicao, len(sub))
