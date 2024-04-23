# --- Dado: Uma string de DNA de até mil nucleotídeos e uma coleção de strings como introns --- #
# --- Problema: A string da proteína resultante da tradução dos exons --- #

# --- Importar a biblioteca --- #
from Bio import SeqIO
from Bio.Seq import Seq

# --- Indicar o arquivo --- #
arquivo = ''

# --- Obter a sequência do gene --- #
dna = ''
for registro in SeqIO.parse(arquivo, 'fasta'):
    dna += registro.seq
    break

# --- Obter os introns --- #
introns = []
for registro in SeqIO.parse(arquivo, 'fasta'):
    seq = str(registro.seq)
    introns.append(seq)

# --- Remover a sequência do gene --- #
introns.pop(0)

# --- Remover os introns --- #
for intron in introns:
    dna = dna.replace(intron, '')

# --- Traduzir para proteína --- #
proteina = Seq(dna).translate(to_stop=True)

# --- Mostrar a resposta --- #
print(proteina)
